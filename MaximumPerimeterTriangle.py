#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    sticks.sort()
    for i in range(len(sticks)-3,-1,-1):
        if sticks[i]+sticks[i+1]>sticks[i+2]:
            return " ".join(map(str,[sticks[i],sticks[i+1],sticks[i+2]]))
            break
    return str(-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(result)
    fptr.write('\n')

    fptr.close()
