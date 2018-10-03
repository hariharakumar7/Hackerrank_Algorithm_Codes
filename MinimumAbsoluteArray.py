#!/bin/python3

import sys


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
ans=10000000
a.sort()
for i in range(len(a)-1):
    if ans>abs(a[i]-a[i+1]):
            ans=abs(a[i]-a[i+1])
    '''for j in range(i+1,len(a)):
        if ans>abs(a[i]-a[j]):
            ans=abs(a[i]-a[j])'''
# your code goes here
print(ans)
