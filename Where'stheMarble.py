#!/bin/python3

import sys


m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
pos=m
for a0 in range(n):
    a,b = input().strip().split(' ')
    a,b = [int(a),int(b)]
    if a== pos:
        pos=b
    elif b==pos:
        pos=a
print(pos)        
