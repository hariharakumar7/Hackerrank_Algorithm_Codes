#!/bin/python3

import sys


n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
    unsorted_t = str(input().strip())
    unsorted.append(unsorted_t)
'''    
for i in range(n):
    for j in range(i+1,n):
        if len(unsorted[i])>len(unsorted[j]):
            unsorted[i],unsorted[j]=unsorted[j],unsorted[i]
pos=0
z=[]
for i in range(n-1):
    if len(unsorted[i])==len(unsorted[i+1]):
        pos=i
    else:
        a=unsorted[pos:i+1]
        a.sort()
        z.append(a)
print(z)        
'''
for i in range(n):
    unsorted[i]=int(unsorted[i])
unsorted.sort()
for i in unsorted:
    print(i)
# your code goes here