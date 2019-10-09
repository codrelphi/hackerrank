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
    cpt = nbr = 0
    for i in ar:
        nbr = ar.count(i)
        if nbr == 1:
            ar.remove(i)
            print("Delete: ", i, " ar: ", ar)
        else:
            cpt = cpt +  (nbr // 2)
            for j in range(nbr):
                ar.remove(i)
            print("Delete: ", i, " ar: ", ar)

    return cpt

if __name__ == '__main__':
    """fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()"""
    #ar = [10, 20, 10, 10, 30, 50, 10, 20]
    ar = [6, 5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5]
    result = sockMerchant(len(ar), ar)
    print(result)
