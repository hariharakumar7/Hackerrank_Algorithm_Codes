#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
pos=0
neg=0
zero=0
for i in arr:
    if i>0:
        pos+=1
    if i<0:
        neg+=1
print(pos/len(arr))
print(neg/len(arr))
print(1-(pos/len(arr))-neg/len(arr))