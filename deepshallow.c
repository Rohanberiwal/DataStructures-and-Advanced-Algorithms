// code 4 deep and shallow copy 

#include <stdio.h>
#include <string.h>

void change(int ar[],int n)
{
  for(int i=0;i<n;i++)
    {
      ar[i]=ar[i]+5;
    }
}

int change2(int x,int y)
{
  x+=5;
  y+=5;
  printf("\n%d and %d",x,y);
  return 0;
}

int main(void) {

  int ar[]={10,20,30,40,50};
  
  change(ar,5); //call by reference 
  //changes in called function will be reflected back 
  //to calling function (main)

  printf("\nChanged Array\n");
  for(int i=0;i<5;i++)
    {
      printf("%d ",ar[i]);
    }

  int a=100,b=200;

  int x=change2(a,b); //call by value 

  //changes in called function will not be reflected back 
  //to calling function (main)

  printf("\nChanged Values are %d and %d",a,b);
  
  /*
  int x=10,y;
  y=x;

  x+=5;

  printf("X = %d",x);
  printf("\nY = %d",y);
  
  int x=10,*y;
  y=&x; //y is containing address of x(*y is pointing to value             of x)
  
  *y=*y+5;

  printf("X = %d",x);
  printf("\nY = %d",*y);

  x=x+10;

  printf("\nX = %d",x);
  printf("\nY = %d",*y);

  */
  
  return 0;
}

// malloc() function toi create a dynamic array 
#include <stdio.h>
int main()
{

  int *p;
int n,i,s=0;

  printf("Enter n");
  scanf("%d",&n);
  
  p=(int *)malloc(sizeof(int)*n);

  printf("Enter elements in array\n");
  for(int i=0;i<n;i++)
    {
    scanf("%d",&p[i]);
    }


  for(int i=0;i<n;i++)
    {
      s=s+p[i];
    }

  printf("Sum = %d",s);


  free(p);
       return 0 ;
    
    
}
//code for enumeration 

/*Enumeration (or enum) is a user
 defined data type in C. It is mainly 
 used to assign names to integral constants, 
 the names make a program easy to read and maintain.
 */
// code that is using emnum data type 
// user data type decleration ;

enum week{Mon, Tue, Wed, Thur, Fri, Sat, Sun};
 
int main()
{
    enum week day;
    day = Wed;
    printf("%d",day);
    return 0;
}


