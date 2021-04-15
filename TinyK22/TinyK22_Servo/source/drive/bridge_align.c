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
#include "term.h"
#include "util.h"
#include "drive.h"
#include "quad.h"
#include "motor.h"
#include "source/drive/bidge_align.h"

static tCommandLineHandler clh;       // terminal command line handler



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
    result = EC_SUCCESS;
  }
  else if (strncmp(cmd, "setSpd", sizeof("setSpd")-1) == 0)
	{
		cmd += sizeof("setSpd");
		bool aligned = false;
		int16_t algnSpeedR = ALIGN_SPEED;				// The speed the device is aligned with
		int16_t algnSpeedL = ALIGN_SPEED;


		driveSetSpeed(algnSpeedR, algnSpeedL);	// Start the motors
		while(aligned)
		{
			if(!(SWITCH_LEFT_PDIR & (uint32_t)(1 << SWITCH_LEFT_PIN)))	// if the left switch is activated (touching the stairs)
			{
				algnSpeedL = 0;
				driveSetSpeed(algnSpeedR, algnSpeedL);	// stop the left wheel and continue with the right wheel
			}
			if(!(SWITCH_RIGHT_PDIR & (uint32_t)(1 << SWITCH_RIGHT_PIN)))	// if the left switch is activated (touching the stairs)
			{
				algnSpeedR = 0;
				driveSetSpeed(algnSpeedR, algnSpeedL);	// stop the right wheel and continue with the left wheel
			}
			if(!algnSpeedL && !algnSpeedR)	// Leave the while-loop, when both switches have been touched (the device is aligned)
			{
				break;	// leave the while loop
			}
		}
		result = EC_SUCCESS;
	}
  return result;
}

void bridgeAlignInit(void)
{
	// GPIO direction
	GPIOD->PDDR &= ~(1<<1 | 1<<2);	// Configure PTA1 and PTA2 as input

	// Set input with pull-up
	PORTD->PCR[1] = PORT_PCR_MUX(1) | PORT_PCR_PE(1) | PORT_PCR_PS(1);	// PTA1 as GPIO with pull-up
	PORTD->PCR[2] = PORT_PCR_MUX(1) | PORT_PCR_PE(1) | PORT_PCR_PS(1);	// PTA2 as GPIO with pull-up

  // register terminal command line handler
  termRegisterCommandLineHandler(&clh, "aln", "(align)", bridgeAlignParseCommand);
}
