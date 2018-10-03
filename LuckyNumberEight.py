def powerset(s):
    n = len(s)
    masks = [1<<j for j in range(n)]
    for i in range(1,2**n):
        yield [s[j] for j in range(n) if (masks[j] & i)]


if __name__ == '__main__':
    count=0
    n=input()
    abc=input()
    for elem in powerset(list(abc)):
        val=0
        val=int(''.join(elem))
        if val%8==0:
            count+=1
            #print(val)
    print(count)            