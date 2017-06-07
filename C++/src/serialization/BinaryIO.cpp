
#include "headers/BinaryIO.h"
#include <iostream>
#include <stdio.h>


#ifndef DEBUG
#define DEBUG false
#endif

#define BYTEMASK 0xFF
#define SHORTMASK 0xFFFF
#define INTMASK 0xFFFFFFFF
#define LONGMASK 0xFFFFFFFFFFFFFFFF

#define SBYTESHIFT 8
#define DBYTESHIFT 16
#define QBYTESHIFT	32


void printBytes(const byte *bytes, const int length) {
	for (int i = 0; i < length; ++i) {
		if (i != 0 && i % 8 == 0) { std::cout << " "; }	//This ensures that after the first 8 bytes there is a space for easier readability
		if (i != 0 && i % 16 == 0) { std::cout << "\n"; } //This will add a new line to prevent the line getting longer than the console.
		printf("0x%1X ", bytes[i]);	//Print the bytes out.
	}
	std::cout << "" << std::endl;
}

int getNumBytes(BinDataTypes dataType)
{
	switch (dataType)
	{
		case BOOLEAN:
		case CHAR:
			return 1;
		case SHORT:
			return 2;
		case INT:
		case FLOAT:
			return 4;
		case LONG:
		case DOUBLE:
			return 8;
	}
	return -1;
}

/**************************************************************
* This function handles actually putting a byte to the array.
**************************************************************/
int writeBytes(byte *dest, const int pointer, const unsigned char data)
{
	dest[pointer] = data;
	return pointer+1;
}

int writeBytes(byte *dest, const int pointer, const char data){	return writeBytes(dest, pointer, (unsigned char) data);}
int writeBytes(byte *dest, const int pointer, const signed char data){ return writeBytes(dest, pointer, (unsigned char) data);}
int writeBytes(byte *dest, const int pointer, const bool data) { return writeBytes(dest, pointer, (char)(data & BYTEMASK)); }
int writeBytes(byte *dest, const int pointer, const short data){	return writeBytes(dest, writeBytes(dest, pointer, (char)(data & BYTEMASK)) , (char)((data >> SBYTESHIFT) & BYTEMASK));}
int writeBytes(byte *dest, const int pointer, const unsigned short data){ return writeBytes(dest, pointer, (short) data);}
int writeBytes(byte *dest, const int pointer, const int data){ return writeBytes(dest, writeBytes(dest, pointer, (short)(data & SHORTMASK)), (short)((data >> DBYTESHIFT) & SHORTMASK));}
int writeBytes(byte *dest, const int pointer, const unsigned int data){ return writeBytes(dest, pointer, (int)data);}
int writeBytes(byte *dest, const int pointer, const long long data){	return writeBytes(dest, writeBytes(dest, pointer, (int)(data & INTMASK)), (int)((data >> QBYTESHIFT) & INTMASK));}
int writeBytes(byte *dest, const int pointer, const unsigned long long data){ return writeBytes(dest, pointer, (long long)data);}


unsigned char readUnsignedChar(byte *src, const int pointer){return (unsigned char)(src[pointer] & BYTEMASK);}
unsigned short readUnsignedShort(byte *src, const int pointer) { return (unsigned short)(((unsigned short)readUnsignedChar(src, pointer) | (unsigned short)readUnsignedChar(src, pointer + 1) << SBYTESHIFT) & SHORTMASK); }
unsigned int readUnsignedInt(byte *src, const int pointer) { return (unsigned int)(((unsigned int)readUnsignedShort(src, pointer) | (unsigned int)readUnsignedShort(src, pointer + 2) << DBYTESHIFT) & INTMASK); }
unsigned long long readUnsignedLong(byte *src, const int pointer) { return (unsigned long long)(((unsigned long long)readUnsignedInt(src, pointer) | (unsigned long long)readUnsignedInt(src, pointer + 4) << QBYTESHIFT) & LONGMASK); }
char readChar(byte *src, const int pointer){ return (char)(readUnsignedChar(src, pointer)); }
short readShort(byte *src, const int pointer){ return (short)readUnsignedShort(src, pointer); }
int readInt(byte *src, const int pointer){ return (int)readUnsignedInt(src, pointer); }
long long readLong(byte *src, const int pointer){ return (long long) readUnsignedLong(src, pointer); }
