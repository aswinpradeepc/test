#include<iostream>
using namespace std;
int n=0;
struct phone{int ph,ar,ex;};
phone x[100];
void read()
{
	cout<<"the number of phone numbers to be stored :";
	cin>>n;
}
void readin()
	{

		int i=0;
		for ( i; i<n; i++)
	{
		cout<<"Enter the phone number :";
		cin>>x[i].ph;
		cout<<"Enter the area number :";
		cin>>x[i].ar;
		cout<<"Enter the exno :";
		cin>>x[i].ex;
		cout<<endl;
	}
	}
void display()
{
	int i=0;
	for (i;i<n;i++)
	{
		cout<<x[i].ph<<"-"<<x[i].ar<<"-"<<x[i].ex<<endl;
	}
}
int main()
{
	read();
	readin();
	cout<<"The entered phone numbers are"<<endl;
	display();
	return 0;
}
