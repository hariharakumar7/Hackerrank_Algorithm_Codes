#!/bin/python3

import sys

def timeCompare(t1, t2):
    x=t1[-2:]
    y=t2[-2:]
    if x>y:
        return "Second"
    elif y<x:
        return "First"
    else:
        x=t1[:2]   
        y=t2[:2]
        if int(x)==12 and t1[-2:]=="PM":
            return "First"
        if int(y)==12 and t2[-2:]=="PM":
            return "Second"
        if int(x)==12 and t1[-2:]=="AM":
            return "Second"
        if int(y)==12 and t1[-2:]=="AM":
            return "First"
        if int(x)>int(y):
            return "Second"
        elif int(x)<int(y):
            return "First"
        else:
            x=t1[3:5]
            y=t2[3:5]
            if x>y:
                return "Second"
            else:
                return "First"
q = int(input().strip())
for a0 in range(q):
    t1, t2 = input().strip().split(' ')
    t1, t2 = [str(t1), str(t2)]
    result = timeCompare(t1, t2)
    print(result)
