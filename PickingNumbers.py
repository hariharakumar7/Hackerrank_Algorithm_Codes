#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pickingNumbers function below.
def pickingNumbers(a):
    m=0
    for i in range(len(a)):
        c=1
        print(a[i],end="")
        for j in range(len(a)):
            if i==j:
                continue
            if a[j]-a[i] in range(0,2):
                print(a[j],end="")
                c+=1
        print(c,"==")
        if c>m:
            m=c
        c=1
        print(a[i],end="")
        for j in range(len(a)):
            if i==j:
                continue
            if a[i]-a[j] in range(0,2):
                print(a[j],end="")
                c+=1
        print(c,"==")
        if c>m:
            m=c
    return m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
