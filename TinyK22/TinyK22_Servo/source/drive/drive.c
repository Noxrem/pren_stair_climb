/**
 *--------------------------------------------------------------------\n
 *          HSLU T&A Hochschule Luzern Technik+Architektur            \n
 *--------------------------------------------------------------------\n
 *
 * \brief         Drive with PID
 * \file
 * \author        Christian Jost, christian.jost@hslu.ch
 * \date          15.04.2020
 *
 *--------------------------------------------------------------------
 */

#include <string.h>
#include "platform.h"
#include "term.h"
#include "util.h"
#include "drive.h"
#include "quad.h"
#include "motor.h"

static tCommandLineHandler clh;       // terminal command line handler

static int16_t setValueLeft;
static int16_t setValueRight;
static uint8_t kpL, kiL, kdL;
static uint8_t kpR, kiR, kdR;
//static int16_t kpL, kiL, kdL;					// PID parameters set to 16bit signed int
//static int16_t kpR, kiR, kdR;
static int16_t integL, devL, devOldL;
static int16_t integR, devR, devOldR;
static int32_t valL, valR;



#define PID_LOOPS_PER_SECOND  (1000 / PID_PERIOD)
#define ACCELERATION_OFFSET   (ACCELERATION / PID_LOOPS_PER_SECOND)
#define DECELERATION_OFFSET   (DECELERATION / PID_LOOPS_PER_SECOND)

int16_t sl[256];
int16_t sr[256];
uint8_t sli, sri;




/**
 * Sets the speed
 * @param[in] speedL
 *   the speed of the left wheel in mm/sec
 * @param[in] speedR
 *   the speed of the right wheel in mm/sec
 */
void driveSetSpeed(int16_t speedL, int16_t speedR)
{
  if (speedL > MAX_SPEED) speedL = MAX_SPEED;
  else if (speedL < -MAX_SPEED) speedL = -MAX_SPEED;

  if (speedR > MAX_SPEED) speedR = MAX_SPEED;
  else if (speedR < -MAX_SPEED) speedR = -MAX_SPEED;

  setValueLeft = speedL;
  setValueRight = speedR;
}


/**
 * This function sets the control parameters for the right motor
 * @param[in] pKpR Kp right 0..255
 * @param[in] pKiR Ki right 0..255
 * @param[in] pKdR Kd right 0..255
 */
void driveSetParametersR(uint8_t pKpR, uint8_t pKiR, uint8_t pKdR)
{
  kpR = pKpR;
  kiR = pKiR;
  kdR = pKdR;
}

/**
 * This function sets the control parameters for the left motor
 * @param[in] pKpL Kp left 0..255
 * @param[in] pKiL Ki left 0..255
 * @param[in] pKdL Kd left 0..255
 */
void driveSetParametersL(uint8_t pKpL, uint8_t pKiL, uint8_t pKdL)
{
  kpL = pKpL;
  kiL = pKiL;
  kdL = pKdL;
}

/**
 * This function contains the PID closed loop controller
 */
