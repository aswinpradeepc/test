#include<iostream>
#include<cmath>
using namespace std;
class shape
{
public:
    virtual float area()=0;
    virtual int perimeter()=0;
};
class triangle : public shape
{
private:
    int a,b,c,p;
    float ar;
public:
    int perimeter()
    {
        p = a+b+c;
        cout<<"The perimeter is :"<<p<<endl;
        return p;
    }
    float area()
    {
        int s = (a+b+c)/2;
        ar = sqrt(s*(s-a)*(s-b)*(s-c));
        cout<<"The area is :"<<ar<<endl;
        return ar;
    }
    triangle()
    {
        cout<<"Enter first side :";
        cin>>a;
        cout<<"Enter second side :";
        cin>>b;
        cout<<"Enter third side :";
        cin>>c;
    }
};
class rectangle : public shape
{
private:
    int a,b,p,ar;
    public:
    int perimeter()
    {
        p=2*(a+b);
        cout<<"The perimeter is :"<<p<<endl;
        return p;
    }
    float area()
    {
        ar=a*b;
        cout<<"The area is :"<<ar<<endl;
        return ar;
    }
    rectangle()
    {
        cout<<"Enter length :";
        cin>>a;
        cout<<"Enter Breadth :";
        cin>>b;
    }
};
class circle: public shape
{
private:
    int r,p;
    float ar;
public:
    int perimeter()
    {
        p=2*3.14*r;
        cout<<"The perimeter is :"<<p<<endl;
        return p;
    }
    float area()
    {
        ar=3.14*r*r;
        cout<<"The area is :"<<ar<<endl;
        return ar;
    }
    circle()
    {
        cout<<"Enter radius of circle :";
        cin>>r;
    }
};
class square : public shape
{
private:
    int a,p;
    float ar;
public:
    int perimeter()
    {
        p=4*a;
        cout<<"The perimeter is :"<<p<<endl;
        return p;
    }
    float area()
    {
        ar=a*a;
        cout<<"The area is :"<<ar<<endl;
        return ar;
    }
    square()
    {
        cout<<"Enter the sides of square :";
        cin>>a;
    }
};
int main()
{
    bool b=0;
    jump:
    cout<<"1. circle \n 2. triangle \n 3. square \n 4. rectangle \n Enter your choice :";
    int choice=0;
    cin>>choice;
    switch(choice) {
        case 1: {
            circle c;
            c.perimeter();
            c.area();
            break;
        }
        case 2: {
            triangle t;
            t.perimeter();
            t.area();
            break;
        }
        case 3: {
            square s;
            s.perimeter();
            s.area();
            break;
        }
        case 4: {
            rectangle r;
            r.perimeter();
            r.area();
            break;
        }
    }
    cout<<"Enter 0 to exit; 1 to continue :";
    cin>>b;
    if(b)
        goto jump;
    return 0;
}
