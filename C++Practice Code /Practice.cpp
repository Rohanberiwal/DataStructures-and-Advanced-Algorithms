#include <iostream>
using namespace std ;
int main()
{
    cout<<"\nhello world " ; 
    cout<<"\n this is the next line " ;
    return 0 ;
    
}
#include <iostream>
// endl escape  sequence 
using namespace std ;
int main()
{
    cout<<"\nhello world " ; 
    cout<<endl ;
    cout<<"\n this is the next line " ;
    return 0 ;
    
}


#include <iostream>
// endl escape  sequence in the single line 
using namespace std ;
int main()
{
    cout<<"\nhello world " <<endl  ;
    cout<<"\n this is the next line " ;
    return 0 ;
    
}

#include <iostream>
// endl escape  sequence in the single line 
using namespace std ;
int main()
{
   int x  = 10; // initlisation of the variable 
   cout<<"the number is "<<x  ;
   return 0 ;
}

#include <iostream>
// endl escape  sequence in the single line 
using namespace std ;
int main()
{
   int x  = 10; // initlisation of the variable 
   float y  = 100.87 ;
   cout<<"the number is "<<x  ;
   cout<< endl ;
   cout<< "the number y is "<<y ;
   return 0 ;
}

#include <iostream>
// endl escape  sequence in the single line 
using namespace std ;
int main()
{
   int x  = 10; // initlisation of the variable 
   float y  = 100.87 ;
   cout<<"computation " <<x*y ;
   cout <<endl ;
   return 0 ;
}

// conditionals 
#include <iostream>
using namespace std  ;
int main()
{
    int x = 10 ;
    if(x==10)
    {
        cout<<"True the number is " <<x ;
        
    }
    else 
    {
     cout<<"the number is not " <<x ;
    }
    return 0 ;
}

// conditonals wiht the boolean operators 
#include <iostream>
#include <climits> 
using namespace std  ;
int main()
{
   int x  = INT_MAX ;
   bool check  = true  ;
   if(x> 0)
   {
       check  = false ;
   }
   cout<<"check is "<<check ;
}
