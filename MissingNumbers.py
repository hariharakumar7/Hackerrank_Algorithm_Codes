#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    b=[]
    x=brr[:]
    brr=list(set(brr))
    s=[]
    for i in range(len(brr)):
        b.append(x.count(brr[i]))
    for i in range(len(brr)):
        if arr.count(brr[i])<b[i]:
            s.append(brr[i])
    s.sort()
    return s
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
