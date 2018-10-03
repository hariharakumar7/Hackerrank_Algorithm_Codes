#!/bin/python3

import sys

def smallestSizeSubsequence(n, A):
    su=sum(A)
    if n==1 and su%2!=0:
        return -1
    if su%2==0:
        return 0
    else:
        return 1

n = int(input().strip())
A = list(map(int, input().strip().split(' ')))
result = smallestSizeSubsequence(n, A)
print(result)
