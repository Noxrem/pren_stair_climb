/**
 *--------------------------------------------------------------------\n
 *          HSLU T&A Hochschule Luzern Technik+Architektur            \n
 *--------------------------------------------------------------------\n
 *
 * \brief         Common settings of the FTM0
 * \file
 * \author        Christian Jost, christian.jost@hslu.ch
 * \date          04.04.2020
 *
 *--------------------------------------------------------------------
 */

#ifndef SOURCES_FTM0_H_
#define SOURCES_FTM0_H_

#define FTM0_CLOCK              250000  // 250 kHz
#define FTM0_MODULO				2500	// for a frequency of 100 Hz (250kHz / 1) / 100Hz = 2500

void ftm0Init(void);

#endif /* SOURCES_FTM0_H_ */
