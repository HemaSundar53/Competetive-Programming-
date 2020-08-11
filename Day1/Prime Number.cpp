#include<iostream>
using namespace std;

int main()
{
    int n,temp=-1;
    cin>>n;
    for(int i=2;i<n;i++){
        if(n%i==0){
            temp=0;
            break;
        }
    }
    if(temp==0||n==1)
        cout<<n<<" is not a prime number";
    else
        cout<<n<<" is a prime number";
    
    return 0;
}
