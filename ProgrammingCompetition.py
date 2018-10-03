n = int(input().strip())
diff=0
nam=""
for a0 in range(n):
    name, d, j = input().strip().split(' ')
    name, d, j = [str(name), int(d), int(j)]
    if j-d>diff:
        nam=name
        diff=j-d
print(nam,diff)