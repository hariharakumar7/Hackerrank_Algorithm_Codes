q=int(input())
while q>0:
    q-=1
    s=input()
    l=list(s)
    a=[]
    for i in l:
        a.append(i)
    a.reverse()
    flag=0
    for i in range(0,len(l)-1):
        if abs(ord(l[i+1])-ord(l[i]))!=abs(ord(a[i+1])-ord(a[i])):
            flag=1
            break
    if flag==0:
        print("Funny")
    else:
        print("Not Funny")
               
        