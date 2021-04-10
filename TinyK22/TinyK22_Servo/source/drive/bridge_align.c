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
#include "platform.h"
#include "term.h"
#include "util.h"
#include "drive.h"
#include "quad.h"
#include "motor.h"
#include "bridge_align.h"

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

void bridgeAlignInit(void)
{


  // register terminal command line handler
  termRegisterCommandLineHandler(&clh, "drv", "(drive)", driveParseCommand);
}
