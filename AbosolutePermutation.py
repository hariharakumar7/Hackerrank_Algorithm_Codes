import math
import sys
def lexicographically_next_permutation(a):
    i = len(a) - 2
    while not (i < 0 or a[i] < a[i+1]):
        i -= 1
    if i < 0:
        return False
    # else
    j = len(a) - 1
    while not (a[j] > a[i]):
        j -= 1
    a[i], a[j] = a[j], a[i]        # swap
    a[i+1:] = reversed(a[i+1:])    # reverse elements from position i+1 till the end of the sequence
    return True
 
#############################################################################
q=int(input())
while q>0:
    q-=1
    nk=(input().split())
    n=int(nk[0])
    k=int(nk[1])
    li=[]
    count=0
    total=0
    for i in range(1,n+1):
        li.append(i)
    for i in range(0,len(li)):
            if abs(i+1-li[i])==k:
                total+=1    
    if total==len(li):
        count=1
        for i in li:
            print(i,end=' ')
    total=0
    if count==0:
        while lexicographically_next_permutation(li):
        
            for i in range(0,len(li)):
                if abs(i+1-li[i])==k:
                    total+=1
            if total==len(li):
                count=1
                for i in li:
                    print(i,end=' ')
    if count==0:
        print(-1,end=' ');
    print()    
    
