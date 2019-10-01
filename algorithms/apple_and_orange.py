#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-01
# source: https://www.hackerrank.com/challenges/apple-and-orange/problem
#=================================================================================
import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    position_apples = [(a + apple) for apple in apples]
    position_oranges = [(b + orange) for orange in oranges]
    print(len([apple for apple in position_apples if apple >= s and apple <= t]))
    print(len([orange for orange in position_oranges if orange >= s and orange <= t]))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
