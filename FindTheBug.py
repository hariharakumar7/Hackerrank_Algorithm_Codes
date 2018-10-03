#!/bin/python3

import sys

def findTheBug(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]=="X":
                return [i,j]

n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
    grid_t = str(input().strip())
    grid.append(grid_t)
# Return an array containing [r, c]
result = findTheBug(grid)
print (",".join(map(str, result)))


