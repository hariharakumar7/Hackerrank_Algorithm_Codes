import sys
n,c = input().strip().split(' ')
n,c = [int(n),int(c)]
l=[]
for i in range(0,c):
    l.append(input())
b=[]
m=[]
for i in range(0,c):
    s=l[i].split()
    b.append(s[0])
    m.append(int(s[1]))    
for i in range(0,c):
    for j in range(i+1,c):
        if m[i]<m[j]:
            m[i],m[j]=m[j],m[i]
            b[i],b[j]=b[j],b[i]
x=0
count=0
while (n>0)and (x<c):
    if int(b[x])<n:
        count+=m[x]*int(b[x])
    else:
        count+=m[x]*n
    
    n-=int(b[x])
    x+=1
print(count)    
        
    
            
