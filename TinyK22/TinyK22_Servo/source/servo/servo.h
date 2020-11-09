/**
 *--------------------------------------------------------------------\n
 *          HSLU T&A Hochschule Luzern Technik+Architektur            \n
 *--------------------------------------------------------------------\n
 *
 * \brief         servo driver for the TinyK22
 * \file
 * \author        Pascal Brülhart
 * \date          07.11.2020
 *
 *--------------------------------------------------------------------
 */

#ifndef SERVO_SERVO_H_
#define SERVO_SERVO_H_

#define SERVO_PTA4_ENABLE			1
// TODO implement alternative Servo motors on other pins
#define SERVO_PTA1_ENABLE			0	// not implemented
#define SERVO_PTA2_ENABLE			0	// not implemented
#define SERVO_PTA5_ENABLE			0	// not implemented

#define SERVO_CnV_MAX				500		// Max. value of the FTM0 Channel equivalent to a PWM pulse width of 2ms (2ms / (1/fclk))
#define SERVO_CnV_MIN				250		// Min. value of the FTM0 Channel equivalent to a PWM pulse width of 1ms (1ms / (1/fclk))

tError servoParseCommand(const char *cmd);
void servoInit(void);

#endif /* SERVO_SERVO_H_ */
