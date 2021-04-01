/**
 *--------------------------------------------------------------------\n
 *          HSLU T&A Hochschule Luzern Technik+Architektur            \n
 *--------------------------------------------------------------------\n
 *
 * \brief         quadrature decoder
 * \file
 * \author        Christian Jost, christian.jost@hslu.ch
 * \date          15.04.2020
 *
 *--------------------------------------------------------------------
 */
#ifndef SOURCES_DRIVE_QUAD_H_
#define SOURCES_DRIVE_QUAD_H_

int16_t quadGetRPMLeft(void);
int16_t quadGetRPMRight(void);
int16_t quadGetSpeedLeft(void);
int16_t quadGetSpeedRight(void);
int16_t quadGetDistanceLeft(void);
int16_t quadGetDistanceRight(void);
void quadContinuousSpeedTransmission(void);

tError quadParseCommand(const char *cmd);

void quadInit(void);

#endif /* SOURCES_DRIVE_QUAD_H_ */
