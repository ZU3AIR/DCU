/************************************************************************************************************************
Task	:	Takes three numbers from command line and returns the largest of the three making sure there are no duplicates
*************************************************************************************************************************/
#include<stdio.h>
#include<stdlib.h>

//Create the Function/Function Declaration
int largest_of_three(int n1, int n2, int n3);//this is an int function

const char * identical_numbers(char n1, char n2, char n3);//this is a str function

const char * identical_numbers(char n1, char n2, char n3)//const char * allows return of string
{
	if(n1==n2||n2==n3||n3==n1)//if any two are equal...
	{
		return "error: two numbers entered are the same";
	}
	else
	{
		;
	}
}

int largest_of_three(int n1, int n2, int n3)//finds largest out of 3
{
	if(n1>n2&&n1>n3)
	{
		return n1;
	}
	else if(n2>n1&&n2>n3)
	{
		return n2;
	}
	else
	{
		return n3;
	}

}

int main(int argc, char* argv[])
{
	//Variable Declaration
	int num1, num2, num3;
	char comp;
	num1 = atoi(argv[1]);
	num2 = atoi(argv[2]);
	num3 = atoi(argv[3]);

	//final if statement in order to fix last printing error
	if(num1==num2||num2==num3||num3==num1)
	{
		printf("%s\n", identical_numbers(num1, num2, num3));
	}
	else
	{
		printf("%d is the largest number.\n", largest_of_three(num1, num2, num3));
	}
	return 0;

}