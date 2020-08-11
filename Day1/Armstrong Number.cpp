#include<iostream>
using namespace std;
#include<math.h>

int main()
{
    int n,d=0,sum=0;
    cin>>n;
    int num = n;
    while(num!=0){
        d++;
        num/=10;
    }
    num=n;
    while(num!=0){
        sum += pow((num%10),d);
        num/=10;
    }
    if(n==sum)
        cout<<"Armstrong";
    else
        cout<<"Not Armstrong";

}
