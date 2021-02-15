/************************************************************************************************************************
Task	:	Accepts number from command line only no. 1-9 are allowed, all numbers must be positive ints, ex 1234 is valid
            Count the number of odd, even & prime numbers in the sequence
*************************************************************************************************************************/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<stdbool.h>

/*Function Intialisation*/
int isprime(int n);
bool isOnlyNumbers(const char* str);

/*Function Description*/
int isprime(int n)
{
	int x, i, flag=0;//returns whether n is prime or not
	for(i=2;i<=n/2;++i)
		//non prime
	{
		if(n%i==0)
		{
			flag=1;
			break;
		}
	}
	if(n==1)
	{
		return 0;
	}
	else
	{
		if(flag==0){
			return 1;
	}
		else
		{
			return 0;
		}
	}

}

bool isOnlyNumbers(const char* str){
    int len = strlen(str);
    for(int i = 0; i < len; ++i)    
        if(!isdigit(str[i]))
            return false;    
    return true;

}
int main(int argc, char* argv[])
{
	int i, x, y, converted, converted2, oddnum=0, evennum=0, primenum=0;;//variable initialisation
    for(i=1;i<argc;++i)
    {
    	converted=atoi(argv[i]);
    		if(isprime(converted)==1)
    		{
    			++primenum;
    		}
    		if(converted%2==0)
    		{
    			++evennum;
    		}
    		if(converted % 2 != 0)
    		{
    			++oddnum;
    		}	
    }
    for(int j = 1; j < argc; ++j)
    {
        if(atoi(argv[j])<0)
            x = 1;
            
        else if(!isOnlyNumbers(argv[j]))        
            y = 1;        
    }

    if(argc<2)
    {
    	printf("insufficient command line arguments.\n");
    }
    if(x==1)
    {
    	printf("Error: Only positive integers are permitted.\n");
    }
    if(y==1)
    {
    	printf("Error: only numbers are permitted.\n");
    }
    if(x!=1 && y!=1 && argc>=2)
    {
    	printf("Number of odd numbers: %d\nNumber of even numbers: %d\nNumber of prime numbers: %d\n", oddnum, evennum, primenum);
    }
    return 0;
}
