#!/bin/python3

import sys


n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
ans=0
count=0
x=[]
x.append(types.count(1))
x.append(types.count(2))
x.append(types.count(3))
x.append(types.count(4))
x.append(types.count(5))
m=0
if x[0]>ans:
    m=1
    ans=x[0]
if x[1]>ans:
    m=2
    ans=x[1]
if x[2]>ans:
    m=3
    ans=x[2]
if x[3]>ans:
    m=4
    ans=x[3]
if x[4]>ans:

    m=5
    ans=x[4]
print(m)    
