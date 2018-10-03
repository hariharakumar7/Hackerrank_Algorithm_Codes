#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(n, arr):
    s=list(set(arr))
    s.sort()
    x=10**10
    for i in range(len(s)-1):
        #print(abs(s[i]-s[i+1]))
        if abs(s[i]-s[i+1])<x:
            x=abs(s[i]-s[i+1])
    return x
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
