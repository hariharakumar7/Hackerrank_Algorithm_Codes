n,t=map(int,input().split())
width=list(input().split())
a=[int(x) for x in width]
while t>0:
    t-=1
    i,j=map(int,input().split())
    print(min(a[i:j+1]))
