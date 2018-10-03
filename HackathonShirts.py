#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    sizes = list(map(int, input().strip().split(' ')))
    v = int(input().strip())
    count=0
    for a1 in range(v):
        smallest,largest = input().strip().split(' ')
        smallest,largest = [int(smallest),int(largest)]
        st=""
        for i in range(n):
            if sizes[i]<largest and sizes[i]>smallest:
                count+=1
                st+=str(i)
        stt=list(st)
        stt.sort()
        for i in range(len(stt)-1,1,-1):
            del sizes[stt[i]]
    print(count+1)