#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2020-01-05
# source: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
#=================================================================================
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def reverse_int(x):
    l = list()
    for i in str(x): l.append(i)
    l.reverse()
    return int(''.join(l))

def beautifulDays(i, j, k):
    count = 0
    for nbr in range(i, j+1):
        diff = abs(nbr - reverse_int(nbr))
        if diff % k == 0:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
