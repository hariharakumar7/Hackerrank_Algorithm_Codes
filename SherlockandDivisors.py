import math
def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True
n=int(input())
l=list(filter(is_prime,range(3,1000)))
while n>0:
    n-=1
    x=int(input())
    pro=1
    b=[]
    if x%2==0:
        pro=1
        temp=x
        
        for i in l:
            if temp==1 or temp==0:
                break
            count=0
            while temp%i==0:
                temp=temp//i
                count+=1
            b.append(count+1)
        for i in b:
            pro*=i
        z=0                
        while x%2==0:
            z+=1 
            x=x//2
            
        print(pro*(z))           
    else:
        print("0")
            
    
