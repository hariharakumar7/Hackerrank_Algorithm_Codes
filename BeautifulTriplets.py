ab=list(map(int,input().split()));
a=ab[0]
b=ab[1]
count=0
x=list(map(int,input().split()));
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        for k in range(j+1,len(x)):
            if x[j]-x[i]==x[k]-x[j]:
                if x[j]-x[i]==b:
                    count+=1
print(count);
                
                