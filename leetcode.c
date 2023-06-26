// code 1
#include <stdio.h>
int main()
{
    int n ;
    scanf("%d",&n) ;
    int nums[n] ;
    for(int i = 0 ; i<n ;i++)
    {
        printf("enter the  input ") ;
        scanf("%d", &nums[i]) ;
    }
    int target ;
    scanf("%d",&target) ;
    for(int i=0 ; i<n ; i++)
    {
        for(int j=i+1 ; j<n  ;j++)
        {
            int z  ;
            z = nums[i]+nums[j] ;
            if (z == target)
            {
                printf("[%d, %d]",i,j) ;

            }
        }

    }
    return 0 ;
}


// code 2 
// it does not work for 2 digit numbers
#include <stdio.h>
int main()
{
    int n ;
    printf("enter the number") ;
    scanf("%d",&n) ;
    int nums_1[n] ;
    int l  ;
    printf("\nenter the number") ;
    scanf("%d",&l) ;
    int nums_2[l] ;
    for(int i = 0 ; i<n ; i++)
    {
        printf("\nenter the inputs ") ;
        scanf("%d",&nums_1[i]) ;

    }
    for(int i = 0 ; i<n ; i++)
    {
        printf("\nenter the inputs for array 2 ") ;
        scanf("%d",&nums_2[i]) ;

    }
    for(int i = 0 ; i<n ; i++)
    {
        int sum ;
        sum  = nums_1[i] +nums_2[i] ;
        printf("\n%d",sum) ;
    }
    return 0 ;
}
// cdode 3
#include <stdio.h>
#include <string.h>
int main()
{
    int n , counter ;
    printf("enter the length of the array ") ;
    scanf("%d",&n);
    int m =n ;
    char array[n] ;
    printf("enter the input") ;
    scanf("%s",&array) ;
    printf("the input sting is %s",array ) ;
    for (int i = 0 ; i<n ; i++)
    {
        printf("%s",array[i]) ;
    }
  /*  for(int i= 0 ; i<n ; i++)
    {
        for(int j = i ; i<n ; j++)
        {
            if (array[i]== array[j])
            {
                counter = counter+1 ;
            }
        }
    }
    printf("%d",counter) ;*/
    return 0;
    
}

// code for weird algoritham 
#include <stdio.h>
#include <string.h>
int main()
{
    int n ;
    printf("enter the number") ;
    scanf("%d",&n) ;
    if (n%2==0)
    {
        int z ;
        z = n/2  ;
        printf("%d",z) ;
    }
    else 
    {
        int z ; 
        z = 3*n+1 ;
        printf("%d",z) ;
        
    }
    return 0 ;
}

// code 2 cses.py
#include <stdio.h>
#include <string.h>
int main()
{
    int n  ;
    printf("enter the size ");
    scanf("%d",&n) ;
    int array[n-1];
    for (int i =0 ; i<n ; i++)
    {
        printf("enter the numebr ") ;
        scanf("%d",&array[i]) ;
    }
    int array_2[n] ;
    for (int i = 0 ; i<n ; i++)
    {
        array[i] = i+1 ;
        printf("%d",i+1) ;
        
    }
    for (int i =0 ; i<n ; i++)
    {
        for (int j = n ; j>= 0 ;j--)
        {
            if (array[i]-array_2[j])
            {
                int z  ;
                
                z  =array[i] - array_2[j] ;
                
                printf("%d",z) ;
                break  ;
            }
        }
    }
    return 0 ;
    
}


// leet code question 3

#include <stdio.h>

int main()
{
    int n;
    long int sum=0;
    printf("How many numbers you want to add:");
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        long int num=0;
        printf("Enter Number %d here:",i);
        scanf("%ld",&num);
        sum+=num;
    }
    printf("The Sum is %ld",sum);
}