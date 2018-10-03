def reverse(Number):
    Reverse = 0
    while(Number > 0):
        Reminder = Number %10
        Reverse = (Reverse *10) + Reminder
        Number = Number //10
    return Reverse
ijk=input().split()
i=(int)(ijk[0])
j=(int)(ijk[1])
k=(int)(ijk[2])
count=0
for x in range(i,j+1):
   
    if (abs(x-reverse(x)))%k==0:
        count+=1
print(count)