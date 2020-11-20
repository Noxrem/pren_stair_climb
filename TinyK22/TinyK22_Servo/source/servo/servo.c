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
#include "map.h"
#include <string.h>

static tCommandLineHandler clh;       // terminal command line handler

/**
 * Prints the current degree value of the servo at the Pin (servo).
 *
 * @param[in] servo
 * 	string that takes the servo pin number e.g. "pta4" and prints it
 *
 * @param[in] value
 * 	value to print
 */
void servoPrintValue(char *servo, uint16_t value)
{
	char str[4];
	utilNum16uToStr(str, sizeof(str), value);		// converts the value to string
	termWrite("Servo ");
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
    termWriteLine("  pta4 [0..180]");					// Servo on pin PTA4 with 0..180 degrees
    termWriteLine("  pta5 [0..180]");					// Servo on pin PTA5 with 0..180 degrees
    termWriteLine("  pta45 [0..180]");					// Servo on pin PTA4 and PTA5 with 0..180 degrees
    termWriteLine("  status");
    result = EC_SUCCESS;
  }
	else if (strncmp(cmd, "pta45", sizeof("pta45") - 1) == 0)
	{
		cmd += sizeof("pta45");						// cuts off the "pta45" from the string, now the value afterwards is in cmd
		uint16_t v;
		result = utilScanDecimal16u(&cmd, &v);		// test if it is a decimal
		if (result != EC_SUCCESS) return result;
//		FTM0->CONTROLS[1].CnV = v;
//		FTM0->CONTROLS[2].CnV = v;

		if (v < 0 || v > 180) return EC_INVALID_ARG;	// if the value is out of bound (0...180) throw error

		uint16_t ch_value = mapRangeToAnother(v, 0, 180, SERVO_CnV_MIN,
				SERVO_CnV_MAX);    						// Map the value from (0...180) to the range of the Servo pulse width
		FTM0->CONTROLS[1].CnV = ch_value;				// Set PWM pulse width of PTA4
		FTM0->CONTROLS[2].CnV = ch_value;				// Set PWM Pulse width of PTA5

		servoPrintValue("pta45", v);				// Print current degree of servo
		result = EC_SUCCESS;
	}
	else if (strncmp(cmd, "pta4", sizeof("pta4") - 1) == 0)
	{
		cmd += sizeof("pta4");						// cuts off the "pta4" from the string, now the value afterwards is in cmd
		uint16_t v;
		result = utilScanDecimal16u(&cmd, &v);		// test if it is a decimal
		if (result != EC_SUCCESS) return result;
		//FTM0->CONTROLS[1].CnV = v;

		if (v < 0 || v > 180) return EC_INVALID_ARG;	// if the value is out of bound (0...180) throw error

		uint16_t ch_value = mapRangeToAnother(v, 0, 180, SERVO_CnV_MIN,
				SERVO_CnV_MAX);    						// Map the value from (0...180) to the range of the Servo pulse width
		FTM0->CONTROLS[1].CnV = ch_value;				// Set PWM pulse width

		servoPrintValue("pta4", v);				// Print current degree of servo
		result = EC_SUCCESS;
	}
	else if (strncmp(cmd, "pta5", sizeof("pta5") - 1) == 0)
	{
		cmd += sizeof("pta5");						// cuts off the "pta5" from the string, now the value afterwards is in cmd
		uint16_t v;
		result = utilScanDecimal16u(&cmd, &v);		// test if it is a decimal
		if (result != EC_SUCCESS) return result;
		//FTM0->CONTROLS[2].CnV = v;

		if (v < 0 || v > 180) return EC_INVALID_ARG;	// if the value is out of bound (0...180) throw error

		uint16_t ch_value = mapRangeToAnother(v, 0, 180, SERVO_CnV_MIN,
				SERVO_CnV_MAX);    						// Map the value from (0...180) to the range of the Servo pulse width
		FTM0->CONTROLS[2].CnV = ch_value;				// Set PWM pulse width

		servoPrintValue("pta5", v);				// Print current degree of servo
		result = EC_SUCCESS;
	}
	else if (strncmp(cmd, "status", sizeof("status") - 1) == 0)
	{
		// TODO there is a small conversion error
		uint16_t degPTA4 = mapRangeToAnother(FTM0->CONTROLS[1].CnV,
				SERVO_CnV_MIN, SERVO_CnV_MAX, 0, 180);	// Convert ftm0 channel value to degrees (0..180)
		servoPrintValue("pta4", degPTA4);				// Print current degree of servo
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
	#if SERVO_PTA4_ENABLE
	// PTA4 Muxing for FTM0_CH1
	PORTA->PCR[4] = PORT_PCR_MUX(3);

	// initialy set servo to a 0 degree position (PWM to a ~1ms pulse)
	FTM0->CONTROLS[1].CnV = SERVO_CnV_MIN;

	// FTM0 channel configuration as edge-align pwm and high-true pulses
	FTM0->CONTROLS[1].CnSC = FTM_CnSC_MSx(2) | FTM_CnSC_ELSx(2);
	#endif

	#if SERVO_PTA5_ENABLE
	// PTA5 Muxing for FTM0_CH2
	PORTA->PCR[4] = PORT_PCR_MUX(3);

	// initialy set servo to a 0 degree position (PWM to a ~1ms pulse)
	FTM0->CONTROLS[2].CnV = SERVO_CnV_MIN;

	// FTM0 channel configuration as edge-align pwm and high-true pulses
	FTM0->CONTROLS[2].CnSC = FTM_CnSC_MSx(2) | FTM_CnSC_ELSx(2);
	#endif

  // register terminal command line handler
  termRegisterCommandLineHandler(&clh, "srv", "(servo)", servoParseCommand);
}

