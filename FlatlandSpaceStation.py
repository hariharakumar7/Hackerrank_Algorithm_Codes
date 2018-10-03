n,m=map(int,input().split())

c=list(map(int,input().split()))
c=sorted(c)
large=0
c=list(str(0))+c
c=c+list(str(n-1))
for i in range(0,len(c)-1):
    if int(c[i+1])-int(c[i])>large:
        large=int(c[i+1])-int(c[i])
if large==1:
    large=0
    
if large%2==0:
    print(large//2)
else:
    print(large)
        
    

