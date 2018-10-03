def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i not in factors:
                factors.append(i)
    if n > 1:
        if n not in factors:
            factors.append(n)
    return factors
q=int(input())
while(q>0):
    q-=1
    upper = int(input())
    print(len(prime_factors(upper)))
