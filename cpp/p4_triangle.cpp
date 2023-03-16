#include<iostream>
#include<cmath>
using namespace std;
class triangle
{
private:
	int a,b,c;
	float ar;
	bool val=0;
public:
	void read()
	{
	cout<<"Enter side 1 :";
	cin>>a;
	cout<<"Enter side 2 :";
	cin>>b;
	cout<<"Enter side 3 :";
	cin>>c;
	}
	void valid()
	{
	if ((a+b)>c && (a+c)>b && (b+c)>a)
	{
	cout<<"valid";
	val=1;
	}
	else 
	{
	cout<<"The current values are invalid. Please enter correct values"<<endl;
	read();
	}
	}
	void area()
	{
	if (val==1);
	{
		int s=0;
		s=(a+b+c)/2;
		ar= sqrt((s-a)*(s-b)*(s-c)*s);
		cout<<"The area of the triangle is :"<<ar<<endl;
	}
	}
};
int main()
{
triangle x;
x.read();
x.valid();
x.area();
return 0;
}
