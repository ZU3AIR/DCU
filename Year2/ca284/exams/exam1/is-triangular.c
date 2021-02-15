/****************************************************************************
Task	:	Determine whether input from command line is a triangular number
*****************************************************************************/
#include<stdio.h>
#include<stdlib.h>

int main(int argc, char* argv[])//	argc = counts amount of args & char* argv[] = stores args
{
	int number;//variable declaration
	number = atoi(argv[1]);//atoi is a converter from str to int
	switch(number)//alternative to if and else statements 
	{
		case 1 ://if number==1 or any other number underneath print...
		case 3 :
		case 6 :
		case 10 :
		case 15 :
		case 21 :
		case 28 :
		case 36 :
		case 45 :
		case 55 : printf("%d is a triangular number.\n", number);
					break;//stops it going into the next case
		default : printf("%d is not a triangular number.\n", number);//alternative else statement
					break;
	}
	return 0;//ends the code
}