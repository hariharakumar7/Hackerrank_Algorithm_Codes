#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())
p=""
l=list(s)
for i in l:
    k=k%26
    if ord(i) in range(65,91):
        if (ord(i)+k)>90:
            p+=chr(ord(i)+k-26)
        else:
            p+=chr(ord(i)+k)
    elif ord(i) in range(97,123):
        if ord(i)+k>122:
            p+=chr(ord(i)+k-26)
        else:
            p+=chr(ord(i)+k)
    else:
        p+=i
print(p)
