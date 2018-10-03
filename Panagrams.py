str=input().strip().upper()
count=0
for i in range(65,93):
    if chr(i) in str:
        count+=1
if count==26:
    print("pangram")
else:
    print("not pangram")
