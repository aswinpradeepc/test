#include<iostream>
using namespace std;
class vector
{
private:
    int x1,x2,x3;
public:
    vector(int a, int b, int c)
    {
        x1 = a;
        x2 = b;
        x3 = c;
    }
    vector operator+ (vector a)
    {
        vector k(0,0,0);
        k.x1 = a.x1+ x1;
        k.x2 = a.x2+ x2;
        k.x3 = a.x3+ x3;
        return k;
    }
    void show()
    {
        cout<<"The sum of vectors are :";
        cout<<"("<<x1<<","<<x2<<","<<x3<<")"<<endl;
    }
};
int main()
{
    vector p(1,2,3);
    vector q(4,5,6);
    vector o(0,0,0);
    o=p + q;
    o.show();
    return 0;
}
