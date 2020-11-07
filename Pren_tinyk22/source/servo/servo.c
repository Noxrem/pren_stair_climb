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
    termWriteLine("  status");
    result = EC_SUCCESS;
  }
  else if (strncmp(cmd, "pta4", sizeof("pta4")-1) == 0)
  {
	  cmd += sizeof("pta4");											// adds chars to the command char[] the amount of "pta4\0"
	  uint16_t v;
	  result = utilScanDecimal16u(&cmd, &v);							// test if it is a decimal
	  if (result != EC_SUCCESS) return result;
	  if (v < 0 || v > 180) return EC_INVALID_ARG;						// if the value is out of bound (0...180) throw error
	  {
		  uint16_t ch_value = mapRangeToAnother(v, 0, 180, SERVO_CnV_MIN, SERVO_CnV_MAX);	// Map the value from (0...180) to the range of the Servo pulse width
	  	  FTM0->CONTROLS[1].CnV = ch_value;								// Set PWM pulse width
	  }
	  result = EC_SUCCESS;
  }
  else if (strncmp(cmd, "status", sizeof("status")-1) == 0)
  {
	  char degree[8];
	  // TODO implement conversion from FTM0 channel value to range of degree (0...180)
	  utilNum16uToStr(degree, sizeof(degree), FTM0->CONTROLS[1].CnV);	// converts the channel 1 pwm value to string
	  termWrite("Servo PTA4 at: ");
	  termWrite(degree);
	  termWriteLine(" degrees");
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
	#ifdef SERVO_PTA4_ENABLE
	// PTA4 Muxing for FTM0_CH1
	PORTA->PCR[4] = PORT_PCR_MUX(3);

	// initialy set servo PWM to a 1ms pulse
	FTM0->CONTROLS[1].CnV = 250;

	// FTM0 channel configuration as edge-align pwm and high-true pulses
	FTM0->CONTROLS[1].CnSC = FTM_CnSC_MSx(2) | FTM_CnSC_ELSx(2);
	#endif

  // register terminal command line handler
  termRegisterCommandLineHandler(&clh, "srv", "(servo)", servoParseCommand);
}

