#!/bin/python3

import sys

def getPoints(month1, month2, month3):
    coun=0
    if month1>10:
        coun+=100
    else:
        coun+=month1*10
    if month2>10:
        coun+=100
    else:
        coun+=month2*10
    if month3>10:
        coun+=100
    else:
        coun+=month3*10
    return coun
    

month1,month2,month3 = input().strip().split(' ')
month1,month2,month3 = [int(month1),int(month2),int(month3)]
pointsEarned = getPoints(month1, month2, month3)
print(pointsEarned)
