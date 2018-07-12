#!/bin/python3

import math
import os
import random
import re
import sys

def stringTable(string):
    myDict = dict()
    for char in string:
        if char in myDict:
            myDict[char] += 1
        else:
            myDict[char] = 1
    return myDict

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    deletions = 0
    aDict = stringTable(a)
    bDict = stringTable(b)
    for key in aDict:
        while (key not in bDict and aDict[key] > 0) or (key in bDict and aDict[key] > bDict[key]):
            aDict[key] -= 1
            deletions += 1
    for key in bDict:
        while (key not in aDict and bDict[key] > 0) or (key in aDict and bDict[key] > aDict[key]):
            bDict[key] -= 1
            deletions += 1
    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()