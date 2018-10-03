#!/bin/python3

import sys


n = int(input().strip())
p = int(input().strip())
# your code goes here
tot=0
if n%2==0:
    tot=(n+2)//2
else:
    tot=(n+1)//2
req=0
if p%2==0:
    req=(p+2)//2
else:
    req=(p+1)//2
if req>(tot//2):
    print(tot-req)
else:
    print(req-1)