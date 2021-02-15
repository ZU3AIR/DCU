/************************************************************************************************************************
Task	:	Accepts number from command line only upto 8 digits. Digit can only be a number 0 or 1. Your task is to 
			convert the binary 
***********************************************************************************/
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int binconverter(char *binaryvalue);
void tester(char *binaryvalue);

int binconverter(char *binaryvalue){
    int value=0, int position=0;
    int l=strlen(binaryvalue);
    for (int i=l-1;i>=0;--i){
        if(binaryvalue[i]=='1'){
            value+=pow(2, position);
        }
        position+=1;
    }
    return value;
}

void tester(char *binaryvalue){
    int l = strlen(binaryvalue);

    if(8<l){

            	printf("Too many binary digits entered.\n");
            	exit(0);

    }
    for (int i=0;i<l;++i){
        if (binaryvalue[i] !='0'&&binaryvalue[i]!='1'){
                	printf("Only digits 1 and 0 are permitted.\n");
                	exit(0);

        }
    }
}

int main(int argc, char *argv[]){
    int z, a;
    char binaryvalue[500]={'\0'};
    for(int i=1;i<argc;++i){
        strcat(binaryvalue, argv[i]);
    }
	tester(binaryvalue);
	int result=binconverter(binaryvalue);
printf("%i\n", result);

return 0;
}
