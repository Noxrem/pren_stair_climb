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


// calulate nr of TOF count for a given number of milliseconds
#define TOFS_MS(x)   ((uint16_t)(((FTM3_CLOCK / 1000) * x) / (FTM3_MODULO + 1)))



void CheckAdc(void)
{
  static uint16_t j;

  if (j++ == TOFS_MS(250)) {            // toogle rear leds every 250ms
    j=0;
    if (adcGet16BitValue(18) > 65000)
    {
      GPIOA->PTOR = (1<<17);
      if (adcGetVoltage(18) > 1190000) GPIOA->PTOR = (1<<15);
    }
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

  // configure read red leds on PTA15 and PTA17
  PORTA->PCR[15] = PORTA->PCR[17] = PORT_PCR_MUX(1);
  GPIOA->PDDR |= (1<<15) | (1<<17);

  while(TRUE)
  {
    // check for commands from terminal
    termDoWork();


    // check for timer overflow
    if (FTM3->SC & FTM_SC_TOF_MASK)
    {
      FTM3->SC &= ~FTM_SC_TOF_MASK;    // clear TOF flag
      CheckAdc();
    }
  }
}
