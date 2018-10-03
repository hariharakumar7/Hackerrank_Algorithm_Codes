#!/bin/python3

import sys
n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    i = int(input().strip())
    if i<37:
        print(i)
    else:
        if ((i//5+1)*5)-i<3:
            print((i//5+1)*5)
        else:
            print(i)


