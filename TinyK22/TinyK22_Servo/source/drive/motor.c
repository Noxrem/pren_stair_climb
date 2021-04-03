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
static int8_t motorValueRight;
static int8_t motorValueLeft;
static int8_t motorValueWinch;
static bool motorsEnabled = false;		// Enables/disables the motors and speed update

/**
 * Getter Method if the motors are enabled/disabled
 */
bool getMotorsEnabled(void)
{
	return motorsEnabled;
}

/**
 * Increments or decrements the PWM value oft the right wheel
 * @param[in] value
 *   a positive or negative value to add
 */
void motorIncrementPwmRight(int8_t value)
{
  int32_t v = motorValueRight + value;
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
  int32_t v = motorValueLeft + value;
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
  motorValueRight = value;

  if (value < 0)
  {
	  // drive backward
	  value = -value;             	// value has to be a positive channel value!
	  motorSetDIR('R', false);
	  MOTOR_RIGHT_PWM();			// set motor right as timer Pin (pwm signal)
  }
  else if (value > 0)
  {
	  // drive forward
	  motorSetDIR('R', true);
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
  motorValueLeft = value;

  if (value < 0)
  {
	  // drive backwards
	  value = -value;
	  motorSetDIR('L', false);
	  MOTOR_LEFT_PWM();				// set motor left as timer Pin (pwm signal)
  }
  else if (value > 0)
  {
	  // drive forward
	  motorSetDIR('L', true);
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
 * Sets the PWM value of the winch motor
 *
 * @param[in] value
 *   the value between -MOTOR_MAX_VALUE..0..+MOTOR_MAX_VALUE
 *   A value of '0' stops the winch.
 */
void motorSetPwmWinch(int8_t value)
{
  if (value > MOTOR_MAX_VALUE) value = MOTOR_MAX_VALUE;
  if (value < -MOTOR_MAX_VALUE) value = -MOTOR_MAX_VALUE;
  motorValueWinch = value;

  if (value < 0)
  {
	  // drive backwards
	  value = -value;
	  motorSetDIR('W', false);
	  MOTOR_WINCH_PWM();				// set winch motor as timer Pin (pwm signal)
  }
  else if (value > 0)
  {
	  // drive forward
	  motorSetDIR('W', true);
	  MOTOR_WINCH_PWM();				// set winch motor as timer Pin (pwm signal)
  }
  else
  {
	  // stop
	  MOTOR_WINCH_GPIO();			// set motor left as GPIO Pin (low-level)
  }
  int16_t v = (uint16_t)(((FTM3_MODULO + 1) * ((uint32_t)value)) / MOTOR_MAX_VALUE);
  FTM3->CONTROLS[2].CnV = v;
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
    termWriteLine("  enable");
    termWriteLine("  disable");
    termWriteLine("  setL [-127..127]");
    termWriteLine("  setR [-127..127]");
    termWriteLine("  setW [-127..127]");
    termWriteLine("  getFltR");
    termWriteLine("  getFltL");
    termWriteLine("  status");
    result = EC_SUCCESS;
  }
  else if (strncmp(cmd, "setL", sizeof("setL")-1) == 0)
  {
    cmd += sizeof("setL");
    int16_t v;
    result = utilScanDecimal16s(&cmd, &v);
    if (result != EC_SUCCESS) return result;
//    motorSetPwmLeft((int16_t)((MOTOR_MAX_VALUE * v) / 100));	// entry in percent
    motorSetPwmLeft((int8_t)v);	// value between -127..0..127
  }
  else if (strncmp(cmd, "setR", sizeof("setR")-1) == 0)
  {
    cmd += sizeof("setR");
    int16_t v;
    result = utilScanDecimal16s(&cmd, &v);
    if (result != EC_SUCCESS) return result;
//    motorSetPwmRight((int16_t)((MOTOR_MAX_VALUE * v) / 100));
    motorSetPwmRight((int8_t)v);	// value between -127..0..127
  }
  else if (strncmp(cmd, "setW", sizeof("setW")-1) == 0)
    {
      cmd += sizeof("setW");
      if(!motorsEnabled) return EC_INVALID_CMD;	// cmd not available if the motors are disabled
      int16_t v;
      result = utilScanDecimal16s(&cmd, &v);
      if (result != EC_SUCCESS) return result;
      motorSetPwmWinch((int8_t)v);	// value between -127..0..127
    }
  else if (strncmp(cmd, "enable", sizeof("enable")-1) == 0)
  {
	  // enable motors
  	motorsEnabled = true;
	  motorSetSLP('R', true);	// set the SLP Pins of the motor driver
	  motorSetSLP('L', true);
	  motorSetSLP('W', true);	// sets the PWM to 0
	  termWriteLine("Motors enabled");
	  result = EC_SUCCESS;
  }
  else if (strncmp(cmd, "disable", sizeof("disable")-1) == 0)
  {
	  // disable motors
  	motorsEnabled = false;
	  motorSetSLP('R', false);	// clear the SLP Pins of the motor driver
	  motorSetSLP('L', false);
	  motorSetSLP('W', false);	// sets the PWM to 0
	  termWriteLine("Motors disabled");
  	  result = EC_SUCCESS;
  }
  else if (strncmp(cmd, "getFltR", sizeof("getFltR")-1) == 0)
  {
	  cmd += sizeof("getFltR");
	  if( motorGetFLT('R') == true)		// if motor R driver detected fault, return 1
	  {
		  termWriteLine("Motor R fault: 1");
	  }
	  else
	  {
		  termWriteLine("Motor R fault: 0");
	  }
	  result = EC_SUCCESS;
  }
  else if (strncmp(cmd, "getFltL", sizeof("getFltL")-1) == 0)
  {
	  cmd += sizeof("getFltL");
	  if( motorGetFLT('L') == true)		// if motor L driver detected fault, return 1
	  {
		  termWriteLine("Motor L fault: 1");
	  }
	  else
	  {
		  termWriteLine("Motor L fault: 0");
	  }
	  result = EC_SUCCESS;
  }
  else if (strcmp(cmd, "status") == 0)	// returns state of the motor values
  {
//	  int16_t motorRPercent = (motorValueRight * 100) / MOTOR_MAX_VALUE;	// convert the motor value R into percent
//	  int16_t motorLPercent = (motorValueLeft * 100) / MOTOR_MAX_VALUE;		// convert the motor value L into percent
//	  char strRPercent[5];
//	  char strLPercent[5];
//	  utilNum16sToStr(strRPercent, sizeof(strRPercent), motorRPercent);
//	  utilNum16sToStr(strLPercent, sizeof(strLPercent), motorLPercent);
	  termWriteLine("motor status:");
	  termWrite("ValueR: ");
//	  termWriteNum16s(motorRPercent);	// output in percent
	  termWriteNum16s(motorValueRight);
	  termWriteLine("");
	  termWrite("ValueL: ");
//	  termWriteNum16s(motorLPercent);		// output in percent
	  termWriteNum16s(motorValueLeft);
	  termWriteLine("");
	  termWrite("ValueW: ");
		termWriteNum16s(motorValueWinch);
		termWriteLine("");
	  result = EC_SUCCESS;
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
bool motorGetFLT(char side)
{
	if(side == 'R')
	{
		return !(MOTOR_R_FLT_PDIR & (uint32_t)(1 << MOTOR_R_FLT_PIN));	// return motor R fault pin value (invert fault pin because it is low-active)
	}
	else if(side == 'L')
	{
		return !(MOTOR_L_FLT_PDIR & (uint32_t)(1 << MOTOR_L_FLT_PIN));	// return motor L fault pin value (invert fault pin because it is low-active)
	}
	else { return false; }	// error: invalid argument
}

/**
 * Sets the GPIO PDOR value of the motor driver board DIR Pin
 *
 * @param[in] side
 *   side of the motor: R or L or W
 *
 * @param[in] value
 * 	 value to set the pin to
 */
void motorSetDIR(char side, bool value)
{
	if(side == 'R')	// set motor R direction pin
	{
		if(value) { MOTOR_R_DIR_PDOR |= (uint32_t)(1 << MOTOR_R_DIR_PIN); }	// forward DIR: 1
		else { MOTOR_R_DIR_PDOR &= ~(uint32_t)(1 << MOTOR_R_DIR_PIN); }			// backward DIR: 0
	}
	else if(side == 'L')	// set motor L direction pin
	{
		if(value) { MOTOR_L_DIR_PDOR &= ~(uint32_t)(1 << MOTOR_L_DIR_PIN); }	// forward DIR: 0
		else { MOTOR_L_DIR_PDOR |= (uint32_t)(1 << MOTOR_L_DIR_PIN); }				// backward DIR: 1
	}
	else if(side == 'W')	// set motor winch direction pin
	{
		if(value) { MOTOR_W_DIR_PDOR |= (uint32_t)(1 << MOTOR_W_DIR_PIN); }	// forward DIR: 1
		else { MOTOR_W_DIR_PDOR &= ~(uint32_t)(1 << MOTOR_W_DIR_PIN); }			// backward DIR: 0
	}
	else { }	// error: invalid argument
}

/**
 * Activates or deactivates the motor driver
 * Sets the GPIO PDOR value of the motor driver board SLP Pin
 * The winch motor driver has no SLP Pin. So just the PWM is set to 0.
 *
 * @param[in] side
 *   side of the motor: R or L or W
 *
 * @param[in] value
 * 	 value to set the pin to
 */
void motorSetSLP(char side, bool value)
{
	if(side == 'R')
	{
		if(value) { MOTOR_R_SLP_PDOR |= (uint32_t)(1 << MOTOR_R_SLP_PIN); }	// set motor R sleep pin
		else
		{
			MOTOR_R_SLP_PDOR &= ~(uint32_t)(1 << MOTOR_R_SLP_PIN); 			// clear motor sleep pin
			motorSetPwmRight(0);											// disable PWM
		}
	}
	else if(side == 'L')
	{
		if(value) { MOTOR_L_SLP_PDOR |= (uint32_t)(1 << MOTOR_L_SLP_PIN); }	// set motor L sleep pin
		else
		{
			MOTOR_L_SLP_PDOR &= ~(uint32_t)(1 << MOTOR_L_SLP_PIN); 			// clear motor sleep pin
			motorSetPwmLeft(0);												// disable PWM
		}
	}
	else if(side == 'W')
	{
		motorSetPwmWinch(0);												// disable PWM
	}
	else { }	// error: invalid argument
}

/**
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

	GPIOD->PDDR |= 1<<0 | 1<<1 | 1<<2 | 1<<3;			// configure PTD0 & PTD1 & PTD2 (PWM) as output and PTD3 as output (GPIO)
	GPIOC->PDDR |= 1<<8 | 1<<9 | 1<<10 | 1<<11;		// configure PTC8, PTC9, PTC10 & PTC11 as output

	// PORT as GPIO with pull-up (FLT)
	PORTB->PCR[2] = PORT_PCR_MUX(1) | PORT_PCR_PE(1) | PORT_PCR_PS(1);	// PTB2 as GPIO with pull-up
	PORTB->PCR[3] = PORT_PCR_MUX(1) | PORT_PCR_PE(1) | PORT_PCR_PS(1);	// PTB3 as GPIO with pull-up

	// PORTC as GPIO
	PORTC->PCR[8] = PORT_PCR_MUX(1);
	PORTC->PCR[9] = PORT_PCR_MUX(1);
	PORTC->PCR[10] = PORT_PCR_MUX(1);
	PORTC->PCR[11] = PORT_PCR_MUX(1);

	// PORTD as GPIO
	PORTD->PCR[3] = PORT_PCR_MUX(1);

	// Motor Sleep Pin (high to disable motor)
	motorSetSLP('R', false);
	motorSetSLP('L', false);
	motorSetSLP('W', false);

	// Motor Direction Pin (low: current from A to B)
	motorSetDIR('R', false);
	motorSetDIR('L', false);
	motorSetDIR('W', false);

	// GPIO Clear Bits on PTD0 & PTD1 & PTD2
	GPIOD->PCOR |= 1<<0 | 1<<1 | 1<<2;

	// configures the pin muxing of the 2 pins as GPIO-Pin.
	// the output level will be '0' (break operation) because of the configuration above.
	MOTOR_RIGHT_GPIO();
	MOTOR_LEFT_GPIO();
	MOTOR_WINCH_GPIO();

	// set PWM value to 0
	FTM3->CONTROLS[0].CnV = 0;
	FTM3->CONTROLS[1].CnV = 0;
	FTM3->CONTROLS[2].CnV = 0;

	// configure all three channels as edge aligned PWM with high-true pulses
	FTM3->CONTROLS[0].CnSC = FTM_CnSC_MSx(2) | FTM_CnSC_ELSx(2);
	FTM3->CONTROLS[1].CnSC = FTM_CnSC_MSx(2) | FTM_CnSC_ELSx(2);
	FTM3->CONTROLS[2].CnSC = FTM_CnSC_MSx(2) | FTM_CnSC_ELSx(2);

  // register terminal command line handler
  termRegisterCommandLineHandler(&clh, "mot", "(motor)", motorParseCommand);
}
