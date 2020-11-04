/**
 *--------------------------------------------------------------------\n
 *          HSLU T&A Hochschule Luzern Technik+Architektur            \n
 *--------------------------------------------------------------------\n
 *
 * \brief         Exercise 12 - Line Sensor
 * \file
 * \author        Christian Jost, christian.jost@hslu.ch
 * \date          16.05.2020
 *
 *--------------------------------------------------------------------
 */
#include "platform.h"
#include "ftm0.h"
#include "ftm3.h"
#include "motor.h"
#include "quad.h"
#include "term.h"
#include "sound.h"
#include "soundPlayer.h"
#include "drive.h"
#include "pwrSwitch.h"
#include "i2c.h"
#include "led.h"
#include "color.h"
#include "adc.h"
#include "util.h"
#include "eeprom.h"

/**
 * Lets the blue Led on the TinyK22 blink in a specified amount of ms.
 *
 * @param[in]
 *   toggle the Led every "ms" milliseconds
 */
void BlinkBlueLedEveryMS(uint16_t timeMS)
{
  static uint16_t j;

  if (j++ == FTM3_TOFS_MS(timeMS)) 		// toogle blue led every timeMS milliseconds
  {
	  j=0;
      GPIOC->PTOR = (1<<2);
  }
}





/**
 * The main function of the MC-Car app.
 */
void main(void)
{
  ftm0Init();
  ftm3Init();
  termInit(57600);
  soundInit();
  soundPlayerInit();
  motorInit();
  quadInit();
  driveInit();
  pwrSwitchInit();
  EnableDebugLeds();
  ledInit();
  i2cInit();
  eepromInit();
  adcInit();

  soundBeep(4000, 100);

  // configure blue led on PTC2
  PORTC->PCR[2] = PORT_PCR_MUX(1);
  GPIOC->PDDR |= (1<<2);

  while(TRUE)
  {
    // check for commands from terminal
    termDoWork();


    // check for timer overflow
    if (FTM3->SC & FTM_SC_TOF_MASK)
    {
      FTM3->SC &= ~FTM_SC_TOF_MASK;    // clear TOF flag
      BlinkBlueLedEveryMS(100);
    }
  }
}
