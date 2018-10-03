q=int(input())
while q>0:
    q-=1
    s=list(input().lower())
    t=list(input().lower())
    for i in s:
        if i in t:
            continue
        else:
            s.remove(i)
    if s==t:
        print("YES")
    else:
        print("NO")
                    
               
        
    