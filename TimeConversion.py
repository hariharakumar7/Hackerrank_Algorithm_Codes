#!/bin/python3

import sys


time = input().strip()
abc=time.split(':')
am=abc[2][2:]
abc[2]=abc[2][:2]
if am=='PM':
    if (int)(abc[0])!=12:
        abc[0]=(int)(abc[0])+12
if am=='AM' and (int)(abc[0])==12:
    abc[0]='00'
print((str)(abc[0])+':'+abc[1]+':'+abc[2])