import sys
y = int(input().strip())
if y<1918:
    if y%4==0:
        s=str(y)
        s="12.09."+s
        print(s)            
    else:
        s=str(y)
        s="13.09."+s
        print(s)            
elif y==1918:
    s=str(y)
    s="26.09."+s
    print(s)
else:
    if y%400==0 or (y%4==0 and y%100!=0):
        s=str(y)
        s="12.09."+s
        print(s)            
    else:
        s=str(y)
        s="13.09."+s
        print(s)            
        
