q=int(input())
while q>0:
    q-=1
    abc=int(input())
    s=str(abc)
    count=0
    for i in s:
        if int(i)!=0 and abc%int(i)==0:
            count+=1
    print(count)
