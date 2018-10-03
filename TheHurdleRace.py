#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
x=max(height)
if k<x:
    print(x-k)
else:
    print(0)
# your code goes here
