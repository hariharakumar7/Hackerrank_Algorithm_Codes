#!/bin/python3

import sys
import math

n = int(input().strip())
a = [int(A_temp) for A_temp in input().strip().split(' ')]
min=2147483647
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            if min>abs(i-j):
                min=abs(i-j)
if min==2147483647:
    print(-1)
else:
    print(min)
    