#include<iostream>
#include<string>
using namespace std;
int i=0;
class bank 
{
private:
int acno;
float bal=0;
string name;

public:
void create()
{
	cout<<"Enter the name of account holder :";
	cin>>name;
	cout<<"Enter the initial deposit amount :";
	cin>>bal;
	cout<<"Your account number is :"<<i<<endl;
	i++;
}
int read()
{
	int a;
	cout<<"Enter the account number :";
	cin>>a;
	return a;
}
void details()
{
	i=read();
	cout<<"Your name is :"<<name<<endl;
	cout<<"Your balance is :"<<bal<<endl;
}
void deposit()
{
	int n;
	i=read();
	cout<<"Enter the amount to be deposited :";
	cin>>n;
	bal=bal+n;
	cout<<"Your balance is :"<<bal<<endl;
}
void withdraw()
{
	int n;
	i=read();
	cout<<"Enter the amount to be withdrawn :";
	cin>>n;
	bal=bal-n;
	cout<<"Your balance is :"<<bal<<endl;
}

};

int main()
{
bool boool=1;
bank s;
int c=0;
while (boool)
{
cout<<"1.Create \n 2.Deposit \n 3.Withdraw \n 4.Details \n"; 
cout<<"Enter your choice :";
cin>>c;
switch (c)
{
case 1:
	{
	s.create();
	break;
	}
case 2:
	{
	s.deposit();
	break;
	}
case 3:
	{
	s.withdraw();
	break;
	}
case 4:
	{
	s.details();
	break;
	
	}
default:
	{
	cout<<"Invalid Input";
	break;
	}
};
cout<<"Do you want to continue\n Enter 1 to continue, 0 to exit :";
cin>>boool;
}
return 0;
}
