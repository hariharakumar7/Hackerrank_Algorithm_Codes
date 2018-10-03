#!/bin/python3

import os
import sys

# Complete the findTheAbsentStudents function below.
def findTheAbsentStudents(n, a):
    a=list(set(a))
    x=[]
    for i in range(1,n+1):
        if i in a:
            continue
        else:
            x.append(i)
    return x
    # Return the list of student IDs of the missing students in increasing order.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = findTheAbsentStudents(n, a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
