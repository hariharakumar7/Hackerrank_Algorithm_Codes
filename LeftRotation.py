n,k=input().split()
n,k=[int(n),int(k)]
a=input().split()
for i in range(len(a)):
    print(a[(i+k)%n],end=" ")
