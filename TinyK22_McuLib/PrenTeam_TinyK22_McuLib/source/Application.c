/*
 * Application.c
 *
 *  Created on: 04.12.2020
 *      Author: Noxrem
 */

#include "Application.h"
#include "LEDpin1.h"
#include "McuWait.h"

void APP_RUN()
{
	McuGPIO_Handle_t BlueLed;

	McuGPIO_HwPin_t HwPin;
	HwPin.gpio

	while(1)
	{
		LEDpin1_PutVal(true);
		McuWait_Waitms(300);
		LEDpin1_PutVal(false);
		McuWait_Waitms(300);
	}

}
