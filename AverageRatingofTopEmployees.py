#!/bin/python3

import os
import sys

# Complete the averageOfTopEmployees function below.
def averageOfTopEmployees(rating):
    c=0
    s=0
    for i in rating:
        if i>=90:
            c+=1
            s+=i
    print(str(round(s/c,2)).ljust(5,'0'))
if __name__ == '__main__':
    n = int(input())

    rating = []

    for _ in range(n):
        rating_item = int(input())
        rating.append(rating_item)

    averageOfTopEmployees(rating)
