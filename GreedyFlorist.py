#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(n, k, c):
    c.sort()
    c=c[::-1]
    kk=[[] for i in range(k)]
    j=0
    for i in range(n):
        kk[j%k].extend([c[i]])
        j+=1
    s=0
    for i in range(len(kk)):
        for j in range(len(kk[i])):
            s+=(j+1)*kk[i][j]
    return s
            
        
        
    
    
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(n, k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
