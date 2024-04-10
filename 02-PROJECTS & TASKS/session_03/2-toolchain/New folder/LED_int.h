#include "std_types.h"
#ifndef LED_INT_H_
#define LED_INT_H_

void LED_voidInitBit(u8 Copy_u8Port,u8 Copy_u8Pin);

void LED_voidInitReg(u8 Copy_u8Port);

void LED_voidOnOff(u8 Copy_u8Port,u8 Copy_u8Pin,u8 Copy_u8StatePin);
void LED_voidOnOFFReg(u8 Copy_u8Port,u8 Copy_u8PortValu);
void Toogle_voidLED(u8 Copy_u8Port,u8 Copy_u8Pin);

#endif /* LED_INT_H_ */
