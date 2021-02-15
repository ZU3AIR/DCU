/************************************************************************************************************************
Task	:	Accepts number from command line only no. 1-9 are allowed, all numbers must be positive ints, ex 1234 is valid
            Count the number of odd, even & prime numbers in the sequence
*************************************************************************************************************************/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

char isdigittester(const char* word)
{
    int x = strlen(word);
    for(int z = 0; z < x; ++z)    
        if(!isdigit(word[z]))
            return 0;    
    return 1;
}
int primenumbertester(int number)
{
	int i, counter=0;
	for(i=1;i<=number;++i)
	{
		if(number%i==0)
		{
			counter++;
		}
	}
	if(counter==2)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

int main(int argc, char* argv[])
{
	int i, positive, nondigits, n;
	int prime=0, odd=0, even=0;
	for(i=1;i<argc;++i)
    {
    	n=atoi(argv[i]);
    		if(primenumbertester(n)==1)
    		{
    			++prime;
    		}
    		if(n%2==0)
    		{
    			++even;
    		}
    		if(n % 2 != 0)
    		{
    			++odd;
    		}	
    }
    int t;
    for(t=1;t<argc;++t)
    {
        if(atoi(argv[t])<0)
            positive = 1;
            
        else if(!isdigittester(argv[t]))        
            nondigits = 1;        
    }


    if(positive==1){
    	printf("Error: Only positive integers are permitted.\n");
    }
    if(nondigits==1){  	
    	printf("Error: only numbers are permitted.\n");
    }
   	if(argc<2){
    	printf("insufficient command line arguments.\n");
    }
   	else if(nondigits!=1&&positive!=1&&argc>=2){
    	printf("Number of odd numbers: %d\nNumber of even numbers: %d\nNumber of prime numbers: %d\n", odd, even, prime);
   	}
    return 0;
}
