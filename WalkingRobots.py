#!/bin/python3

import sys

def push(z,n):
    z.append(n)
    return z
def pop(z):
    z.pop()
    return z
    
def howManyCollisions(s):
    la=list(s)
    count=0
    l=[]
    l=push(l,la[0])
    for i in la[1:]:
    
        if i=="d":
            l=push(l,"d")
        else:
            if l[-1]==i:
                l=push(l,i)
            else:
                if i=="l":
                    x=l[-1]
                    l=pop(l)
                    if x=="d":
                        count+=1
                        l=push(l,"d")
                    else:
                        count+=2
                        l=push(l,"d")
                else:
                    l=push(l,"r")
    
    
    if l.count("d")>0 or l.count("l")>0:
        za=len(l)-2
        while za>=0:
            if l[za]=="r" and l[za+1]=="l":
                count+=2
                l[za]="d"
                l[za+1]="d"
            if l[za]=="r" and l[za+1]=="d":
                count+=1
                l[za]="d"
            za-=1
       
    return count                    

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    # Returns the number of times moving robots collide.
    result = howManyCollisions(s)
    print(result)
