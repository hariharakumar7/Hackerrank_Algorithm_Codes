x,y=(input().split())
x=int(x)
y=int(y)
q=int(input().strip())
l=[]
for i in range(0,q):
    l.append(input())
for i in range(0,q):
    s=l[i].split()
    x-=int(s[0])
    y-=int(s[1])
print(x,y)    
