## Advent of Code 2018 Day 3

## imports
import os
import difflib
import re

## parameters
fname = 'input.txt'
strArray = []

## instantiate coordinates dict
## and set each value to '...'
coordinates = {}
for i in range(0,2000):
    for j in range(0,2000):
        coordinates[(i,j)] = "..."

## get input file
for line in open(fname, 'r'):
    if line.strip():           # line contains eol character(s)
        line = re.sub('[@#:\n'']', '', line)
        strArray.append(line)


## manipulate the strArray to be easier to work with
for index in range(0,len(strArray)):
    newValue = [i for i in strArray[index].split(" ")]
    strArray[index] = newValue
    strArray[index].remove('')
    strArray[index][0] = int(strArray[index][0])
    strArray[index][1] = [int(i) for i in strArray[index][1].split(",")]
    strArray[index][2] = [int(i) for i in strArray[index][2].split("x")]
    index += 1


## for each rectangle, print its value in hex to the appropriate coordinates
## if trying to write to a value that already exists
## print the special code 'ZZZ'
## 'ZZZ' will tell us that there was an overlap that occurred
for index in range(0,len(strArray)):
    value = hex(strArray[index][0])
    startX = strArray[index][1][0]
    startY = strArray[index][1][1]
    sizeX = strArray[index][2][0]
    sizeY = strArray[index][2][1]

    for i in range (0, sizeX):
        for j in range (0, sizeY):
            if (coordinates[(i+startX,j+startY)] != "..."):
                coordinates[(i+startX,j+startY)] = "ZZZ"
            else:
                coordinates[(i+startX,j+startY)] = value

## re-run the code above but this time check for overlaps
for index in range(0,len(strArray)):
    value = hex(strArray[index][0])
    startX = strArray[index][1][0]
    startY = strArray[index][1][1]
    sizeX = strArray[index][2][0]
    sizeY = strArray[index][2][1]

    ## check all coordinates of each rectangle
    for i in range (0, sizeX):
        for j in range (0, sizeY):

            ## if one of the coordinates is NOT the value
            ## then it is an overlap
            ## when that occurs, re-write the rectangle
            ## so that all characters are the special
            ## character "ZZZ"
            if (coordinates[(i+startX,j+startY)] != value):
                for k in range (0, sizeX):
                    for l in range (0, sizeY):
                        coordinates[(k+startX,l+startY)] = "ZZZ"
                break


## check the coordinates to for those that aren't blank, i.e. '...', and
## for those that aren't "ZZZ"
for i in range(0,2000):
    for j in range(0,2000):
        if(coordinates[(i,j)] != "ZZZ" and coordinates[(i,j)] != "..."):
            print(int(coordinates[(i,j)],16))
