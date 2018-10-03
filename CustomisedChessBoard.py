#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(board):
    flag=0
    for i in range(len(board)):
        for j in range(len(board[i])-1):
            if board[i][j]!=board[i][j+1]:
                continue
            else:
                return "No"
    for i in range(len(board)-1):
        for j in range(len(board[i])):
            if board[i][j]!=board[i+1][j]:
                continue
            else:
                return "No"
    return "Yes"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        board = []

        for _ in range(n):
            board.append(list(map(int, input().rstrip().split())))

        result = solve(board)

        fptr.write(result + '\n')

    fptr.close()
