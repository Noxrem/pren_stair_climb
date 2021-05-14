/**
 *--------------------------------------------------------------------\n
 *          HSLU T&A Hochschule Luzern Technik+Architektur            \n
 *--------------------------------------------------------------------\n
 *
 * \brief         servo driver for the TinyK22
 * \file
 * \author        Pascal Brülhart
 * \date          07.11.2020
 *
 *--------------------------------------------------------------------
 */

#include "platform.h"
#include "servo.h"
#include "ftm0.h"
#include "term.h"
#include "util.h"
//#include "UTIL1.h"
#include "map.h"
#include <string.h>

static tCommandLineHandler clh;       // terminal command line handler

/**
 * Prints the current degree value of the servo at the Pin (servo).
 *
 * @param[in] servo
 * 	string that takes the servo name e.g. "arm" and prints it
 *
 * @param[in] value
 * 	value to print
 */
void servoPrintValue(char *servo, uint16_t value)
{
	char str[4];
	utilNum16uToStr(str, sizeof(str), value);		// converts the value to string
	termWrite(servo);
	termWrite(": ");
	termWrite(str);									// Prints the given servo value
	termWriteLine(" degrees");
}
/**
 * Command line parser for this file.
 * This code is complete and works.
 *
 * @param[in] cmd
 *   the command to parse
 */
tError servoParseCommand(const char *cmd)
{
  tError result = EC_INVALID_ARG;
  if (strcmp(cmd, "help") == 0)
  {
    termWriteLine("srv (servo) commands:");
    termWriteLine("  help");
    termWriteLine("  status");
    termWriteLine("  arm [0..180]");					// Servo on pin PTD4 with 0..180 degrees
    termWriteLine("  cam [0..180]");					// Servo on pin PTA5 with 0..180 degrees
    termWriteLine("  both [0..180]");					// Servo on pin PTD4 and PTA5 with 0..180 degrees

    result = EC_SUCCESS;
  }
	else if (strncmp(cmd, "status", sizeof("status") - 1) == 0)
	{
		uint16_t degPTD4 = mapRangeToAnother(FTM0->CONTROLS[4].CnV, SERVO_CnV_MIN,
				SERVO_CnV_MAX, 0, 180);    						// Convert ftm0 channel 4 value to degrees (0..180)
		uint16_t degPTA5 = mapRangeToAnother(FTM0->CONTROLS[2].CnV, SERVO_CnV_MIN,
				SERVO_CnV_MAX, 0, 180);    						// Convert ftm0 channel 2 value to degrees (0..180)
		termWriteLine("servo status:");
		servoPrintValue("arm", degPTD4);					// Print current degree of servo
		servoPrintValue("cam", degPTA5);
		result = EC_SUCCESS;
	}
	else if (strncmp(cmd, "both", sizeof("both") - 1) == 0)
	{
		cmd += sizeof("both");										// cuts off the "both" from the string, now the value afterwards is in cmd
		uint16_t v;
		result = utilScanDecimal16u(&cmd, &v);		// test if it is a decimal
		if (result != EC_SUCCESS) return result;

		if (v < 0 || v > 180) return EC_INVALID_ARG;	// if the value is out of bound (0...180) throw error

		uint16_t ch_value = mapRangeToAnother(v, 0, 180, SERVO_CnV_MIN,
				SERVO_CnV_MAX);    									// Map the value from (0...180) to the range of the Servo pulse width
		FTM0->CONTROLS[4].CnV = ch_value;				// Set PWM pulse width of PTD4
		FTM0->CONTROLS[2].CnV = ch_value;				// Set PWM Pulse width of PTA5

		servoPrintValue("both", v);							// Print current degree of servo
		result = EC_SUCCESS;
	}
	else if (strncmp(cmd, "arm", sizeof("arm") - 1) == 0)
	{
		cmd += sizeof("arm");										// cuts off the "arm" from the string, now the value afterwards is in cmd
		uint16_t v;
		result = utilScanDecimal16u(&cmd, &v);		// test if it is a decimal
		if (result != EC_SUCCESS) return result;

		if (v < 0 || v > 180) return EC_INVALID_ARG;	// if the value is out of bound (0...180) throw error

		uint16_t ch_value = mapRangeToAnother(v, 0, 180, SERVO_CnV_MIN,
				SERVO_CnV_MAX);    									// Map the value from (0...180) to the range of the Servo pulse width
		FTM0->CONTROLS[4].CnV = ch_value;				// Set PWM pulse width

		servoPrintValue("arm", v);							// Print current degree of servo
		result = EC_SUCCESS;
	}
	else if (strncmp(cmd, "cam", sizeof("cam") - 1) == 0)
	{
		cmd += sizeof("cam");										// cuts off the "cam" from the string, now the value afterwards is in cmd
		uint16_t v;
		result = utilScanDecimal16u(&cmd, &v);		// test if it is a decimal
		if (result != EC_SUCCESS) return result;

		if (v < 0 || v > 180) return EC_INVALID_ARG;	// if the value is out of bound (0...180) throw error

		uint16_t ch_value = mapRangeToAnother(v, 0, 180, SERVO_CnV_MIN,
				SERVO_CnV_MAX);    									// Map the value from (0...180) to the range of the Servo pulse width
		FTM0->CONTROLS[2].CnV = ch_value;				// Set PWM pulse width

		servoPrintValue("cam", v);							// Print current degree of servo
		result = EC_SUCCESS;
	}
  return result;
}

/**
 * Initializes the servo motor:
 *
 */
void servoInit(void)
{
	int16_t initDegValue;											// Degree value the servos are initialized with

	#if SERVO_PTD4_ENABLE
	// PTD4 Muxing for FTM0_CH1
	PORTD->PCR[4] = PORT_PCR_MUX(4);

	// FTM0 channel configuration as edge-align pwm and high-true pulses
	FTM0->CONTROLS[4].CnSC = FTM_CnSC_MSx(2) | FTM_CnSC_ELSx(2);

	// initialy set servo arm(PTD4) to a degree position given in the h-file
	initDegValue = mapRangeToAnother(SERVO_PTD4_DEG_INIT, 0, 180, SERVO_CnV_MIN,
					SERVO_CnV_MAX);    											// Map the value from (0...180) to the range of the Servo pulse width
	FTM0->CONTROLS[4].CnV = initDegValue;						// Set PWM pulse width
	//FTM0->CONTROLS[1].CnV = SERVO_CnV_MIN;
	#endif

	#if SERVO_PTA5_ENABLE
	// PTA5 Muxing for FTM0_CH2
	PORTA->PCR[5] = PORT_PCR_MUX(3);

	// FTM0 channel configuration as edge-align pwm and high-true pulses
	FTM0->CONTROLS[2].CnSC = FTM_CnSC_MSx(2) | FTM_CnSC_ELSx(2);

	// initialy set servo cam(PTA5) to a degree position given in the h-file
	initDegValue = mapRangeToAnother(SERVO_PTA5_DEG_INIT, 0, 180, SERVO_CnV_MIN,
					SERVO_CnV_MAX);    											// Map the value from (0...180) to the range of the Servo pulse width
	FTM0->CONTROLS[2].CnV = initDegValue;						// Set PWM pulse width
	//FTM0->CONTROLS[2].CnV = SERVO_CnV_MIN;
	#endif

  // register terminal command line handler
  termRegisterCommandLineHandler(&clh, "srv", "(servo)", servoParseCommand);
}

