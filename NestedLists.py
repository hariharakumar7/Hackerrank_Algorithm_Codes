if __name__ == '__main__':
    s=[]
    n=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        n.append(name)
        s.append(score)
    z=s[:]
    s=list(set(s))
    s.sort()
    x=[]
    for i in range(len(z)):
        if z[i]==s[1]:
            x.append(n[i])
    x.sort()
    for i in x:
        print(i)
    
        
        