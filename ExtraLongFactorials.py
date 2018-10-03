#!/bin/python3

import sys


n = int(input().strip())
pro=1
for i in range(2,n+1):
    pro*=i
print(pro)
