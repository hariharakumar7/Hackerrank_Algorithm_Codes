#!/bin/python3

import sys


n,c,m = input().strip().split(' ')
n,c,m = [int(n),int(c),int(m)]
p = list(map(int, input().strip().split(' ')))
flag=1
for i in p:
    if i>m*c:
        flag=0
if flag==1:
    print("Yes");
else:
    print("No");