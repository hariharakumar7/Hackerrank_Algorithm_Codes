#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    print(grid)
    for i in range(len(grid)):
        grid[i].sort()
    flag=1
    for i in range(len(grid)-1):
        if flag==0:
            break
        for j in range(len(grid[i])):
            if grid[i][j]<=grid[i+1][j]:
                continue
            else:
                flag=0
                break
    if flag==0:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    result=""
    for ii in range(t):
        n = int(input())
        grid = []
        for _ in range(n):
            grid_item = list(input())
            grid.append(grid_item)
        result += gridChallenge(grid)+"\n"

    fptr.write(result)

    fptr.close()