void driveToWork(void)
{
  static int16_t speedLeft = 0;
  static int16_t speedRight = 0;
  static int16_t setValueL = 0;
  static int16_t setValueR = 0;

  //motorSetPwmLeft(0);
  //motorSetPwmRight(0);


  // pre control calculations
  //------------------------------------------------------------------
  // 2 tests with 63 and 127 Gear_ratio = 1, Wheel_diameter = 112mm, no load, Motor_Voltage = 11.1V
  sl[sli] = (uint8_t)valL;     // 332=63  686=127
  sr[sli++] = (uint8_t)valR;   // 332=63  679=127

  // y=m*x+n => preControl: val = setValue * m + n

  //              equation 1    equation 2
  // left motor:  332=63*m+n    686=127*m+n  =>  m=5.53  n=-16
  // right motor: 332=63*m+n    679=127*m+n  =>  m=5.42  n=-10
  //
  #define M_LEFT    553        // = m * 100
  #define M_RIGHT   542        // = m * 100
  #define N_LEFT    16		// was negative before
  #define N_RIGHT   10
  //------------------------------------------------------------------


  speedLeft = ((speedLeft * 1) + quadGetSpeedLeft())/2;
  speedRight = ((speedRight * 1) + quadGetSpeedRight())/2;

  if (setValueRight > setValueR) {                                        // accelerate right wheel
    setValueR += ACCELERATION_OFFSET;
    if (setValueRight < setValueR) setValueR = setValueRight;
  }
  if (setValueRight < setValueR) {                                        // decelerate right wheel
    setValueR -= DECELERATION_OFFSET;
    if (setValueRight > setValueR) setValueR = setValueRight;
  }

  if (setValueLeft > setValueL) {                                         // decelerate left wheel
    setValueL += ACCELERATION_OFFSET;
    if (setValueLeft < setValueL) setValueL = setValueLeft;
  }
  if (setValueLeft < setValueL) {                                         // decelerate left wheel
    setValueL -= DECELERATION_OFFSET;
    if (setValueLeft > setValueL) setValueL = setValueLeft;
  }

  if (setValueL)
  {
    devL = (setValueL - speedLeft);       // calc deviation: max devL = +2000 - -2000 = 4000
    valL = (kpL * devL);                  // P-Part: max (kpL * devL) = 1024000
    if (kiL) integL += devL;              // I-Part with anti-windup
    valL += (kiL * integL);
    valL += (kdL*(setValueL-devOldL));    // D-Part
    devOldL = setValueL;
    valL /= 100;                         // scaling (before it was 1000)

    // pre control
    // y=m*x+n => preControl: setValue*m + n
//    valL += (M_LEFT * setValueL) / 100 + (setValueL > 0 ? N_LEFT : -N_LEFT);

    if (valL > MOTOR_MAX_VALUE) {
      valL = MOTOR_MAX_VALUE;
      integL -= devL;											// anti wind-up
    }
    else if (valL < -MOTOR_MAX_VALUE) {
      valL = -MOTOR_MAX_VALUE;
      integL += devL;											// anti wind-up
    }
  }
  else {
    valL = integL = devOldL = 0;
  }

  if (setValueR)
  {
    devR = (setValueR - speedRight);      // calc deviation
    valR = (kpR * devR);                  // P-Part: (max kpX = 2000 * 255 = 510'000)
    if (kiR) integR += devR;              // I-Part: with anti-windup below
    valR += (kiR * integR);
    valR += (kdR*(setValueR-devOldR));    // D-Part
    devOldR = setValueR;
    valR /= 100;                         // scaling (before it was 1000)

//    // pre control
//    // y=m*x+n => preControl: setValue*m + n
//    valR += (M_RIGHT * setValueR) / 100 + (setValueR > 0 ? N_RIGHT : -N_RIGHT);

    if (valR > MOTOR_MAX_VALUE) {
      valR = MOTOR_MAX_VALUE;
      integR -= devR;                     // anti wind-up
    }
    else if (valR < -MOTOR_MAX_VALUE) {
      valR = -MOTOR_MAX_VALUE;
      integR += devR;                     // anti wind-up
    }
  }
  else {
    valR = integR = devOldR = 0;
  }

  motorSetPwmLeft((int8_t)valL);
  motorSetPwmRight((int8_t)valR);
}

/**
 * Argument parser for setPIDParam command
 * Extracts the pid parameters out of the args string
 *
 * @param[in] args
 * 	the arguments to parse
 * @param[out] pkp
 * 	Address of variable to save the output P-value
 * @param[out] pki
 * 	Address of variable to save the output I-value
 * @param[out] pkd
 * 	Address of variable to save the output D-value
 **/
tError parsePIDParam(const char *args, uint8_t *pkp, uint8_t *pki, uint8_t *pkd)
{
	tError result = EC_INVALID_ARG;
	result = utilScanDecimal8u(&args, pkp);		// scan the first argument (kp parameter)
	if (result != EC_SUCCESS) return result;
	// TODO implement command parsing

	result = utilScanDecimal8u(&args, pki);		// scan the second argument (ki parameter)
	if(result != EC_SUCCESS) return result;

	result = utilScanDecimal8u(&args, pkd);		// scan the third argument (kd parameter)
	if(result != EC_SUCCESS) return result;
	return EC_SUCCESS;
}
/**
 * Command line parser for the drive PID controller.
 *
 * @param[in] cmd
 *   the command to parse
 */
