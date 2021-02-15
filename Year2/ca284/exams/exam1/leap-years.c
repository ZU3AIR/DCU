/*************************************************************************************************
Task	:	Prints all leap years from 1st command arg to 2nd, they should be printed one per line
**************************************************************************************************/
#include<stdio.h>
#include<stdlib.h>

//Creating a Function/Function Declaration
int year_tester(int y);

//Function Definition
int year_tester(int y)//tests whether leep yr or not
{
	if(y%4==0&&y%100!=0||y%400==0)
	{
		return y;
	}
	else
	{
		;
	}
}

int main(int argc, char* argv[])
{
	int year1, year2, i=0, diff, year, isleap;
	year1 = atoi(argv[1]);
	year2 = atoi(argv[2]);
	diff = year2-year1;
	while(i<=diff)
	{
		year = year1 + i;
		isleap = year_tester(year);
		if(isleap>year1)
		{
			printf("%d\n", isleap);
		}
		++i;
	}
	return 0;
}