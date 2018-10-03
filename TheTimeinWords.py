#!/bin/python3

import sys


h = int(input().strip())
m = int(input().strip())
'''
tens=["ten","twenty","thirty","forty","fifty"]
ones=["one","two","three","four","five","six","seven","eight","nine","eleven","tweleve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
output="";
if(m>30):
    h+=1
    if(m%10==0):
        output=tens[((60-m)//10-1)]+" minutes to ";
    elif m%15==0:
        output="quarter to ";
    else:
        output=tens[((60-m)//10-1)]+" "+ones[((60-m)//10)]+" minutes to ";
elif m==30:
    output="half past ";
else:
    if(m%10==0):
        output=tens[(m//10-1)]+" minutes past ";
    elif m%15==0:
        output="quarter past ";
    else:
        output=tens[(m//10-1)]+" "+ones[(m//10)+1]+" minutes past ";        
output+=ones[h-1];
print(output)
'''
class TimeInWords2():
    def __init__(self):
        self.words=["one", "two", "three", "four", "five", "six", "seven", "eight","nine", 
       "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen",
       "seventeen", "eighteen", "nineteen", "twenty", "twenty one", 
       "twenty two", "twenty three", "twenty four", "twenty five", 
       "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]
         
 
         
 
    def caltime(self):
        hrs = h
        mins = m
        header=""
        msg=""
        if (hrs >12):
            hrs=hrs-12
        if (mins == 0):
            hr = self.words[hrs-1]
            msg=header + hr + " o' clock"
        elif (mins < 31):
            hr = self.words[hrs-1]
            mn= self.words[mins-1]
            msg = header + mn + " minutes past " + hr 
        else:
            hr = self.words[hrs]
            mn =self.words[(60 - mins-1)]
            msg = header + mn + " minutes to " + hr
        return msg
 
 
if __name__ == '__main__':
    t = TimeInWords2()
    print(t.caltime())