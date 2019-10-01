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
    # house [s, t]
    # apple position: a
    # orange position: b
    # apples: apples
    # oranges: oranges
    nb_apples = nb_oranges = 0
    position_apples = [(a + apple) for apple in apples]
    position_oranges = [(b + orange) for orange in oranges]
    for pa in position_apples:
        if pa >= s and pa <= t:
            nb_apples += 1

    for po in position_oranges:
        if po >= s and po <= t:
            nb_oranges += 1

    print(nb_apples)
    print(nb_oranges)

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
