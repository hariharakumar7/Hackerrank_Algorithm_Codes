a=0
def superdigit(n):
    n=str(n)
    if len(n)==1:
        print(n)
    else:
        
        l=[int(i) for i in list(n)]
        superdigit(sum(l))
n,k=input().split()
z=[int(i) for i in list(n)]
n1=sum(z)
superdigit(n1*k)
