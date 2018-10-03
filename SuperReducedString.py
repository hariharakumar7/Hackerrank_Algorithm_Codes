x=input().strip()
l=list(x)
flag=1
while flag==1:
    flag=0
    z=l
    for i in range(0,len(l)-1):
        if i<len(z)-1:
#            print(z,i)
            if z[i]==z[i+1]:
                z=z[:i]+z[i+2:]
                flag=1
    l=z
if len(l)==0:
    print("Empty String")
else:
    print(''.join(l))
        