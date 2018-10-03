#!/bin/python3

import sys

def maxScoreOfVincent(n, s, t):
    s=list(s)
    t=list(t)
    cou=0
    for i in range(n):
        if s[i]!=t[i] and s[i]!=".":
            cou+=1
    return cou

#  Return the maximum score of Vincent.
n = int(input().strip())
s = input().strip()
t = input().strip()
result = maxScoreOfVincent(n, s, t)
print(result)
