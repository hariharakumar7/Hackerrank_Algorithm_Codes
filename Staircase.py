#!/bin/python3

import sys


n = int(input().strip())
space=''
for i in range(1,n):
    space+=' '
str='#'
for i in range(0,n):
    print(space+str)
    str+='#'
    space=space[1:]
 
    