x=int(input())
b=input().split()
l=set(b)
b=[int(x) for x in b]
l=[int(x) for x in l]
ma=0
for i in l:
    if ma<b.count(i):
        ma=b.count(i)
print(len(b)-ma)    

    