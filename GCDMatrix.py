#!/bin/python3
from fractions import gcd
import sys

def gc(a,b):
    if( a<0 ):
        a = -a
    if( b<0 ):
        b = -b;
    while( b!=0 ):
        a %= b
        if( a==0 ):
            return b
        b %= a
    return a


def search(x,a):
    for i in a:
        if i==x:
            return 1
        
n,m,q = input().strip().split(' ')
n,m,q = [int(n),int(m),int(q)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))

for a0 in range(q):
    m=[]
    r1,c1,r2,c2 = input().strip().split(' ')
    r1,c1,r2,c2 = [int(r1),int(c1),int(r2),int(c2)]
    for i in range(len(a)):
        x=[]
        for j in range(len(b)):
            x.append(gc(a[i],b[j]))
        m.append(x)
    z=[]        
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            if m[i][j] in z:
                continue
            else:
                z.append(m[i][j])
    print(len(z))            
     