#include <msp430.h>
#include "spi.h"
#include "timerA.h"
#include "LED.h"
/*
 * main.c
 */



void ConfigureClockModule(void)
{
    // Configure Digitally Controlled Oscillator (DCO) for 16 MHz using factory
    // calibrations.
	DCOCTL  = CALDCO_16MHZ;
	BCSCTL1 = CALBC1_16MHZ;
}


int main(void) {
    WDTCTL = WDTPW | WDTHOLD;	// Stop watchdog timer

    ConfigureClockModule();
    InitializeSPIPortPins();
    ConfigureTimerA();
    ConfigureSPI();
    _BIS_SR(GIE);
    while(1);


    return 0;

}


