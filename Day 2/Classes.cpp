#include<iostream>
using namespace std;

class Friend{
    public:
        string name;
        int age;
        Friend(string Name,int Age)
        {
            cout<<"Constructor called "<<age<<endl;
            name = Name;
            age = Age;
        }
        ~Friend()
        {
            cout<<"Destructor called "<<age<<endl;
        }
        void get()
        {
            cout<<name<<"\t";
            cout<<age<<endl;
        }
        void set_(string newname,int newage)
        {
            name = newname;
            age = newage;
        }
};
int main()
{
    Friend f1("abc",10);
    Friend f2("xyz",20);
    f1.get();
    f1.set_("pqr",15);
    f1.get();
    f2.get();
}
