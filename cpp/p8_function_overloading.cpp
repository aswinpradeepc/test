#include<iostream>
#include<cmath>
using namespace std;
double res;
 	double power(int a,int b)
 	{
 		res = pow(a,b);
 		return res;
 	}
 
  	double power(float a,int b)
 	{
 		res = pow(a,b);
		return res;
 	}
  	double power(char a,int b)
 	{
 		res = pow(a,b);
 		return res;
 	}
  	double power(double a,int b)
 	{
 		res = pow(a,b);
 		return res;
 	}
 	double power(long a,int b)
 	{
 		res= pow(a,b);
 		return res;
 	}
 int main()
 {
int i,p;
float f;
long l;
char c;
double res,d;
    cout << "Enter the power : ";
    cin >> p;
    cout << "\nEnter a int type value : ";
    cin >> i;
    cout << "Int type overloaded func returned the value " << power(i, p) << endl;
    cout << "\nEnter a char type value : ";
    cin >> c;
    cout << "Char type overloaded func returned the value " << power(c, p) << endl;
    cout << "\nEnter a long type value : ";
    cin >> l;
    cout << "Long type overloaded func returned the value " << power(l, p) << endl;
    cout << "\nEnter a float type value : ";
    cin >> f;
    cout << "Float type overloaded func returned the value " << power(f, p) << endl;
    cout << "\nEnter a double type value : ";
    cin >> d;
    cout << "Double type overloaded func returned the value " << power(d, p) << endl;
return 0;
 }
