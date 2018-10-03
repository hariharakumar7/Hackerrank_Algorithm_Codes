q=int(input())
r=3
trig=3
x=0
a=1
for i in range(1,q+1):
    if q<a+r:
        x=(trig-(q-a))
        break
    elif q==a+r:
        x=trig*2
        break
    else:
        a+=r
        trig*=2
        r*=2
print(x)        
