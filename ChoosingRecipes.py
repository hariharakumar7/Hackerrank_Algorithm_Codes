#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    r,p,n,m = input().strip().split(' ')
    r,p,n,m = [int(r),int(p),int(n),int(m)]
    pantry = list(map(int, input().strip().split(' ')))
    cost = list(map(int, input().strip().split(' ')))
    recipe = []
    for recipe_i in range(r):
        recipe_t = [int(recipe_temp) for recipe_temp in input().strip().split(' ')]
        recipe.append(recipe_t)
    c=[]
    for i in range(r):
        count=0
        for j in range(p):
            if recipe[i][j]==1:
                if j in pantry:
                    continue
                else:
                    count+=cost[j]
        c.append(count)
    c.sort()
    count=0
    for i in range(n):
        count+=c[i]
    print(count)        
        
    # your code goes here
