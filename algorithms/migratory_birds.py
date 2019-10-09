#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-09
# source: https://www.hackerrank.com/challenges/migratory-birds/problem
#=================================================================================
import math
import os
import random
import re
import sys


def migratoryBirds(arr):
    birds_type_count = [arr.count(i) for i in range(1, 6)]
    max_type = max(birds_type_count)
    
    return birds_type_count.index(max_type) + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
