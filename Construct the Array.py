#!/bin/python3

import sys
def check(n,k,x,pos,curr,prev,l):
    if curr==prev:
        return 0
    if n==pos+1:
        if curr==x:
            return 0
        else:
            return 1
    else:
        s=0
        for i in range(1,k+1):
            if i==l[pos-1]:
                continue
            else:
                l[pos]=i
                s+=check(n,k,x,pos+1,i,curr,l)
        return s
def countArray(n, k, x):
    l=[0 for i in range(n)]
    l[0]=1
    l[-1]=x
    s=0
    for i in range(1,k+1):
        if i==1:
            continue
        else:
            l[1]=i
            s+=check(n,k,x,1,i,l[0],l)
    return s       
        
     
        
        
    

if __name__ == "__main__":
    n, k, x = input().strip().split(' ')
    n, k, x = [int(n), int(k), int(x)]
    answer = countArray(n, k, x)
    print(answer)
