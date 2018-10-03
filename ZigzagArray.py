#!/bin/python3

import sys

def minimumDeletions(a):
    pos=[]
    for i in range(len(a)-2):
        if a[i+1]-a[i]>0 and a[i+2]-a[i+1]>0:
            pos.append(i+1)
        if a[i+1]-a[i]<0 and a[i+2]-a[i+1]<0:
            pos.append(i+1)
    return len(pos)
    
        

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Return the minimum number of elements to delete to make the array zigzag
result = minimumDeletions(a)
print(result)
