#!/bin/python3

import sys


s =list(input().strip())
a=[]
b=set(s)
c=1
a.append((ord(s[0])-96)*c)
for i in range(len(s)):
    if s[i]==s[i-1]:
        c+=1
        a.append((ord(s[i])-96)*c)
    else:
        c=1
        a.append((ord(s[i])-96)*c)
n = int(input().strip())
for a0 in range(n):
    x = int(input().strip())
    flag=0
    for i in a:
        if x==i:
            flag=1
    if flag==1:
        print("Yes")
    else:
        print("No")
    
