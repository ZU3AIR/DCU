/*****************************************************************
*   Task:   Change the case of a string
    Author: M. Zubair Asif
*****************************************************************/
#include<stdio.h>
#include <stdlib.h>
#include <ctype.h>


void tester(char *string);
void tester(char *string)
{
    for (int i=0; string[i]; i++)
    {
        if(isalpha(string[i])==0){
            printf("Invalid character entered.\n");
            exit(0);
        }
    }

}
int main() 
{
  char string[100];
  printf("Enter a string of upper and lower case letters\n");
  scanf("%s", string);
  tester(string);
  for (int i=0; string[i]; i++)
    if (string[i] >= 'A' && string[i] <= 'Z')
      string[i] = string[i] + 32;
    else if (string[i] >= 'a' && string[i] <= 'z')
      string[i] = string[i] - 32;
  printf("%s\n", string);
}
