#include <iostream>
#include <cstdio>
#include "serialization/headers/StringIO.h"
#include <climits>

int main(int argc, char *argv[])
{
	
	unsigned char * bytes = new unsigned char [30];
	long long l = LLONG_MAX;
	int i = INT_MAX;
	short s = SHRT_MAX;
	char c = 'F';
	bool yo = false;

	//writeBytes(bytes, 0, l);
	//serialize(bytes, 2, sch);



	std::cout << l << std::endl;

	//printBytes(bytes, 30);
	//printf("%x %x %x %x %x %x %x %x\n", bytes[0], bytes[1], bytes[2], bytes[3], bytes[4], bytes[5], bytes[6], bytes[7]);

	long long yoyo = readFromString("4283");
	std::cout << yoyo << std::endl;

	std::cin.get();
	return 0;
}
