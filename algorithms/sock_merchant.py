#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-09
# source: https://www.hackerrank.com/challenges/sock-merchant/problem
#=================================================================================
import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    ar.sort()
    cpt = nbr = 0
    x = [i for i in ar if ar.count(i)==1]
    [ar.remove(i) for i in x]
    for i in ar:
        nbr = ar.count(i)
        cpt += nbr // 2
        for j in range(nbr):
            ar.remove(i)
    return cpt

if __name__ == '__main__':
    """fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()"""
    #ar = [10, 20, 10, 10, 30, 50, 10, 20]
    #ar = [6, 5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5]
    ar = [44, 55, 11, 15, 4, 72, 26, 91, 80, 14, 43, 78, 70, 75, 36, 83, 78, 91, 17, 17, 54, 65, 60, 21, 58, 98, 87, 45, 75, 97, 81, 18, 51, 43, 84, 54, 66, 10, 44, 45, 23, 38, 22, 44, 65, 9, 78, 42, 100, 94, 58, 5, 11, 69, 26, 20, 19, 64, 64, 93, 60, 96, 10, 10, 39, 94, 15, 4, 3, 10, 1, 77, 48, 74, 20, 12, 83, 97, 5, 82, 43, 15, 86, 5, 35, 63, 24, 53, 27, 87, 45, 38, 34, 7, 48, 24, 100, 14, 80, 54]
    result = sockMerchant(len(ar), ar)
    print(result)
