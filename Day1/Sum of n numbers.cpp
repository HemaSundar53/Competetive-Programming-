#include<iostream>
using namespace std;

int main()
{
    int n,sum=0,a;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>a;
        sum+=a;
    }
    cout<<sum;
}
