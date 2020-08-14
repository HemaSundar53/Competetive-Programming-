#include<iostream>
using namespace std;

class Area
{
    public:
        Area(float R)
        {
            cout<<(22*R*R/7)<<endl;
        }
        Area(float l, float b)
        {
            cout<<l*b<<endl;
        }
};
int main()
{
    Area circle(7.0);
    Area Rectangle(3.1,5.0);
}
