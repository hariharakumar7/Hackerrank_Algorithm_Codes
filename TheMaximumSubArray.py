def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

q=int(input())
while q>0:
    q-=1
    n=input()
    total=0
    a=list(map(int,input().split()))
    print(max_subarray(a),end=' ')
    for i in range(0,len(a)):
        if a[i]>0:
            total+=a[i]
    if total!=0:           
        print(total)
    else:
        print(max(x for x in a if x<0))
