#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    s = list(input().strip())
    st="hackerrank"
    pos=0
    for i in range(len(s)):
        if pos<len(st):
            if s[i]==st[pos]:
                pos+=1            
    if pos==len(st):
        print("YES")
    else:
        print("NO")
            
    
