#include <util/delay.h>
#include "std_types.h"
#include "BIT_MATH.h"

#include "DIO_int.h"

#include "LED_int.h"
int main(void)

{
  
      LED_voidInitBit(PORTA,PIN0);
	 
	while(1)
	{
		 LED_voidOnOff(PORTA,PIN0,BIN_HIGH);
		 _delay_ms(5000);
         LED_voidOnOff(PORTA,PIN0,BIN_LOW);
		 _delay_ms(5000);

	}
}
