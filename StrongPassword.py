s="!@#$%^&*()-+"
s=list(s)
n=int(input())
a=input()
a=list(a)
c=0
flag=0
l,m,p,q=0,0,0,0
for i in range(len(a)):
    if ord(a[i]) in range(48,58):
        l=1
    elif ord(a[i]) in range(97,123):
        m=1
    elif ord(a[i]) in range(65,91):
        p=1
    elif a[i] in s:
        q=1
if l==0:
    c+=1

if m==0:
    c+=1
if p==0:
    c+=1
if q==0:
    c+=1

if n+c<6:
    print(6-n)
else:
    print(c)
