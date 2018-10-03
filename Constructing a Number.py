#!/bin/python3

import sys
def sod(a):
    a=list(str(a))
    s=0
    for i in a:
        s+=int(i)
    return s


def canConstruct(a):
    a=''.join(a)
    a=int(a)
    if sod(a)%3==0:
        return "Yes"
    else:
        return "No"
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        a = input().split()
        result = canConstruct(a)
        print(result)
