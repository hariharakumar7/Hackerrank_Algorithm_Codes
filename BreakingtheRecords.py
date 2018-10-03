#!/bin/python3

import sys


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
ca=0
cb=0
ma=s[0]
mi=s[0]
for i in s:
    if ma<i:
        ca+=1
        ma=i
    if mi>i:
        cb+=1
        mi=i
print(ca,cb)        

