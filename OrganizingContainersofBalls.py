#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    M = []
    for M_i in range(n):
        M_t = [int(M_temp) for M_temp in input().strip().split(' ')]
        M.append(M_t)
    count=0
    for i in range(0,n):
        count+=M[i][0]
    temp=0
    flag=1
#    print(count,"===")
    for i in range(0,n):
        temp=0
        for j in range(0,n):
            temp+=M[j][i]
        if temp==count:
            continue
        else:
            flag=0
            break
#        print(temp) 
    if flag==1:
        print("Possible")
    else:
        print("Impossible")