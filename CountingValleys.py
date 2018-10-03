ca=0
tot=0
n=int(input())
s=list(input())
for i in range(n):
    if s[i]=="U":
        ca+=1
    else:
        ca-=1
    if ca==0:
        if s[i]=="U":
            tot+=1
print(tot)            
        