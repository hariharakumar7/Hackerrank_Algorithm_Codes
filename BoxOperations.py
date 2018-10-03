import math
n,q=input().split()
n,q=[int(n),int(q)]
ni=input().split()
ni=[int(x) for x in ni]
def maxmin(i,j,mini,a):
    mid=0
    if i==j:
        mini=a[i]
    elif i==j-1:
        if a[i]<a[j]:
            mini=a[i]
        else:
            mini=a[j]
    else:
        mid=(i+j)//2
        mini=maxmin(i,mid,mini,a)
        mini1=maxmin(mid+1,j,mini,a)
        if mini>mini1:
            mini=mini1
    return mini
def su(a,i,j):
    if i==j:
        return a[i]
    elif j-i==1:
        return a[i]+a[j]
    else:
        return su(a,i,(i+j)//2)+su(a,((i+j)//2)+1,j)

        
while q>0:
    q-=1
    qu=input().split()
    qu=[int(x) for x in qu]
'''    
    if qu[0]==1:
        ni[qu[1]:qu[2]+1]=[x+qu[3] for x in ni[qu[1]:qu[2]+1]]
        
    elif qu[0]==2:
        ni[qu[1]:qu[2]+1]=[math.floor(x/qu[3]) for x in ni[qu[1]:qu[2]+1]]

    elif qu[0]==3:
        #print(min(ni[qu[1]:qu[2]+1]))
        print(maxmin(qu[1],qu[2],1000000000,ni))    
    else:
        print(su(ni,qu[1],qu[2]))
    '''