#!/bin/python3

import sys

memo=[]
for i in range(10000):
    memo.append(-1)
memo[0]=1
memo[1]=2
def fib(n):
    if n<=1:
        return 1
    if memo[n-1]!=-1:
        if memo[n-2]!=-1:
            return memo[n-1]+memo[n-2]
        memo[n-2]=fib(n-2)
        return memo[n-1]+memo[n-2]
    if memo[n-2]!=-1:
        memo[n-1]=fib(n-1)
        return memo[n-2]+memo[n-1]
    memo[n]=fib(n-1)+fib(n-2)
    return memo[n]
t = int(input().strip())
for a0 in range(t):
    x = int(input().strip())
    cur=0
    i=0
    while cur<=x:
        cur=fib(i)
        i+=1
    su=0
    for j in range(i-1):
        if memo[j]%2==0:
            su+=memo[j]
    print(su)
    
        