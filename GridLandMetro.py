r,c,k=input().split()
r,c,k=[int(r),int(c),int(k)]
x=[]
for i in range(r):
    l=[]
    for j in range(c):
        l.append(0)
    x.append(l)
t=[]
while k>0:
    k-=1
    t.append(input().strip())
for i in t:
    a=i.split()
    for j in range(int(a[1]),int(a[2])+1):
        x[int(a[0])-1][j-1]=-1
count=0
for i in range(r):
    for j in range(c):
        if x[i][j]!=-1:
            count+=1
print(count)            
        
    