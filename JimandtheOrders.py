#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):
    c=[i+1 for i in range(len(orders))]
    serve=[orders[i][0]+orders[i][1] for i in range(len(orders))]
    print(serve)
    for i in range(len(serve)):
        for j in range(i+1,len(serve)):
            if serve[i]>serve[j]:
                serve[i],serve[j]=serve[j],serve[i]
                orders[i],orders[j]=orders[j],orders[i]
                c[i],c[j]=c[j],c[i]
            elif serve[i]==serve[j]:
                if c[i]>c[j]:
                    c[i],c[j]=c[j],c[i]
                    serve[i],serve[j]=serve[j],serve[i]
                    orders[i],orders[j]=orders[j],orders[i]
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
