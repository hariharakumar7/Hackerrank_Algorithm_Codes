a=input().split()
n=int(input())
z=input().split()
for i in z:
    for j in range(len(a)):
        if i==a[j]:
            a[j]="<b>"+a[j]+"</b>"
x=' '.join(a)
print(x)
            
