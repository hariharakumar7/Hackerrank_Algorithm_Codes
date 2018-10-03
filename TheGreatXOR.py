#!/bin/python3

import sys

count=0
q = int(input().strip())
for a0 in range(q):
    count=0
    x = int(input().strip())
    for i in range(x):
        if i^x>x:
            count+=1     
    print(count)