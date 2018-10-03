#!/bin/python3

import sys
import collections

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
count=0
counter=collections.Counter(c)

for i in counter.values():
    count+=int(i/2)
print(count)
    
