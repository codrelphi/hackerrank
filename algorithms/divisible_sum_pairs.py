#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-07
# source: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
#=================================================================================
import math
import os
import random
import re
import sys


def divisibleSumPairs(n, k, ar):
    return len([(ar[i], ar[j]) for i in range(n) for j in range(n) if i < j and (ar[i] + ar[j]) % k == 0])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
