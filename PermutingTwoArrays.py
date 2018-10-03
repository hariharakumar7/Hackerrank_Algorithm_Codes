#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoArrays function below.
def twoArrays(k, a, b):
    c=[10**10 for i in range(len(b))]
    for i in range(len(a)):
        x=-1
        for j in range(len(b)):
            if a[i]+b[j]>=k:
                if c[i]>b[j]:
                    c[i]=b[j]
                    x=j
        del b[x]
    if c.count(10**10)>0:
        return "NO"
    else:
        return "YES"
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
