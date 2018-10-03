#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;
int gcd(int a, int b)
{
  int c = a % b;
  while(c != 0)
  {
    a = b;
    b = c;
    c = a % b;
  }
  return b;
}


int main(){
    int A;
    int B;
    int C;
    int D;
    int count=0;
    cin >> A >> B >> C >> D;
    for(int i=1;i<=A;i++)
        {
        for(int j=1;j<=B;j++)
            {
            for(int k=1;k<=C;k++)
                {
                for(int l=1;l<=D;l++)
                    {
                    if((i-j)%3==0)
                        {
                        if((j+k)%5==0)
                            {
                            if((i*k)%4==0)
                                {
                                if(gcd(i,l)==1)
                                    {count++;}
                            }
                        }
                    }
                }
            }
        }
    }
    cout<<count;
    return 0;
}
