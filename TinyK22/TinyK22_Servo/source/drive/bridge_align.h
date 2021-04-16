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

#ifndef SOURCES_DRIVE_BRIDGE_ALIGN_H_
#define SOURCES_DRIVE_BRIDGE_ALIGN_H_

#define SWITCH_RIGHT_PDIR GPIOB->PDIR
#define SWITCH_RIGHT_PIN	1
#define SWITCH_LEFT_PDIR	GPIOB->PDIR
#define SWITCH_LEFT_PIN		3

#define DEFAULT_ALIGN_SPEED 20	// Speed for the alignment

void ProcessBridgeAlign(void);
tError bridgeAlignParseCommand(const char *cmd);
void bridgeAlignInit(void);


#endif /* SOURCES_DRIVE_BRIDGE_ALIGN_H_ */
