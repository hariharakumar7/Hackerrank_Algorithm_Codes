#!/bin/python3
n=int(input())
x=[[0 for i in range(n)] for j in range(n)]
m=int(input())
while m!=0:
    m-=1
    
    a,b,c=map(int,input().split())
    cn=0
    while c!=0:
        for i in range(a-cn,a+cn+1):
            for j in range(b-cn,b+cn+1):
                if i>=0 and j>=0 and i<n and j<n:
                    print(i,j)
                    x[i][j]+=1
        c-=1
        cn+=1
    print(x)

