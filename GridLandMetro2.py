nmk=input().split()
n=int(nmk[0])
m=int(nmk[1])
k=int(nmk[2])
arr=[]
li=[]
for i in range(0,n):
    for j in range(0,m):
        li.append(0)
    arr.append(li)
    li=[]
while k>0:
    k-=1
    xab=input().split()
    x=int(xab[0])
    a=int(xab[1])
    b=int(xab[2])
    for i in range(a-1,b):
        arr[x-1][i]=1
total=0       
for i in range(0,n):
    for j in range(0,m):
        if arr[i][j]==0:
            total+=1
print(total)            