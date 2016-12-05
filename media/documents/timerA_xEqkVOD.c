#include "timerA.h"
#include "LED.h"
#include "spi.h"
#include "ArrayValues.h"
#include <intrinsics.h>
#include <stdint.h>

extern int toggleWhich;
int count224 = 0;
int count32 = 0;

void ConfigureTimerA(void) {

	//TACTL |= MC_0;

	TACTL |= (TASSEL_2 | ID_0 | MC_1 | TACLR); //Setting Up the Timer, SMCLK, Divided by 8, in Up Mode, Interupt Endabled and Cleared Timer
	TACCR0 = 736;
	TACCTL0 |= CCIE;


}

#pragma vector = TIMER0_A0_VECTOR
// Timer a interrupt service routine, add code here for IN LAB
__interrupt void TimerA0_routine(void) {


	P1OUT &= ~BIT3;		 //CS/LD Pin 7
	SPISendByte(0x20);
	SPISendByte(array100[count224] >> 8);
	SPISendByte(array100[count224]);
	P1OUT |= BIT3;

	P1OUT &= ~BIT3;		 //CS/LD Pin 7
	SPISendByte(0x21);
	SPISendByte(array300[count224] >> 8);
	SPISendByte(array300[count224]);
	P1OUT |= BIT3;

	P1OUT &= ~BIT3;		 //CS/LD Pin 7
	SPISendByte(0x22);
	SPISendByte(array500[count224] >> 8);
	SPISendByte(array500[count224]);
	P1OUT |= BIT3;

	P1OUT &= ~BIT3;		 //CS/LD Pin 7
	SPISendByte(0x23);
	SPISendByte(array700[count32] >> 8);
	SPISendByte(array700[count32]);
	P1OUT |= BIT3;

	count224++;
	count32++;
	if(count224 == 224){
		count224 = 0;
	}
	if(count32 == 32){
		count32 = 0;
	}



	}

