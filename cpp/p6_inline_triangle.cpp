#include<iostream>
#include<cmath>
bool val=0;
using namespace std;
class triangle
{
	private:
		int x,y,p,q,r,s;
		float a,b,c,d;
	public:
		void distance()
		{
			a=sqrt(pow(x-p,2)+pow(y-q,2));
			b=sqrt(pow(x-r,2)+pow(y-s,2));
			c=sqrt(pow(r-p,2)+pow(s-q,2));
			cout<<"The length of the sides are :"<<endl;
			cout<<a<<endl<<b<<endl<<c<<endl;
		}
		void read()
		{
			cout<<"Enter the abcissa of point 1 :";
			cin>>x;
			cout<<"Enter the ordinate of point 1 :";
			cin>>y;
			cout<<"Enter the abcissa of point 2 :";
			cin>>p;
			cout<<"Enter the  of ordinate point 2 :";
			cin>>q;
			cout<<"Enter the abcissa of point 3 :";
			cin>>r;
			cout<<"Enter the ordinate of point 3 :";
			cin>>s;
			cout<<"The entered points are :"<<endl;
			cout<<"("<<x<<","<<y<<")"<<endl;
			cout<<"("<<p<<","<<q<<")"<<endl;
			cout<<"("<<r<<","<<s<<")"<<endl;
		}
		void valid()
		{
		if ((a+b)>c && (a+c)>b && (b+c)>a)
		{
		cout<<"valid"<<endl;
		val=1;
		}
		else 
		{
		cout<<"The current values are invalid. Please enter correct values"<<endl;
		read();
		distance();
		valid();
		}
		}
		void minm();	
};	
	
inline void triangle :: minm()
{
if (a<b&&a<c)
cout<<"The shortest side is :"<<a<<endl;
else if (b<a&&b<c)
cout<<"The shortest side is :"<<b<<endl;
else if (c<a&&c<b)
cout<<"The shortest side is :"<<c<<endl;
else
cout<<"The triangle has sides of same length"<<endl;
}
		
int main()
{
triangle g;
g.read();
g.distance();
g.valid();
g.minm();
return 0;
}

			
