#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-22
# source: https://www.hackerrank.com/challenges/capitalize/problem
#=================================================================================
import math
import os
import random
import re
import sys

def solve(s):
    for i in s.split():
        s = s.replace(i, i.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
    #print(result)
