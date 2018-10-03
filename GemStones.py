q=int(input())
l=[]
while q>0:
    q-=1
    l.append(input())
a=list(l[0])
z=[]
count=0
flag=0
for i in a:
    for j in range(1,len(l)):
        if i in l[j]:
            continue
        else:
            flag=1
            break
    if flag==1:
        flag=0
    else:
        count+=1
        z.append(i)
z=set(z)        
print(len(z))        