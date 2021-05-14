/**
 *--------------------------------------------------------------------\n
 *          HSLU T&A Hochschule Luzern Technik+Architektur            \n
 *--------------------------------------------------------------------\n
 *
 * \brief         Align the Gefyra and the bridge with the stairs.
 * \file
 * \author        Pascal Brülhart, pascal.bruelhart@stud.hslu.ch
 * \date          10.04.2021
 *
 *--------------------------------------------------------------------
 */

#include <string.h>
#include <stdbool.h>
#include "platform.h"
#include "bridge_align.h"
#include "term.h"
#include "util.h"
#include "drive.h"
#include "quad.h"
#include "motor.h"

static tCommandLineHandler clh;       	// terminal command line handler
static bool bridgeAlignEnabled = false;	// the device is being aligned, if true
int16_t algnSpeed;											// The speed the device is aligned with
int16_t algnSpeedR;
int16_t algnSpeedL;

/**
 * Process that gets called periodically in the main.
 * Aligns the bridge with the right and left switch.
 * Drive forward and turning off the motor when the switch on this side
 * is closed.
 */
void ProcessBridgeAlign(void)
{
	if(bridgeAlignEnabled)
	{
		if(!(SWITCH_LEFT_PDIR & (uint32_t)(1 << SWITCH_LEFT_PIN)))	// if the left switch is activated (touching the stairs)
		{
			algnSpeedL = 0;
			driveSetSpeed(algnSpeedL, algnSpeedR);	// stop the left wheel and continue with the right wheel
		}
		if(!(SWITCH_RIGHT_PDIR & (uint32_t)(1 << SWITCH_RIGHT_PIN)))	// if the left switch is activated (touching the stairs)
		{
			algnSpeedR = 0;
			driveSetSpeed(algnSpeedL, algnSpeedR);	// stop the right wheel and continue with the left wheel
		}
		if(!algnSpeedL && !algnSpeedR)	// when both switches have been touched (the device is aligned)
		{
			bridgeAlignEnabled = false;	// Stop the alignment
			termWriteLine("Alignment completed");
		}
	}
}

/**
 * Command line parser for the bridge and device alignment.
 *
 * @param[in] cmd
 *   the command to parse
 */
tError bridgeAlignParseCommand(const char *cmd)
{
  tError result = EC_INVALID_ARG;
  if (strcmp(cmd, "help") == 0)
  {
    termWriteLine("aln (align) commands:");
    termWriteLine("  help");
    termWriteLine("  start");
    termWriteLine("  stop");
    termWriteLine("  setSpd");
    termWriteLine("  status");
    result = EC_SUCCESS;
  }
  else if (strncmp(cmd, "start", sizeof("start")-1) == 0)
	{
		algnSpeedR = algnSpeed;									// Set the alignment speed
		algnSpeedL = algnSpeed;
		driveSetSpeed(algnSpeedL, algnSpeedR);	// Start the motors
		bridgeAlignEnabled = true;							// Start bridge alignment
		termWriteLine("Alignment started");
		result = EC_SUCCESS;
	}
  else if (strncmp(cmd, "stop", sizeof("stop")-1) == 0)
	{
		driveSetSpeed(0, 0);										// Stop the motors
		bridgeAlignEnabled = false;							// Stop bridge alignment
		termWriteLine("Alignment aborted");
		result = EC_SUCCESS;
	}
  else if (strncmp(cmd, "setSpd", sizeof("setSpd")-1) == 0)
	{
		cmd += sizeof("setSpd");
		result = utilScanDecimal16s(&cmd, &algnSpeed);		// parse message to get the alignment speed
		if(result != EC_SUCCESS) return result;

		result = EC_SUCCESS;
	}
  else if (strncmp(cmd, "status", sizeof("status")-1) == 0)
  {
  	termWriteLine("align status:");
  	termWrite("SetSpd: ");
  	termWriteNum16s(algnSpeed);
  	termWriteLine("");
  	result = EC_SUCCESS;
  }
  return result;
}

void bridgeAlignInit(void)
{
	// GPIO direction
	GPIOB->PDDR &= ~(1<<1 | 1<<3);	// Configure PTB1 and PTB3 as input

	// Set input with pull-up
	PORTB->PCR[1] = PORT_PCR_MUX(1) | PORT_PCR_PE(1) | PORT_PCR_PS(1);	// PTB1 as GPIO with pull-up
	PORTB->PCR[3] = PORT_PCR_MUX(1) | PORT_PCR_PE(1) | PORT_PCR_PS(1);	// PTB3 as GPIO with pull-up

	// Set default alignment speed
	algnSpeed = DEFAULT_ALIGN_SPEED;

  // register terminal command line handler
  termRegisterCommandLineHandler(&clh, "aln", "(align)", bridgeAlignParseCommand);
}
