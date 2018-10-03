#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSum function below.
def minimumSum(l, r):
    a=[]
    a=[0 for i in range(len(l))]
    a[0]=r[0]
    for i in range(1,len(l)):
        if a[i-1] in range(l[i],r[i]+1):
            a[i]=a[i-1]
        else:
            if a[i-1]<l[i]:
                a[i]=l[i]
            else:
                a[i]=r[i]
    print(a)
    s=0
    for i in range(len(a)-1):
        s+=abs(a[i]-a[i+1])
    return s
            
        
    # Return the minimum sum among all arrays that satisfy the condition.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    l = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = minimumSum(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