tError driveParseCommand(const char *cmd)
{
  tError result = EC_INVALID_ARG;
  if (strcmp(cmd, "help") == 0)
  {
    termWriteLine("drv (drive) commands:");
    termWriteLine("  help");
    termWriteLine("  setSpd [right(mm/s)] [left(mm/s)]");
    termWriteLine("  setPIDParamR [kp 0..255] [ki 0..255] [kd 0..255]");
    termWriteLine("  setPIDParamL [kp 0..255] [ki 0..255] [kd 0..255]");
    termWriteLine("  status");
    result = EC_SUCCESS;
  }
  else if (strncmp(cmd, "setSpd", sizeof("setSpd")-1) == 0)
    {
      cmd += sizeof("setSpd");
      int16_t drvSpdR;
      int16_t drvSpdL;

      result = utilScanDecimal16s(&cmd, &drvSpdR);		// parse the message to get the right motor speed
      if(result != EC_SUCCESS) return result;

      result = utilScanDecimal16s(&cmd, &drvSpdL);		// parse the message to get the left motor speed
      if(result != EC_SUCCESS) return result;

      driveSetSpeed(drvSpdL, drvSpdR);	// set the desired speed of the motors
      result = EC_SUCCESS;
    }
  else if (strncmp(cmd, "setPIDParamR", sizeof("setPIDParamR")-1) == 0)
  {
    cmd += sizeof("setPIDParamR");
    uint8_t kp;
    uint8_t ki;
    uint8_t kd;

    result = parsePIDParam(cmd, &kp, &ki, &kd);
    if(result != EC_SUCCESS) return result;
    driveSetParametersR(kp, ki, kd);	// Set PID right parameters

    char str[6];														// Return the received value for checking
    termWrite("PIDR: ");
    utilNum16sToStr(str, sizeof(str), kp);
    termWrite(str);
    termWrite(" ");
    utilNum16sToStr(str, sizeof(str), ki);
    termWrite(str);
    termWrite(" ");
    utilNum16sToStr(str, sizeof(str), kd);
    termWriteLine(str);
    result = EC_SUCCESS;
  }
  else if (strncmp(cmd, "setPIDParamL", sizeof("setPIDParamL")-1) == 0)
	{
		cmd += sizeof("setPIDParamL");
    uint8_t kp;
    uint8_t ki;
    uint8_t kd;

    result = parsePIDParam(cmd, &kp, &ki, &kd);
		if(result != EC_SUCCESS) return result;
		driveSetParametersL(kp, ki, kd);	// Set PID left parameters

		char str[6];														// Return the received value for checking
		termWrite("PIDL: ");
		utilNum16sToStr(str, sizeof(str), kp);
		termWrite(str);
		termWrite(" ");
		utilNum16sToStr(str, sizeof(str), ki);
		termWrite(str);
		termWrite(" ");
		utilNum16sToStr(str, sizeof(str), kd);
		termWriteLine(str);
		result = EC_SUCCESS;
	}
  else if (strcmp(cmd, "status") == 0)	// returns state of the motor values
  {
	  termWriteLine("drive status: ");
	  termWrite("SetSpdR: ");							// return the set speed right
	  termWriteNum16s(setValueRight);
	  termWriteLine("");
	  termWrite("SetSpdL: ");							// return the set speed left
	  termWriteNum16s(setValueLeft);
	  termWriteLine("");
	  termWrite("PIDR: ");								// return the PID parameters right
	  termWriteNum16s(kpR);
	  termWrite(" ");
	  termWriteNum16s(kiR);
	  termWrite(" ");
	  termWriteNum16s(kdR);
	  termWriteLine("");
	  termWrite("PIDL: ");								// return the PID parameters left
	  termWriteNum16s(kpL);
	  termWrite(" ");
	  termWriteNum16s(kiL);
	  termWrite(" ");
	  termWriteNum16s(kdL);
	  termWriteLine("");
	  result = EC_SUCCESS;
  }
  return result;
}

void driveInit(void)
{
  kpL = kpR = 50;	// Tested values with only the Gefyra without bridge
  kiL = kiR = 10;
  kdL = kdR = 0;
  setValueLeft = setValueRight = 00;  //30... 7sec 30m = 4cm/sec

  // register terminal command line handler
  termRegisterCommandLineHandler(&clh, "drv", "(drive)", driveParseCommand);
}
