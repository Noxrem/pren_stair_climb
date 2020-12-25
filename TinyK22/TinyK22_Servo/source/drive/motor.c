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

#include "platform.h"
#include "motor.h"
#include "ftm3.h"
#include "term.h"
#include "util.h"
#include <string.h>
#include <stdbool.h>

// https://ebldc.com/?p=86

static tCommandLineHandler clh;       // terminal command line handler
static int8_t valueRight;
static int8_t valueLeft;



/**
 * Increments or decrements the PWM value oft the right wheel
 * @param[in] value
 *   a positive or negative value to add
 */
void motorIncrementPwmRight(int8_t value)
{
  int32_t v = valueRight + value;
  if (v > MOTOR_MAX_VALUE) v = MOTOR_MAX_VALUE;
  if (v < -MOTOR_MAX_VALUE) v = -MOTOR_MAX_VALUE;
  motorSetPwmRight((int8_t)v);
}


/**
 * Increments or decrements the PWM value oft the left wheel
 * @param[in] value
 *   a positive or negative value to add
 */
void motorIncrementPwmLeft(int8_t value)
{
  int32_t v = valueLeft + value;
  if (v > MOTOR_MAX_VALUE) v = MOTOR_MAX_VALUE;
  if (v < -MOTOR_MAX_VALUE) v = -MOTOR_MAX_VALUE;
  motorSetPwmLeft((int8_t)v);
}


/**
 * Sets the PWM value of the right wheel
 *
 * @param[in] value
 *   the value between -MOTOR_MAX_VALUE..0..+MOTOR_MAX_VALUE
 *   A value of '0' stops the wheel.
 */
void motorSetPwmRight(int8_t value)
{
  if (value > MOTOR_MAX_VALUE) value = MOTOR_MAX_VALUE;
  if (value < -MOTOR_MAX_VALUE) value = -MOTOR_MAX_VALUE;
  valueRight = value;

  if (value < 0)
  {
	  // drive backward
	  value = -value;             	// value has to be a positive channel value!
	  setMotorDIR('R', true);
	  MOTOR_RIGHT_PWM();			// set motor right as timer Pin (pwm signal)
  }
  else if (value > 0)
  {
	  // drive forward
	  setMotorDIR('R', false);
	  MOTOR_RIGHT_PWM();		// set motor right as timer Pin (pwm signal)
  }
  else
  {
	  // stop
	  MOTOR_RIGHT_GPIO();			// set motor right as GPIO Pin (low-level)
  }
  int16_t v = (uint16_t)(((FTM3_MODULO + 1) * ((uint32_t)value)) / MOTOR_MAX_VALUE);
  FTM3->CONTROLS[0].CnV = v;
}


/**
 * Sets the PWM value of the left wheel
 *
 * @param[in] value
 *   the value between -MOTOR_MAX_VALUE..0..+MOTOR_MAX_VALUE
 *   A value of '0' stops the wheel.
 */
void motorSetPwmLeft(int8_t value)
{
  if (value > MOTOR_MAX_VALUE) value = MOTOR_MAX_VALUE;
  if (value < -MOTOR_MAX_VALUE) value = -MOTOR_MAX_VALUE;
  valueLeft = value;

  if (value < 0)
  {
	  // drive backwards
	  value = -value;
	  setMotorDIR('L', true);
	  MOTOR_LEFT_PWM();				// set motor left as timer Pin (pwm signal)
  }
  else if (value > 0)
  {
	  // drive forward
	  setMotorDIR('L', false);
	  MOTOR_LEFT_PWM();				// set motor left as timer Pin (pwm signal)
  }
  else
  {
	  // stop
	  MOTOR_LEFT_GPIO();			// set motor left as GPIO Pin (low-level)
  }
  int16_t v = (uint16_t)(((FTM3_MODULO + 1) * ((uint32_t)value)) / MOTOR_MAX_VALUE);
  FTM3->CONTROLS[1].CnV = v;
}


/**
 * Command line parser for this file.
 * This code is complete and works.
 *
 * @param[in] cmd
 *   the command to parse
 */
