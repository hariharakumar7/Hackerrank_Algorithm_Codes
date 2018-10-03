#!/bin/python3

import sys


n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
for i in alice:
    if i>scores[0]:
        print(1)
    else:
        pos=1
        flag=0
        for j in range(1,len(scores)):
            if scores[j]<scores[j-1]:
                pos+=1
            if i>=scores[j]:
                print(pos)
                flag=1
                break
        if flag==0:
            print(pos+1)
