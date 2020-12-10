/**
 *--------------------------------------------------------------------\n
 *          HSLU T&A Hochschule Luzern Technik+Architektur            \n
 *--------------------------------------------------------------------\n
 *
 * \brief         motor driver
 * \file
 * \author        Christian Jost, christian.jost@hslu.ch
 * \date          15.04.2020
 *
 *--------------------------------------------------------------------
 */

#ifndef SOURCES_DRIVE_MOTOR_H_
#define SOURCES_DRIVE_MOTOR_H_

#define MOTOR_MAX_VALUE               127

void motorIncrementPwmRight(int8_t value);
void motorIncrementPwmLeft(int8_t value);

void motorSetPwmRight(int8_t value);
void motorSetPwmLeft(int8_t value);
void motorInit(void);

#define MOT_R_FLT()		(PORTD->PCR[0] = PORT_PCR_MUX(4))	// input pull-up
#define MOT_L_FLT	// input pull-up
#define MOT_R_PWM()		(PORTD->PCR[0] = PORT_PCR_MUX(4))	// PTD0: FTM3_CH0 output PWM
#define MOT_L_PWM()		(PORTD->PCR[1] = PORT_PCR_MUX(4))	// output PWM
#define MOT_R_SLP	// output (high-active)
#define MOT_L_SLP	// output (high-active)
#define MOT_R_DIR	// output (low: current from A to B, high: current from B to A)
#define MOT_L_DIR	// output (low: current from A to B, high: current from B to A)

#endif /* SOURCES_DRIVE_MOTOR_H_ */
