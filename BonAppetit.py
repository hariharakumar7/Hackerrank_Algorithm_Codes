ab=input().split()
n=int(ab[0])
k=int(ab[1])
c=input().split()
charge=int(input())
sum=0
for i in c:
    sum+=int(i)
sum-=int(c[k])
if (sum/2)==charge:
    print("Bon Appetit")
else:
    print(charge-int((sum/2)))