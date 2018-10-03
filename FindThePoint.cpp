#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int x1,x2,y1,y2,t;
    cin>>t;
    for(int i=0;i<t;i++)
        {
        cin>>x1>>y1>>x2>>y2;
        int x=2*x2-x1;
        int y=2*y2-y1;
        cout<<x<<" "<<y;
        cout<<"\n";
    }
    return 0;
}
