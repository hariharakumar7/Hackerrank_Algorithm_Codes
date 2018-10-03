n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
e=100
flag=1
i=0
while i!=0 or flag==1:
    flag=0
    if c[i]==1:
        e-=3
    if c[i]==0:
        e-=1
    i=(i+k)%n
print(e)        
