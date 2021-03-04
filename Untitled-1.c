#include<stdio.h>
int main()
{
/*    int i;
    for(i=1;1<=9;i++)
    if (i%3==0)
    printf("%d\n",i);
    system("pause")
    */
   double students[4][6];
   double grade;
   int i,j;
   for ( i = 0; i <= 4; i++)
   {
        for ( j = 0; j <= 6; j++)
        {
         scanf('%f',&grade);
         if (grade < 0)  {printf("no!");j-=1;}
         else students[i][j] = grade; 
        }  
   }
   printf(students);
return 0;
}
