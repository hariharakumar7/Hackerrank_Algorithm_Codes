#!/bin/python3

import sys


r,c = input().strip().split(' ')
r,c = [int(r),int(c)]
s="..O.."
d="O.o.O"
for i in range(r*3):
    for j in range(c):
        if i%3==0 or (i+1)%3==0:
            print(s,end="")
        else:
            print(d,end="")
    print()
# your code goes here
