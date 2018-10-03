#!/bin/python3

import sys

def getArrayKb(n, d):
    pro=1
    for i in range(n):
        pro*=d[i]
    pro*=4
    pro=int(pro//1024)
    return pro

#  Return the size of the multidimensional array in kilobytes. Return only the integer part.
n = int(input().strip())
d = list(map(int, input().strip().split(' ')))
result = getArrayKb(n, d)
print(result)
