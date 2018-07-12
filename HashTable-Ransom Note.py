#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
	missingWords = n
	noteWords = dict()
	for word in note:
		if word in noteWords:
			noteWords[word] += 1
		else:
			noteWords[word] = 1   # set count to 1
	for word in magazine:
		if missingWords == 0:	# Stop early if I'm done
			return "Yes"
		if word in noteWords and noteWords[word] != 0:
			noteWords[word] -= 1
			missingWords -= 1
	# Finished iterating through magazine
	if missingWords == 0:
		return "Yes"
	return "No"



if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))