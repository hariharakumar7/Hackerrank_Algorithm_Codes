#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
x = [int(a),int(b),int(c),int(d),int(e)]
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            temp=x[i]
            x[i]=x[j]
            x[j]=temp
count=0       
for i in range(0,4):
    count+=x[i]
cou=0
for i in range(len(x)-4,len(x)):
    cou+=x[i]
print(count,cou)
