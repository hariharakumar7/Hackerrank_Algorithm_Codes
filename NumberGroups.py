#!/bin/python3

import sys

def sumOfGroup(n):
    s=0
    x=n
    n=(n*(n+1))//2
    for i in range(2*(n-x)+1,2*n+1,2):
        s+=i
    return s
    # Return the sum of the elements of the k'th group.

if __name__ == "__main__":
    k = int(input().strip())
    answer = sumOfGroup(k)
    print(answer)
