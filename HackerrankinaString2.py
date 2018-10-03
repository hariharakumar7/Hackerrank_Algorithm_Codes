#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    l=list(s)
    j=0
    x="hackerrank"
    for i in l:
        if j<len(x):
            if i==x[j]:
                j+=1
    #            print(i)
    if j==len(x):
        print("YES")
    else:
        print("NO")
    # your code goes here
