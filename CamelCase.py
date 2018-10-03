str=input().strip()
count=1
for i in str:
    if ord(i)<93 and ord(i)>64:
        count+=1
print(count)
