n=int(input())
l=[None]*n
l=[x for x in l if x is not None]
while n>0:
    n-=1
    inp=input().split()
    if inp[0]=='insert':
        l.insert(int(inp[1]),int(inp[2]))
    if inp[0]=='remove':
        l.remove(int(inp[1]))           
    if inp[0]=='append':
        l.append(int(inp[1]))
    if inp[0]=='sort':
        l=[x for x in l if x is not None]
        l.sort()
    if inp[0]=='pop':
        l.pop()
    if inp[0]=='reverse':
        l.reverse()
    if inp[0]=='print':
        print(l)
      
