q=int(input())
while q>0:
    q-=1
    x=int(input())
    count=1
    for i in range(1,x+1):
        if i%2==0:
            count+=1
        else:
            count*=2
    print(count)
