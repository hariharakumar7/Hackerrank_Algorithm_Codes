#!/bin/python3

import sys
s= input().strip()
l=list(s)
count=0
for i in range(0,len(l),3):
    if l[i]!="S":
        count+=1
    if l[i+1]!="O":
        count+=1
    if l[i+2]!="S":
        count+=1
print(count)