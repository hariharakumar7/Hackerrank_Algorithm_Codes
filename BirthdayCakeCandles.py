#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    x=max(ar)
    return ar.count(x)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
