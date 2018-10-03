#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
total=0
e=set(c)
d=list(e)
for i in d:
    total+=int(c.count(i)/2)
print(total)            
