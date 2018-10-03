import sys
def toString(List):
    return ''.join(List)
n=int(input())
a=list(map(str,input().split()))
k=a[n-1]
for i in range(0,n-1):
    x=n-i-2
    if int(a[x]) >int(k):
        a[x+1]=a[x]
        print(' '.join((a)))
    else:
        a[x+1]=k
        print(' '.join(a))
        sys.exit(0)
a[0]=k
print(' '.join(a))
         
