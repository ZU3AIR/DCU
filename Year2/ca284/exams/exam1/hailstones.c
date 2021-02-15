/*****************************************************************************************
Task	:	Prints the hailstone sequence from the input given until the sequence reaches 1
******************************************************************************************/
#include<stdio.h>
#include<stdlib.h>

//Create the function
int hailstone(int input);

//Edit the function
int hailstone(int input)
{
	if(input%2==0)//test if even
	{
		input=input/2;//hailstone if even
		return input;
	}
	else
	{
		input=(input*3)+1;//hailstone if odd
		return input;
	}
}
//Main\Default function
int main(int argc, char* argv[])// reading from command line
{
	int number;//variable declaration 
	number = atoi(argv[1]);//data type conversion
	while(1<number)
	{
		number = hailstone(number);//testing the number
		printf("%d\n", number);
	}
	return 0;
}
