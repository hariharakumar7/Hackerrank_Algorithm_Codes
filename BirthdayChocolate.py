#!/bin/python3

import sys


n = int(input().strip())
squares = list(map(int, input().strip().split(' ')))
d,m = input().strip().split(' ')
d,m = [int(d),int(m)]
count=0
for i in range(len(squares)-m+1):
#   print(squares[i:i+m])
    if sum(squares[i:i+m])==d:
        count+=1
print(count)        
# your code goes here
