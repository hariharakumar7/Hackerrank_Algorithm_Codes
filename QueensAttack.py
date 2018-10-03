import sys
import math
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
rq,cq = input().strip().split(' ')
rq,cq = [int(rq),int(cq)]
count=0
obs=[]
for a0 in range(k):
    obs.append(input().strip().split())
obs=[[int(y) for y in x] for x in obs]
flag=[1,1,1,1,1,1,1,1]
pos=[[rq-1,cq-1],[rq,cq-1],[rq+1,cq+1],[rq+1,cq-1],[rq+1,cq],[rq-1,cq+1],[rq,cq+1],[rq-1,cq]]
z=max(rq-1,cq-1,n-cq,n-rq)
for i in range(z):
    for j in range(0,8):
        if pos[j] in obs and flag[j]==1:
            flag[j]=0
        elif pos[j][0]>=1 and pos[j][0]<=n and pos[j][1]>=1 and pos[j][1]<=n and flag[j]==1:
            count+=1
            if j==0:
                pos[j][0]-=1
                pos[j][1]-=1
            elif j==1:
                pos[j][1]-=1
            elif j==2:
                pos[j][0]+=1
                pos[j][1]+=1
            elif j==3:
                pos[j][0]+=1
                pos[j][1]-=1
            elif j==4:
                pos[j][0]+=1
            elif j==5:
                pos[j][0]-=1
                pos[j][1]+=1
            elif j==6:
                pos[j][1]+=1
            elif j==7:
                pos[j][0]-=1
print(count)                