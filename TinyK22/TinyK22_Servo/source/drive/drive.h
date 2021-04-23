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

#ifndef SOURCES_DRIVE_DRIVE_H_
#define SOURCES_DRIVE_DRIVE_H_

#define MAX_SPEED              700                        // [mm/s] before 400
#define ACCELERATION           500                        // [mm/s^2]
#define DECELERATION          3000                        // [mm/s^2] before 2000
#define PID_PERIOD              25                        // [ms]


void driveSetParametersR(uint8_t pKpR, uint8_t pKiR, uint8_t pKdR);
void driveSetParametersL(uint8_t pKpL, uint8_t pKiL, uint8_t pKdL);
void driveSetSpeed(int16_t speedL, int16_t speedR);
void driveToWork(void);
void driveInit(void);


#endif /* SOURCES_DRIVE_DRIVE_H_ */
