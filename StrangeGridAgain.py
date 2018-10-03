r,c=input().split()
r,c=[int(r),int(c)]
if r%2==0:
    print((r//2)*10+(c-1)*2-9)
else:
    print((r//2)*10+(c-1)*2)    