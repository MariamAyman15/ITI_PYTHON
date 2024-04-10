#include "DIO_int.h"
#include "LED_int.h"
#include "LED_prv.h"
#include "LED_cfg.h"

void LED_voidInitBit(u8 Copy_u8Port,u8 Copy_u8Pin)
{
	MDIO_voidSetPinDirection(Copy_u8Port,Copy_u8Pin,PIN_OUT);
}

void LED_voidInitReg(u8 Copy_u8Port)
{
	MDIO_voidSetPortDirection( Copy_u8Port,LED_PORTValu);
}

void LED_voidOnOff(u8 Copy_u8Port,u8 Copy_u8Pin,u8 Copy_u8StatePin)
{
	MDIO_voidSetPinValue(Copy_u8Port,Copy_u8Pin,Copy_u8StatePin);
}
void LED_voidOnOFFReg(u8 Copy_u8Port,u8 Copy_u8PortValu)
{
	MDIO_voidSetPortValue(Copy_u8Port,Copy_u8PortValu);
}
void Toogle_voidLED(u8 Copy_u8Port,u8 Copy_u8Pin)
{
	  MDIO_voidSetPinValue(Copy_u8Port,Copy_u8Pin,1 ^ MDIO_u8GETPinValue(Copy_u8Port,Copy_u8Pin));
}
