#!/bin/python3

import sys


n,t = input().strip().split(' ')
n,t = [int(n),int(t)]
c = list(map(int, input().strip().split(' ')))
# your code goes here
count=0
temp=n
c=c[:-1]
for i in c:
    n-=i
    if n<5:
        count+=temp-n
        n+=temp-n
print(count)        
        
