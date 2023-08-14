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
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
struct node {
   int data;
   struct node *next;
};
struct node *head = NULL;
struct node *current = NULL;

void printList(){
   struct node *p = head;
   printf("\n[");
   while(p != NULL) {
      printf(" %d ",p->data);
      p = p->next;
   }
   printf("]");
}

void insertatbegin(int data){

   struct node *lk = (struct node*) malloc(sizeof(struct node));
   lk->data = data;
   lk->next = head;
   head = lk;
}
void insertatend(int data){
   struct node *lk = (struct node*) malloc(sizeof(struct node));
   lk->data = data;
   struct node *linkedlist = head;


   while(linkedlist->next != NULL)
      linkedlist = linkedlist->next;

   linkedlist->next = lk;
}
void insertafternode(struct node *list, int data){
   struct node *lk = (struct node*) malloc(sizeof(struct node));
   lk->data = data;
   lk->next = list->next;
   list->next = lk;
}
void deleteatbegin(){
   head = head->next;
}
void deleteatend(){
   struct node *linkedlist = head;
   while (linkedlist->next->next != NULL)
      linkedlist = linkedlist->next;
   linkedlist->next = NULL;
}
void deletenode(int key){
   struct node *temp = head, *prev;
   if (temp != NULL && temp->data == key) {
      head = temp->next;
      return;
   }
   while (temp != NULL && temp->data != key) {
      prev = temp;
      temp = temp->next;
   }

   if (temp == NULL) return;

   // Remove the node
   prev->next = temp->next;
}
int searchlist(int key){
   struct node *temp = head;
   while(temp != NULL) {
      if (temp->data == key) {
         return 1;
      }
      temp=temp->next;
   }
   return 0;
}
void main(){
   int k=0;
   insertatbegin(12);
   insertatbegin(22);
   insertatend(30);
   insertatend(44);
   insertatbegin(50);
   insertafternode(head->next->next, 33);
   printf("Linked List: ");
   printList();
   deleteatbegin();
   deleteatend();
   deletenode(12);
   printf("\nLinked List after deletion: ");

   printList();
   insertatbegin(4);
   insertatbegin(16);
   printf("\nUpdated Linked List: ");
   printList();
   k = searchlist(16);
   if (k == 1)
      printf("\nElement is found");
   else
      printf("\nElement is not present in the list");
}

// leetcode qwuestion climbing stair dynamic programming 
int climbStairs(int n){
   int* dp = calloc(n + 2, sizeof(int));
    dp[1] = 1;
    dp[2] = 2;
    
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    int result = dp[n];
    free(dp);

    return result;
}

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
struct node {
   int data;
   struct node *next;
};
struct node *head = NULL;
struct node *current = NULL;

void printList(){
   struct node *p = head;
   printf("\n[");
   while(p != NULL) {
      printf(" %d ",p->data);
      p = p->next;
   }
   printf("]");
}

void insertatbegin(int data){

   struct node *lk = (struct node*) malloc(sizeof(struct node));
   lk->data = data;
   lk->next = head;
   head = lk;
}
void insertatend(int data){
   struct node *lk = (struct node*) malloc(sizeof(struct node));
   lk->data = data;
   struct node *linkedlist = head;


   while(linkedlist->next != NULL)
      linkedlist = linkedlist->next;

   linkedlist->next = lk;
}
void insertafternode(struct node *list, int data){
   struct node *lk = (struct node*) malloc(sizeof(struct node));
   lk->data = data;
   lk->next = list->next;
   list->next = lk;
}
void deleteatbegin(){
   head = head->next;
}
void deleteatend(){
   struct node *linkedlist = head;
   while (linkedlist->next->next != NULL)
      linkedlist = linkedlist->next;
   linkedlist->next = NULL;
}
void deletenode(int key){
   struct node *temp = head, *prev;
   if (temp != NULL && temp->data == key) {
      head = temp->next;
      return;
   }
   while (temp != NULL && temp->data != key) {
      prev = temp;
      temp = temp->next;
   }

   if (temp == NULL) return;

   // Remove the node
   prev->next = temp->next;
}
int searchlist(int key){
   struct node *temp = head;
   while(temp != NULL) {
      if (temp->data == key) {
         return 1;
      }
      temp=temp->next;
   }
   return 0;
}
void main(){
   int k=0;
   insertatbegin(12);
   insertatbegin(22);
   insertatend(30);
   insertatend(44);
   insertatbegin(50);
   insertafternode(head->next->next, 33);
   printf("Linked List: ");
   printList();
   deleteatbegin();
   deleteatend();
   deletenode(12);
   printf("\nLinked List after deletion: ");

   printList();
   insertatbegin(4);
   insertatbegin(16);
   printf("\nUpdated Linked List: ");
   printList();
   k = searchlist(16);
   if (k == 1)
      printf("\nElement is found");
   else
      printf("\nElement is not present in the list");
}

// leetcode qwuestion climbing stair dynamic programming 
int climbStairs(int n){
   int* dp = calloc(n + 2, sizeof(int));
    dp[1] = 1;
    dp[2] = 2;
    
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    int result = dp[n];
    free(dp);

    return result;
}
// leetcode 74
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        boolean flag = false ;
        int m  = matrix.length ;
        int n = matrix[0].length ;
        for(int i = 0 ; i<m  ;i++)
        {
            for(int j = 0 ; j<n  ; j++)
            {
                if(matrix[i][j]==target)
                {
                    flag = true ;
                }
                
            }
        }
        return flag ;

    }
}
