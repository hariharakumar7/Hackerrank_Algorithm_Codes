def fact(m):
    z=1
    for i in range(1,m+1):
        z*=i
    return z
        

s=input()
q=int(input())
while q>0:
    q-=1
    a,b=map(int,input().split())
    x=s[a-1:b]
    y=list(set(list(x)))
    m=[]
    n=[]
    even=0
    odd=0
    tot=1
    for i in y:
        lm=x.count(i)
        if lm%2==0:
            m.append(i)
            even+=lm
        else:
            n.append(i)
            if lm>1:
                m.append(i)
    tot=fact(len(m))
    if len(n)!=0:
        tot*=len(n)
    print(tot%(10**9+7))
        
    
