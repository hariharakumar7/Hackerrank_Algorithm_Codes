#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        c=0
        for i in range(0,n,5):
            if (n-c)%3==0:
                break
            else:
                c+=5
        if c>n:
            print("-1")
            continue
        print("5"*(n-c),end="")
        print("3"*c)
            
