#!/bin/python3

import sys

count=0
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
s = input().strip()
friends = [int(friends_temp) for friends_temp in input().strip().split(' ')]
for i in friends:
    if int(s[int(i)-1])==0:
        count=1;
        break;
if count==1:
    print("YES");
else:
    print("NO");
        
        
        