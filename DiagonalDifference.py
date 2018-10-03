#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
count=0
for i in range(0,len(a)):
    count+=a[i][i]
    count-=a[i][len(a)-i-1]
print(abs(count))
    
