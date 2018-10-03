#!/bin/python3

import sys
import math

def shortestTightArray(a, b, c):
    if b in range(min(a,c),max(c,a)+1):
        return (abs(c-a)+1)
    else:
        return (abs(b-a)+1+abs(b-c))

    

a, b, c = input().strip().split(' ')
a, b, c = [int(a), int(b), int(c)]
result = shortestTightArray(a, b, c)
print(result)
