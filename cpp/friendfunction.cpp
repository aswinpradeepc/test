#include<iostream>
#include<string>
using namespace std;
class arr
{
public:
    friend void mas(arr k);
    int a[10]={2,1,5,6,3,4,8,2,6,7};
    arr(int farr[10]) {
        for (int i = 0; i < 10; i++) {
            a[i] = farr[i];
        }
    }
    void show()
    {
        for (int i = 0; i < 10; i++) {
            cout << a[i] << "," << endl;
        }
    }
};
void mas(arr k) {
    int max = k.a[0];
    for (int i = 0; i < 10; i++) {
        if (k.a[i] >max)
            max = k.a[i];
    }
    cout << "the largest number is :" << max << endl;
}
int main ()
{
    int q[10] = {1,2,6,5,4,8,6,3,6,4};
    arr s(q);
    mas(s);
    return 0;
}
