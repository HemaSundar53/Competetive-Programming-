#include<iostream>
using namespace std;

int main()
{
    int a=0,b=1,n,c;
    cin>>n;
    cout<<a<<endl<<b<<endl;
    for(int i=0;i<n-2;i++){
        c=a+b;
        cout<<(a+b)<<endl;
        a=b;
        b=c;
    }
}
