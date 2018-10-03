#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int fact(int x)
    {
    if(x==1||x==0)
        {return 1;}
    else
        {
        return x*fact(x-1);}
   
}
int combi(int a,int b)
    {
    int val;
    val=fact(a)/(fact(a-b)*fact(b));
    return val;
}
int main() {
    int t,n,val,res=0;
    cin>>t;
    for(int i=0;i<t;i++)
        {
        cin>>n;
        for(int j=1;j<=n;j++)
            {
            val=combi(n,j);
            res=res+val;
        }
        cout<<res<<endl;
    }
    return 0;
}
