from fractions import Fraction
def abc(a,b,c,d):
    nu=[1]
    de=[d]
    for i in range(1,c+1):
        nu.append((i+1)*de[-1])
        de.append(nu[-2]+de[-1])  
    totnum=1
    for i in nu:
        totnum*=i
    totden=1
    for i in de:
        totden*=i
    for i in range(0,b):
        totnum=totnum//nu[i]
        totden=totden//de[i]
    li=[totnum,totden]
    return li
q=int(input())
tq=(3*q)//4
while q>0:
    q-=1
    tq-=1
    a,b,c,d=input().split()
    a,b,c,d=[int(a),int(b),int(c),int(d)]
    if a==1:
        li=abc(a,b,c,d)
        totnum=li[0]
        totden=li[1]
        MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]
        z=MMI(Fraction(totnum,totden).denominator,1000000007)
        zz=(Fraction(totnum,totden).numerator*z)%1000000007
        print(zz)
    else:
        tot=[]
        totnum=1
        totden=1
        for j in range(0,c+1):
            nu=[1]
            de=[d+j]
            for i in range(1,b+1):
                nu.append((i+1)*de[-1])
                de.append(nu[-2]+de[-1])                
            tot.append(Fraction((i+1)*de[-2],nu[-2]+de[-2]))
        for i in range(len(tot)):
            totnum*=tot[i].numerator
            totden*=tot[i].denominator
        MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]
        z=MMI(Fraction(totnum,totden).denominator,1000000007)
        zz=(Fraction(totnum,totden).numerator*z)%1000000007
        print(zz)
