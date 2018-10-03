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
while n>0:
    n-=1
    x=int(input())
    l=list(filter(is_prime,range(1,51)))
    pro=1
    count=0
    for i in l:
        if i*pro<=x:
            pro*=i
            count+=1
        else:
            break
    print(count)
