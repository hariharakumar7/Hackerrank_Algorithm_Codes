#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(n, k, contests):
    l=[]
    x=0
    for i in range(len(contests)):
        if contests[i][1]==1:
            l.append(contests[i][0])
        else:
            x+=(contests[i][0])
    print(x)
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]<l[j]:
                l[i],l[j]=l[j],l[i]
    print(k,l)
    for i in range(0,min(k,len(l))):
        x+=l[i]
    for i in range(k,len(l)):
        x-=l[i]
    return x
        
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(n, k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
