#!/bin/python3

import sys


s_len = int(input().strip())
s = input().strip()
li=list(s)
high=0
x=list(set(li))
flag=0
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        temp=li
        temp=list(filter((x[i]).__ne__,temp))
        temp=list(filter((x[j]).__ne__,temp))
        for k in range(0,len(temp)-2):
            if temp[k]!=temp[k+2]:
                flag=1
        if flag==0:                
            if high<len(temp):
                high=len(temp)
print(high)           
                