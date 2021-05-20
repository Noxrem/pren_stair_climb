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

#define SERVO_PTD4_ENABLE			1
#define SERVO_PTA1_ENABLE			0	// not implemented
#define SERVO_PTA2_ENABLE			0	// not implemented
#define SERVO_PTA5_ENABLE			1

// Servo degree values to be initialized with on startup [degree]
#define SERVO_PTD4_DEG_INIT			25		// ARM of the Gefyra (ARM in resting position, pointing to the back)
#define SERVO_PTA5_DEG_INIT			90		// Raspberry Pi CAM (centered setting)

											// Values for SG92R
#define SERVO_CnV_MAX				640		// Max. value of the FTM0 Channel equivalent to a PWM pulse width of 2ms (2ms / (1/fclk))
#define SERVO_CnV_MIN				140		// Min. value of the FTM0 Channel equivalent to a PWM pulse width of 1ms (1ms / (1/fclk))

void servoOutDegree(const char *servo, uint16_t value);
tError servoParseCommand(const char *cmd);
void servoInit(void);

#endif /* SERVO_SERVO_H_ */
