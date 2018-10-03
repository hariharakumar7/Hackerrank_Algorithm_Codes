#!/bin/python3

import sys

def solve(a,n):
    l=a[:n//2]
    s=a[n//2:]
    return (abs(sum(l)-sum(s)))
    

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = solve(a,n)
print(result)
