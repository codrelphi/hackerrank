#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-29
# source: https://www.hackerrank.com/challenges/diagonal-difference/problem
#=================================================================================

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    fdiag = sdiag = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                fdiag += arr[i][i]
            if i + j == len(arr) - 1:
                sdiag += arr[i][j]
    return abs(fdiag - sdiag)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
