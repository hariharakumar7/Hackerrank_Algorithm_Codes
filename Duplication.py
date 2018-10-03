#!/bin/python3

import sys

q = int(input().strip())
s="01"
while len(s)<1000:
    z=""
    l=list(s)
    for i in l:
        if i=="0":
            z+="1"
        else:
            z+="0"
    s+=z
l=list(s)
for a0 in range(q):
    x = int(input().strip())
    print(l[x])
