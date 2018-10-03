#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int t,count=0;
    float y,x1,y1,x2,y2;
      cin>>t;
    for(int l=0;l<t;l++)
        {
        count=0;
        cin>>x1>>y1>>x2>>y2;
        if(x1<x2)
            {
            for(int i=x1+1;i<x2;i++)
                {
                    y=y1+(((y2-y1)/(x2-x1))*(i-x1));
                    if(floor(y)==y)
                        {
                        count++;
                    }
            }
        }
        else if(x1>x2)
            {
            for(int i=x2+1;i<x1;i++)
                {
                    y=y1+(((y2-y1)/(x2-x1))*(i-x1));
                    if(floor(y)==y)
                        {
                        count++;
                    }
            }
        }
        cout<<count<<endl;
    }
    return 0;
}
