n=int(input())
while n>0:
    n-=1
    x=int(input())
    l=input().split()
    l=[int(x) for x in l]
    count=1
    for i in l:
        count*=i
    print(count%1234567)
         