tError motorParseCommand(const char *cmd)
{
  tError result = EC_INVALID_ARG;
  if (strcmp(cmd, "help") == 0)
  {
    termWriteLine("mot (motor) commands:");
    termWriteLine("  help");
    termWriteLine("  setL [-100..100]");
    termWriteLine("  setR [-100..100]");
    termWriteLine("  status");
    result = EC_SUCCESS;
  }
  else if (strncmp(cmd, "setL", sizeof("setL")-1) == 0)
  {
    cmd += sizeof("setL");
    int16_t v;
    result = utilScanDecimal16s(&cmd, &v);
    if (result != EC_SUCCESS) return result;
    motorSetPwmLeft((int16_t)((MOTOR_MAX_VALUE * v) / 100));
  }
  else if (strncmp(cmd, "setR", sizeof("setR")-1) == 0)
  {
    cmd += sizeof("setR");
    int16_t v;
    result = utilScanDecimal16s(&cmd, &v);
    if (result != EC_SUCCESS) return result;
    motorSetPwmRight((int16_t)((MOTOR_MAX_VALUE * v) / 100));
  }
  return result;
}

/**
 * Returns the GPIO PDOR value of the motor driver board FLT Pin
 *
 * @param[in] side
 *   side of the motor: R or L
 *
 * @return
 * 	 value of the pin
 */
bool getMotorFLT(char side)
{
	if(side == 'R')
	{
		return (MOTOR_R_FLT_PDIR & (uint32_t)(1 << MOTOR_R_FLT_PIN));	// return motor R fault pin value
	}
	else if(side == 'L')
	{
		return (MOTOR_L_FLT_PDIR & (uint32_t)(1 << MOTOR_L_FLT_PIN));	// return motor L fault pin value
	}
	else { return false; }	// error: invalid argument
}

/**
 * Sets the GPIO PDOR value of the motor driver board DIR Pin
 *
 * @param[in] side
 *   side of the motor: R or L
 *
 * @param[in] value
 * 	 value to set the pin to
 */
void setMotorDIR(char side, bool value)
{
	if(side == 'R')
	{
		if(value) { MOTOR_R_DIR_PDOR |= (uint32_t)(1 << MOTOR_R_DIR_PIN); }	// set motor R direction pin
		else { MOTOR_R_DIR_PDOR &= ~(uint32_t)(1 << MOTOR_R_DIR_PIN); }
	}
	else if(side == 'L')
	{
		if(value) { MOTOR_L_DIR_PDOR |= (uint32_t)(1 << MOTOR_L_DIR_PIN); }	// set motor L direction pin
		else { MOTOR_L_DIR_PDOR &= ~(uint32_t)(1 << MOTOR_L_DIR_PIN); }
	}
	else { }	// error: invalid argument
}

/**
 * Sets the GPIO PDOR value of the motor driver board SLP Pin
 *
 * @param[in] side
 *   side of the motor: R or L
 *
 * @param[in] value
 * 	 value to set the pin to
 */
void setMotorSLP(char side, bool value)
{
	if(side == 'R')
	{
		if(value) { MOTOR_R_SLP_PDOR |= (uint32_t)(1 << MOTOR_R_SLP_PIN); }	// set motor R sleep pin
		else { MOTOR_R_SLP_PDOR &= ~(uint32_t)(1 << MOTOR_R_SLP_PIN); }
	}
	else if(side == 'L')
	{
		if(value) { MOTOR_L_SLP_PDOR |= (uint32_t)(1 << MOTOR_L_SLP_PIN); }	// set motor L sleep pin
		else { MOTOR_L_SLP_PDOR &= ~(uint32_t)(1 << MOTOR_L_SLP_PIN); }
	}
	else { }	// error: invalid argument
}

