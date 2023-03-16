#include<iostream>
using namespace std;
class dat
{
    private:
    int day,m,year;
    bool leap=0;
    public:
        void read()
        {
            cout<<"Enter date in the format dd mm yyyy :";
            cin>>day>>m>>year;
        }
        void leapyr()
        {
        if(year%4==0)
        {
        	if(year%100==0 && year % 400==0)
        	{
        		leap=1;
        		cout<<"leap year"<<endl;
        	}
        	else if(year%100==0)
        	{
        	cout<<"not a leap year"<<endl;
        	leap=0;
        	}
        	else
        	{
        	leap=1;
        	cout<<"leap year"<<endl;
        	}
        }
        else
        {
        leap=0;
        cout<<"not a leap year"<<endl;
        }
        }
        void valid()
        {
        if (m>0 && m<13)
        {
            if (m==1||m==3||m==5||m==7||m==8||m==10|m==12)
                {
                    if ( day<32 && day>0)
                    cout<<"Valid"<<endl;
                    else
                    cout<<"invalid day"<<endl;
                }
            if (m==4||m==6|m==9||m==11)
                {
                    if ( day<31 && day>0)
                    cout<<"Valid"<<endl;
                    else
                    cout<<"invalid day"<<endl;
                }
            if (m==2)
            	{
                if (day<29)
                cout<<"Valid"<<endl;
                else
                cout<<"invalid day"<<endl;
            	}
        }
        else if (m<0||m>12)
        {cout<<"Invalid Month"<<endl;}
	}
};
int main()
{
    dat x;
    x.read();
    x.leapyr();
    x.valid();
    return 0;
}
