#!/bin/python3

import sys


s = input().strip()
n = int(input().strip())
le=len(s)
count=0
for i in range(0,le):
    if s[i]=='a':
        count+=1
times=n/le;
x=times-int(times)
if(x>0):
    x=int(times)+1
else:
    x=int(times)
count=(x-1)*count
le=n-(x-1)*le
for i in range(0,le):
    if s[i]=='a':
        count+=1
print(count)       

    


