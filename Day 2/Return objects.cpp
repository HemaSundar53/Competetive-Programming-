#include<iostream>
using namespace std;

class Cal
{
    public:
        float sum,diff,prod,div;
};

Cal Eval(float a,float b)
{
    Cal c;
    c.sum = a+b;
    c.diff = a-b;
    c.prod = a*b;
    c.div = a/b;
    return c;
}

int main()
{
    Cal ans;
    ans = Eval(11.0,5.5);
    cout<<ans.sum<<endl;
    cout<<ans.diff<<endl;
    cout<<ans.prod<<endl;
    cout<<ans.div<<endl;
}
