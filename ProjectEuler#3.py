#!/bin/python3

import sys

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(max(primes(n)))
