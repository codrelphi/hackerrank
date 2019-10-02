#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-01
# source: https://www.hackerrank.com/challenges/kangaroo/problem
#=================================================================================
import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    MAX_JUMPS = 100000 # simulation of positive infinity
    if x2 > x1 and v2 > v1:
        return 'NO'
    else:
        p1 = x1
        p2 = x2
        for i in range(MAX_JUMPS):
            p1 += v1
            p2 += v2
            if p1 == p2:
                return 'YES'
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
