#!/bin/python3

import sys

count=0
s = input().strip()
for i in range(len(s)):
    if s[i]=='0':
        count+=1
    else:
        for j in range(i+1,len(s)+1):
            a=list(s)
            a=a[i:j]
            a=[int(x) for x in a]
            if (sum(a)%6==0 and a[0]!=0):
                count+=1
print(count)        
    
# your code goes here
