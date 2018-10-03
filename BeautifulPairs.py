#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulPairs function below.
def beautifulPairs(A, b):
    s=0
    a=[0 for i in range(1001)]
    for i in A:
        a[i]+=1
    for i in range(len(b)):
        if a[b[i]]>0:
            s+=1
            a[b[i]]-=1
    if s==n:
        return s-1
    else:
        return s+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
