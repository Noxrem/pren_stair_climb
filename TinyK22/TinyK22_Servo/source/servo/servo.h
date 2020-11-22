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
#define SERVO_PTA1_ENABLE			0	// not implemented
#define SERVO_PTA2_ENABLE			0	// not implemented
#define SERVO_PTA5_ENABLE			1

											// Values for TGY-50090M
#define SERVO_CnV_MAX				570		// Max. value of the FTM0 Channel equivalent to a PWM pulse width of 2ms (2ms / (1/fclk))
#define SERVO_CnV_MIN				140		// Min. value of the FTM0 Channel equivalent to a PWM pulse width of 1ms (1ms / (1/fclk))

void servoOutDegree(const char *servo, uint16_t value);
tError servoParseCommand(const char *cmd);
void servoInit(void);

#endif /* SERVO_SERVO_H_ */
