/*******************************************************
*	Binary.h			|
* -----------------------
* Binary is used to convert primitive data types to
* byte[]. A byte[] and insertion index must be provided.
*
* Do not use this class for JSON, XML, or similar
*	implementations
*
* Binary is not intended to be used directly, but through
* builder classes that interface with developers to
* easily construct structure for deserialization.
*******************************************************/
#pragma once

typedef unsigned char byte;	//Set this 'Data Type' to prevent confusion

/*****************************************************
* PrintBytes
*
*  This function will print out the bytes in the given
* Array with the given length.
*****************************************************/
void printBytes(const byte *bytes, const int length);

enum BinDataTypes
{
	BOOLEAN,
	CHAR,
	SHORT,
	INT,
	FLOAT,
	LONG,
	DOUBLE
};

/******************************************
* getNumBytes(datatype)
*
*	This function will return the number
* of bytes that the datatype will require
******************************************/
int getNumBytes(BinDataTypes dataType);

/*****************************************************************
* WriteBytes
* These functions will convert given data and insert it into 
* byte[] at pointer location.
* I.E. dest[pointer] = (converted to bytes) data
*
* These functions DO NOT ENSURE that there is enough room in the 
* array. Please ensure that the given array has enough length
* to insert data starting at the given index plus the length of data:
*
* char, unsigned char, bool = 1 byte
* short, unsigned short = 2 bytes
* int, unsigned int = 4 bytes
* long, unsigned long = 8 bytes
*****************************************************************/
int writeBytes(byte *dest, const int pointer, const unsigned char data);
int writeBytes(byte *dest, const int pointer, const unsigned short data);
int writeBytes(byte *dest, const int pointer, const unsigned int data);
int writeBytes(byte *dest, const int pointer, const unsigned long long data);
int writeBytes(byte *dest, const int pointer, const bool data);
int writeBytes(byte *dest, const int pointer, const char data);
int writeBytes(byte *dest, const int pointer, const short data);
int writeBytes(byte *dest, const int pointer, const int data);
int writeBytes(byte *dest, const int pointer, const long long data);



/*****************************************************************
* Read<INSERTDATATYPE>
* 
*	This function will read the bytes starting at the given pointer
* and return the selected datatype.
*
*	This function will NOT check to see if the bytes at the given
* is of the given datatype requested or if the data starts at the
* given location.
*
* char, unsigned char, bool = 1 byte
* short, unsigned short = 2 bytes
* int, unsigned int = 4 bytes
* long, unsigned long = 8 bytes
*****************************************************************/
unsigned char readUnsignedChar(byte *src, const int pointer);
unsigned short readUnsignedShort(byte *src, const int pointer);
unsigned int readUnsignedInt(byte *src, const int pointer);
unsigned long long readUnsignedLong(byte *src, const int pointer);
char readChar(byte *src, const int pointer);
short readShort(byte *src, const int pointer);
int readInt(byte *src, const int pointer);
long long readLong(byte *src, const int pointer);