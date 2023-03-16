#iclude<iostream>
using namespace std;

class base
{
public:
    void show()
    {
        cout<<"show fn in base"<<endl;
    }
    virtual void display()
    {
        cout<<"display fn in base "<<endl;
    }
};
class child: public base
{
public:
    void show()
    {
        cout<<"show fn in child"<<endl;
    }
    void display()
    {
        cout<<"display fn in child "<<endl;
    }
};
int main()
{
    base p;
    child c;
    cout<<"a pointer of type base class is created <parent *bptr;>"<<endl;
    base *bptr;
    bptr = &p;
    cout<<"bptr points to base class obj"<<endl;
    bptr ->show();
    bptr ->display();
    cout<<"bptr points to child class object"<<endl<<"show() is not a virtual function while, display() is declared virtual in base class"<<endl;
    bptr=&c;
    bptr->show();
    bptr ->display();
    return 0;
}