/**
 * Initializes the motor driver:
 * - Motor R A: PTD0, FTM3_CH0, Mux:4
 * - Motor R B: PTE5, FTM3_CH0, Mux:6
 * - Motor L A: PTD1, FTM3_CH1, Mux:4
 * - motor L B: PTE6, FTM3_CH1, Mux:6
 *
 * Initializes the motor driver:
 * - Motor R FLT: PTB2, GPIO, Mux:1
 * - Motor L FLT: PTB3, GPIO, Mux:1
 * - Motor R PWM: PTD0, FTM3_CH0, Mux:4
 * - Motor L PWM: PTD1, FTM3_CH1, Mux:4
 * - Motor R DIR: PTC8, GPIO, Mux:1			low: current from A to B, high: current from B to A
 * - Motor L DIR: PTC9, GPIO, Mux:1			low: current from A to B, high: current from B to A
 * - Motor R SLP: PTC10, GPIO, Mux:1
 * - Motor L SLP: PTC11, GPIO, Mux:1
 */
void motorInit(void)
{
	// GPIO Direction
	GPIOB->PDDR &= ~(1<<2 | 1<<3);	// configure PTB2 & PTB3 (FLT) as input

	GPIOD->PDDR |= 1<<0 | 1<<1;					// configure PTD0 & PTD1 (PWM) as output
	GPIOC->PDDR |= 1<<8 | 1<<9 | 1<<10 | 1<<11;	// configure PTC8, PTC9, PTC10 & PTC11 as output

	// PORT as GPIO with pull-up (FLT)
	PORTB->PCR[2] = PORT_PCR_MUX(1) | PORT_PCR_PE(1) | PORT_PCR_PS(1);	// PTB2 as GPIO with pull-up
	PORTB->PCR[3] = PORT_PCR_MUX(1) | PORT_PCR_PE(1) | PORT_PCR_PS(1);	// PTB3 as GPIO with pull-up

	// PORTC as GPIO
	PORTC->PCR[8] = PORT_PCR_MUX(1);
	PORTC->PCR[9] = PORT_PCR_MUX(1);
	PORTC->PCR[10] = PORT_PCR_MUX(1);
	PORTC->PCR[11] = PORT_PCR_MUX(1);

	// Motor Sleep Pin (high to enable motor)
	setMotorSLP('R', true);
	setMotorSLP('L', true);

	// Motor Direction Pin (low: current from A to B)
	setMotorDIR('R', false);
	setMotorDIR('L', false);

	// GPIO Clear Bits on PTD0 & PTD1
	GPIOD->PCOR |= 1<<0 | 1<<1;

	// configures the pin muxing of the 2 pins as GPIO-Pin.
	// the output level will be '0' (break operation) because of the configuration above.
	MOTOR_RIGHT_GPIO();
	MOTOR_LEFT_GPIO();


//  // Configure the pin direction of the 4 pins as output.
//  GPIOD->PDDR = 1<<0 | 1<<1;               // configure PTD0 & PTD1 as output
//  GPIOE->PDDR = 1<<5 | 1<<6;               // configure PTE5 & PTE6 as output
//
//  // set the pin value of all of the 4 pins to '1'
//  GPIOD->PSOR = 1<<0 | 1<<1;               // set PTD0 & PTD1 = 1
//  GPIOE->PSOR = 1<<5 | 1<<6;               // set PTE5 & PTE6 = 1
//
//  // configures the pin muxing of all of the 4 pins as GPIO-Pin.
//  // the output level will be '1' because of the configuration above.
//  MOTOR_LEFT_A_GPIO();
//  MOTOR_LEFT_B_GPIO();
//  MOTOR_RIGHT_A_GPIO();
//  MOTOR_RIGHT_B_GPIO();

	// set PWM value to 0
	FTM3->CONTROLS[0].CnV = 0;
	FTM3->CONTROLS[1].CnV = 0;

	// configure both channels as edge aligned PWM with high-true pulses
	FTM3->CONTROLS[0].CnSC = FTM_CnSC_MSx(2) | FTM_CnSC_ELSx(2);
	FTM3->CONTROLS[1].CnSC = FTM_CnSC_MSx(2) | FTM_CnSC_ELSx(2);

  // register terminal command line handler
  termRegisterCommandLineHandler(&clh, "mot", "(motor)", motorParseCommand);
}
