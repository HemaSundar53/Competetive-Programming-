// https://www.geeksforgeeks.org/program-to-find-the-nth-prime-number/
#include<iostream>
using namespace std;

int prime(int n)
{
    for(int i=2;i<n;i++){
        if(n%i==0){
            return 0;
        }
    }
    return 1;
}
int main()
{
    int n;
    cin>>n;
    int i=2,count=0;
    while(1){
        if(prime(i)){
            count++;
            if(count==n)
            {
                cout<<i;
                break;
            }
        }
        i++;
    }
    return 0;
}
