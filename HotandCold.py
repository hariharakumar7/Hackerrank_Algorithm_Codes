#!/bin/python3

import sys

def isSatisfiable(c1, c2, h1, h2):
    if min(h1,h2)-max(c1,c2)<0:
        return "NO"
    else:
        return "YES"

# Return "YES" if all four conditions can be satisfied, and "NO" otherwise
c1, c2, h1, h2 = input().strip().split(' ')
c1, c2, h1, h2 = [int(c1), int(c2), int(h1), int(h2)]
result = isSatisfiable(c1, c2, h1, h2)
print(result)
