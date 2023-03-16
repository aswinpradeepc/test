#include<iostream>
using namespace std;
class arr
{
private:
	int ar[100];
	int n=0,av=1,sum=0,i=0;
	float avg;
public:
	void read()
	{
		cout<<"Enter the number of elements :";
		cin>>n;
		cout<<"Enter the array :";
		for (i=0; i<n;i++)
		{
		cin>>ar[i];
		}
		cout<<"The entered array is :";
		display();
	}
	void sigma()
	{
	for (i=0;i<n;i++)
		{
		sum=sum+ar[i];
		}
	avg=sum/n;
	cout<<"The average is :"<<avg<<endl;
	}
	
	void mul()
	{
	cout<<"Enter the number to multiply :";
	cin>>av;
	for(i=0;i<=n;i++)
	{
		ar[i]= ar[i]*av;
	}
	cout<<"The multiplied array is :";
	sum=0;
	display();
	sigma();
	}
	void display()
	{
	int q=0;
	for(i=0;i<n;i++)
	{
	cout<<ar[i]<<",";
	}
	cout<<endl;
	}
};
int main ()
{
arr a,b,c;
a.read();
a.sigma();
a.mul();
return 0;
}
