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

bool getMotorFLT(char side);
void setMotorDIR(char side, bool value);
void setMotorSLP(char side, bool value);
void motorInit(void);

// macros to switch a pin configuration from GPIO to FTM-Mode and vice versa
#define MOTOR_RIGHT_PWM() 		(PORTD->PCR[0] = PORT_PCR_MUX(4))  // PTD0: FTM3_CH0	Motor 1
#define MOTOR_RIGHT_GPIO()      (PORTD->PCR[0] = PORT_PCR_MUX(1))  // PTD0: GPIO		Motor 1
#define MOTOR_LEFT_PWM()        (PORTD->PCR[1] = PORT_PCR_MUX(4))  // PTD1: FTM3_CH1	Motor 2
#define MOTOR_LEFT_GPIO()       (PORTD->PCR[1] = PORT_PCR_MUX(1))  // PTD1: GPIO		Motor 2

// GPIO PDIR (port direction input register), GPIO PDOR (port direction output register macros
#define MOTOR_R_FLT_PDIR		GPIOB->PDIR
#define MOTOR_R_FLT_PIN			2
#define MOTOR_L_FLT_PDIR		GPIOB->PDIR
#define MOTOR_L_FLT_PIN			3
#define MOTOR_R_SLP_PDOR		GPIOC->PDOR
#define MOTOR_R_SLP_PIN			10
#define MOTOR_L_SLP_PDOR		GPIOC->PDOR
#define MOTOR_L_SLP_PIN			11
#define MOTOR_R_DIR_PDOR		GPIOC->PDOR
#define MOTOR_R_DIR_PIN			8
#define MOTOR_L_DIR_PDOR		GPIOC->PDOR
#define MOTOR_L_DIR_PIN			9

#endif /* SOURCES_DRIVE_MOTOR_H_ */
