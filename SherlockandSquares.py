import math
q=int(input())
while q>0:
    q-=1
    ab=input().split()
    a=int(ab[0])
    b=int(ab[1])
    print(math.floor(math.sqrt(b)-math.ceil(math.sqrt(a))+1))
    
    
