// pre-order traversal
#include <stdio.h>
#include<stdlib.h>
#include<malloc.h>
struct node 
{
int data ;
struct node *left ;
struct node *right ;
} ;
typedef struct node node ;
node *root = NULL;

node *create(node *root)
{
  int data ;
  printf("enter data : ");
  scanf("%d",&data) ;
  if(data==-1)
  {
    return NULL ;
  }
  node *r = (node*)malloc(sizeof(node)) ;
  root = r ;
  root->left = NULL ;
  root ->right = NULL ;
  root->data = data ;
  root->left = create(root->left);
  root->right = create(root->right);
  return root ;
  
  
}
void preorder(struct node *root)
{
   if(root==NULL)
   {
      return;
   }
   printf("%d ",root->data); //root node
   preorder(root->left); //left
   preorder(root->right); //rigth


}
int main()
{
  node *root = NULL ;
  root = create(root) ;
  preorder(root);
}

// code for inorder traversal 
#include <malloc.h>
#include <stdio.h>
#include <stdlib.h>
struct node {
  int data;
  struct node *left;
  struct node *right;
};
typedef struct node node;
node *root = NULL;
node *create(node *root) {
  int data;
  printf("enter data : ");
  scanf("%d", &data);
  if (data == -1) {
    return NULL;
  }
  node *r = (node *)malloc(sizeof(node));
  r->data = data;
  r->left = NULL;
  r->right = NULL;
  root = r;
  root->left = create(root->left);
  root->right = create(root->right);
  return root;
}
int inorder(node *root) {
  if (root == NULL) {
    return NULL;
  }
  inorder(root->left);
  printf("%d ", root->data);
  inorder(root->right);
}
int main() {
  node *root = NULL;
  root = create(root);
  inorder(root);
  
}

// code for Postorder traversal in a binary tree 
#include <malloc.h>
#include <stdio.h>
#include <stdlib.h>
struct node {
  int data;
  struct node *left;
  struct node *right;
};
typedef struct node node;
node *root = NULL;
node *create(node *root) {
  int data;
  printf("enter data : ");
  scanf("%d", &data);
  if (data == -1) {
    return NULL;
  }
  node *r = (node *)malloc(sizeof(node));
  r->data = data;
  r->left = NULL;
  r->right = NULL;
  root = r;
  root->left = create(root->left);
  root->right = create(root->right);
  return root;
}
int postorder(node *root) {
  if (root == NULL) {
    return NULL;
  }
  postorder(root->left);
  postorder(root->right);
  printf("%d ", root->data);
}
int main() {
  node *root = NULL;
  root = create(root);
  postorder(root); 
  
}


// GEEKS FOR GEEKS Q-1)
// code for calcualtion of height of the binary tree ;
// error ! not able toi see the "n" == arry[i] part 

#include <stdio.h>
#include<stdlib.h>
#include<malloc.h>
struct node
{
int data ;
struct node *left  ;
struct node *right ;

} ;
typedef struct node node  ;
node *root = NULL ;
int main()
{
  int len ;
  printf("length of the binary tree : ");
  scanf("%d",&len) ;
  char arry[len]  ;
  for(int i = 0 ; i<len ; i++)
    {
      printf("enter string : ") ;
      scanf("%s",&arry[i]) ;
    }
  // testing ;
  printf("\nPREORDER TRAVERSAL :") ;
  // preorder - root , left , right
  for(int i = 0 ; i<len ; i++)
    {
      printf("%c",arry[i]) ;
    }
  int c = 0 ;
  for(int i = 0  ; i<len ; i++)
    {
      if(arry[i] == "n")
      {
        c = c+1 ;
      }
    }
  printf("\nthe length of the binary tree is %d ",c) ;
  
  return 0 ;
  
}
// code --2  (non coding question -->non programiing)
// no use 
#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
void createtree(int array[] , int g[] , int x )
{
  
}
int main(void)
{
  int x  ;
  printf("enter the pre - order length : ") ;
  scanf("%d",&x);
  int array[x] ;
  for(int i = 0  ; i<x  ; i++)
    {
      printf("enter data") ;
      scanf("%d",&array[i]) ;
    }
   for(int i = 0  ; i<x  ; i++)
    {
      printf("%d ",array[i]) ;
    }
  int g[x] ;
  for(int i = 0  ; i< x ; i++)
    {
      printf("\nenter level order data : ");
      scanf("%d",&g[i]) ;
      
    }
    for(int i = 0  ; i< x ; i++)
    {
      printf("%d ",g[i]);
      
    }
  createtree(array ,g , x) ;
  
}
