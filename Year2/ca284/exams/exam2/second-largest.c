#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include <limits.h>

#define MAX_SIZE 10

int main(int argc, char* argv[])
{
    int arr[MAX_SIZE], i;
    int max1, max2;
    int x;
    for(i=1;i<argc;i++)
    {
    	arr[i] = atoi(argv[i]);
    }

    max1 = max2 = INT_MIN;


    for(i=0; i<argc; i++)
    {
        if(arr[i] > max1)
        {
            max2 = max1;
            max1 = arr[i];
        }
        else if(arr[i] > max2 && arr[i] < max1)
        {
            max1 = arr[i];
        }
        else if(arr[i]<0){
        	x=1;
        }
    }

    if(x==1){
    	printf("Number must be bigger than 0");
    }
    if(argc<2)
    {
    	printf("Insufficant numbers given");
    }
    else{
    	printf("Second_largest: %d\n", max2);
    }

    return 0;
}