memo=[]
a,b,n=input().split()
a,b,n=[int(a),int(b),int(n)]
for i in range(n):
    memo.append(0)
memo[0]=a
memo[1]=b
def fib(a,b,n):
    if n==0:
        return a
    elif n==1:
        return b
    else:
        memo[n-1]=fib(a,b,n-2)+fib(a,b,n-1)**2     
        return memo[n-1]
print(fib(a,b,n-1))        
        
        
        
    
    