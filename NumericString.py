#!/bin/python3

import sys

def getMagicNumber(s, k, b, m):
    su=0
    for i in range(len(s)-k+1):
        su+=(int(s[i:i+k],b))%m
    return su
s = input().strip()
k, b, m = input().strip().split(' ')
k, b, m = [int(k), int(b), int(m)]
result = getMagicNumber(s, k, b, m)
print(result)
