n = int(input().strip())
a=[]
for i in range(n):
    a.append(input().strip())
b=[]
for i in a:
    b.append(list(set(list(i))))
c=0
for i in range(len(b)):
    for j in range(i+1,len(b)):
        if(len(list(set(b[i]+b[j])))==10):
              c+=1
      
      
print(c)
      
  
  