/*****************************************************************
*   Task:   Find whether the first string is a substring of the second
    Author: M. Zubair Asif
*****************************************************************/

#include<stdio.h>
#include <stdlib.h>

//  function declaration
void con(char * string);
int tester(int value1, int value2, int counter, char *s1, char *s2);
//  void function description
void con(char *string){
    // Looping through to test validity
    for(int i=0;string[i];i++){
    if (string[i]>='0'&&string[i]<='9'){
    printf("Invalid character entered\n");
    exit(0);
}
}
}

int tester(int value1, int value2, int counter, char *s1, char *s2){
    for(int i=0;i<=value1-value2;i++){
        for(int j=i;j<i+value2;j++){
            counter=1;
            if(s1[j]!=s2[j-i]){
                counter=0;
                break;
            }
        }
        if (counter==1)
            return 1;
}
}
//  main function description
int main()
{
    //  array & variable declaration
    char string1[100], string2[100];
    int value1 = 0, value2 = 0, i, counter;
    //  getting the first string
    printf("Enter the first string:\n");
    scanf("%s", &string1);
    // testing the string using the con void function
    con(string1);
    printf("Enter the second string:\n");
    // getting the second string
    scanf("%s", &string2);
    con(string2);
    while (string1[value1]!='\0')
        value1++;
    while (string2[value2]!='\0')
        value2++;

    if (tester(value1, value2, counter, string1, string2)==1)
        printf("the string '%s' is contained in the string '%s'\n", string2, string1);
    else
        printf("the string '%s' is not contained in the string '%s'\n", string2, string1);

    return 0;
}
