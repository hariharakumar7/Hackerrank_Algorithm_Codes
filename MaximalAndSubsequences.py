

import sys
import itertools

def rec(n,k,a):
    return list(set(itertools.combinations(a,k)))
        

def solve(n, k, a):
    l=0
    coun=0
    zs=[]
    maxi=rec(n,k,a)
    for i in maxi:
        z=i
        s=z[0]
        for j in z:
            s=s&j           
        if s>=l:
            l=s
            zs.append(l)
               
    return [l,zs.count(l)%1000000007]            
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)
result = solve(n, k, a)
print ("\n".join(map(str, result)))


