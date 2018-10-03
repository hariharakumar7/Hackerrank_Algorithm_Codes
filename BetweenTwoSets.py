nk=input().split()
n=int(nk[0])
k=int(nk[1])
a=input().split()
b=input().split()
flag=1
count=0
for i in range(int(max(a)),int(max(b))+1):
    flag=1
    for j in a:
        if i/int(j)!=float(i//int(j)):
            flag=0
            break
    flag=1
    for j in b:
        if int(j)/i!=float(int(j)//i):
            flag=0
            break
    if flag==1:
        count=count+1
print(count)
