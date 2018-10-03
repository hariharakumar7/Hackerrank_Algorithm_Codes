n=int(input())
l=[]
m=[]
mdict=[]
while n>0:
    n-=1
    x=input().split()
    if x[0]=="store":
        a=int(x[2])
        pos=0
        for i in m:
            pos+=1
            if int(i)>a:
                break
        m.insert(pos,int(x[2]))
        l.insert(pos,x[1])
    else:
        if len(l)>0:
            print(l[-1])
            m.pop()
            l.pop()
        else:
            print("-1")
    
        
        
        
     