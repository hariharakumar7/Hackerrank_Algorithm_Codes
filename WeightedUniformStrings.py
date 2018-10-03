s = input().strip()
n = int(input().strip())
z=list(s)
fin=[]
count=1
for i in range(len(z)-1):
    if z[i]==z[i+1]:
        fin.append((ord(z[i])-96)*count)
        count+=1        
    else:
        fin.append((ord(z[i])-96)*count)
        count=1
if z[-2]==z[-1]:
    count+=1
else:
    count=1
fin.append((ord(z[-1])-96)*count)
fin.sort()
for i in range(n):
    x=int(input().strip())
    flag=0
    a=0
    b=len(fin)-1
    while a!=b:
        mid=(a+b)//2
        if x==fin[mid] or x==fin[a] or x==fin[b]:
            flag=1
            break
        elif x>fin[mid]:
            a=mid+1
            continue
        elif x<fin[mid]:
            b=mid
            continue
    if flag==0:
        print("No")
    else:
        print("Yes")