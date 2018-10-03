#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the swapToSort function below.
def swapToSort(a):
    # Return -1 or 0 or 1 as described in the problem statement.
    swap=0
    flag=0
    b=a[:]
    a.sort()
    for i in range(len(a)):
        if a[i]!=b[i]:
            swap+=1
        if swap>2:
            break
    if swap==0:
        return 0
    if swap>2:
        return -1
    if swap==2:
        return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = swapToSort(a)

    fptr.write(str(result) + '\n')

    fptr.close()
