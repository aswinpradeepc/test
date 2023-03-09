#include<iostream>
using namespace std;
class circle
{
private:
    int r;
    int x,y;
    float ar,cr;
public:
    circle()
    {
        r=10;
        x=0;
        y=0;
        ar = 3.14*10*10;
        cr = 2*3.14*10;
    }
    circle(int a,int b, int c)
    {
        r= a;
        x= b;
        y=c;
    }
    void area()
    {
        ar = 3.14*r*r;
        cout<<"area :"<<ar<<endl;
    }
    void crm()
    {
        cr = 2*3.14*r;
        cout<<"crm :"<<cr<<endl;
    }
    void show()
    {
        cout<<"radius :"<<r<<endl<<"(x,y) :("<<x<<","<<y<<")"<<endl;
    }
};
int main()
{
    circle q;
    q.show();
    circle c(4,0,0);
    c.show();
    c.area();
    c.crm();
}
