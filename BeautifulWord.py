#!/bin/python3

import sys


w = input().strip()
ls=list(w)
flag=1
z=['a','e','i','o','u','y']
for i in range(1,len(ls)):
    if (ls[i-1]==ls[i]) or (ls[i-1] in z and ls[i] in z):
        flag=0
        break
if flag==1:
    print("Yes")
else:
    print("No")
