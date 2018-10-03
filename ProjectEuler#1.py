t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n-=1
    a=0
    x=n//3
    a+=(3*((x)*(x+1))//2)
    x=n//5
    a+=(5*((x)*(x+1))//2)
    x=n//15
    a-=(15*((x)*(x+1))//2)
    print(a)