#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-26
# source: https://www.hackerrank.com/challenges/compare-the-triplets/problem
#=================================================================================
import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    # a: alice
    # b: bob
    result = [0, 0]

    for i in range(len(a)):
        if a[i] > b[i]:
            result[0] += 1
        if a[i] < b[i]:
            result[1] += 1

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
