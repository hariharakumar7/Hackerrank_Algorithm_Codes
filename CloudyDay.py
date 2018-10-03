#!/bin/python3

import sys

def maximumPeople(p, x, y, r):
    sun=0
    c=[0 for i in range(len(y))]
    for i in range(len(y)):
        flag=1
        for j in range(len(p)):
            if x[j] in range(y[i]-r[i],y[i]+r[i]):
                c[i]+=p[j]
    for i in range(len(p)):
        flag=1
        for j in range(len(y)):
            if x[i] in range(y[j]-r[j],y[j]+r[j]):
                flag=0
        if flag==1:
            sun+=p[i]
    return sun+max(c)
            
    
     
        

if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    x = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    y = list(map(int, input().strip().split(' ')))
    r = list(map(int, input().strip().split(' ')))
    result = maximumPeople(p, x, y, r)
    print(result)
