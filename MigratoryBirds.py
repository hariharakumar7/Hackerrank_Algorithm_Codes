#!/bin/python3

import sys


n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
types.sort()
a=list(set(types))
m=0
z=0 
for i in a:
    if m<types.count(i):
        m=types.count(i)
        z=i
print(z)        
