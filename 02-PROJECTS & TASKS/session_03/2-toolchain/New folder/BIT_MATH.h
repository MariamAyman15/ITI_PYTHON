#ifndef 	BIT_MATH_H
#define 	BIT_MATH_H


#define bitset(byte,nbit)   ((byte) |=  (1<<(nbit)))
#define bitclear(byte,nbit) ((byte) &= ~(1<<(nbit)))
#define bitflip(byte,nbit)  ((byte) ^=  (1<<(nbit)))
#define bitcheck(byte,nbit) ((byte) &   (1<<(nbit)))
#define GET_BIT(byte,b)   (((byte)>>(b))&(1))
#define equal_register(port,value)  ( port = value)

#endif
