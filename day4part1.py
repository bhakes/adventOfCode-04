## Advent of Code 2018 Day 4
## Part 1

## imports
import os
from datetime import datetime
import re

## parameters
fname = 'input.txt'
strArray = []

calendar = dict()
for month in range(3,12):
    for day in range(0,32):
        for minute in range(0,60):
            calendar[(month,day,minute)] = "."

print(calendar[(9,9,9)])

## get input file & manipulate
for line in open(fname, 'r'):
    if line.strip():           # line contains eol character(s)
        line = re.sub('[\n#]', '', line)
        dateTime = datetime.strptime(line[1:17], "%Y-%m-%d %H:%M")

        otherData = line[18:].split(' ')
        otherData.pop(0)
        if otherData[0] == "Guard":
            otherData.pop(0)
        otherData.pop(len(otherData) - 1)
        if len(otherData) > 1:
            otherData[0] = int(otherData[0])
        strArray.append((dateTime,otherData))

sortedStrArray = sorted(strArray, key=lambda array: array)

print (sortedStrArray[:5])
## print output
print("Date\tID\tMinute")
print("\t\t000000000011111111112222222222333333333344444444445555555555")
print("\t\t012345678901234567890123456789012345678901234567890123456789")

## manipulate the strArray to be easier to work with
guardID = 0
for index in range(0,len(sortedStrArray)):
    if len(sortedStrArray[index][1])>1:
        guardID = sortedStrArray[index][1]
        continue
    if sortedStrArray[index][1] == "falls":
        month = sortedStrArray[index][0].month
        day = sortedStrArray[index][0].day
        minute = sortedStrArray[index][0].minute
        stopMonth = sortedStrArray[index + 1][0].month
        stopDay = sortedStrArray[index + 1][0].day
        stopMinute = sortedStrArray[index + 1][0].minute
        calendar[(month, day, minute)]
