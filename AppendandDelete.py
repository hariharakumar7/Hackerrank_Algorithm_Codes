import sys
import math
s = input().strip()
t = input().strip()
k = int(input().strip())
ls=list(s)
lt=list(t)
if k>len(ls)+len(lt):
    print("Yes")
else:
    count=0
    if ''.join(ls) in ''.join(lt) or ''.join(lt) in ''.join(ls):
        count=abs(len(ls)-len(lt))
    for i in range(0,min(len(ls),len(lt))):
        if ls[i]==lt[i]:
            continue
        else:
            count+=(len(ls)-i) +(len(lt)-i)
            break
#    print(count)            
    if count>k:
        print("No")
    else:        
        if (k-count)%2==0:
            print("Yes")
        else:
            print("No")
