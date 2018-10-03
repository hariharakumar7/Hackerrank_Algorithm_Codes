#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int l,b,t,area;
    cin>>t;
    for(int z=0;z<t;z++)
        {
        int count=0,temp=0;
        cin>>l>>b;
        if(l==b)
            {
            cout<<1<<endl;
        }
        else if(l>b || b>l)
            {
            area=l*b;
            for(int i=2;i<1000;i++)
                {int s=i*i;
                if(area%s==0 && (l%i==0 && b%i==0))
                    {
                        count=area/s;
                }
            }
            if(count==0)
                {
                cout<<area<<endl;
            }
            else if(count!=0)
                {
            cout<<count<<endl;
            }
        }
    }
    return 0;
}
