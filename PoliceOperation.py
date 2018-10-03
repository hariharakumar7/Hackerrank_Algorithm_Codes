n,w=input().split()
n,w=[int(n),int(w)]
a=input().split()
a=[int(x) for x in a]
b=[]
for i in range(0,len(a)-1):
    b.append((a[i+1]-a[i])**2)
count=0
for i in range(n-1):
    if b[i]!=1:
        count+=1
    elif b[i-1]==1:
        continue
    else:
        count+=1        
tot=count*w
pos=0
for i in range(n-2):
    if b[i]==1:
        if b[i+1]==1:
            continue
        else:
            tot+=(i-pos)**2
            pos=i
print(tot)            
            w