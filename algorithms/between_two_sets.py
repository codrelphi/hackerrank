#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-03
# date(update): 2019-10-04
# source: https://www.hackerrank.com/challenges/between-two-sets/problem
#=================================================================================

def getTotalX(a, b):
    x = set(range(2, 36))
    y = set()
    z = set()
    for i in x:
        for j in a:
            if i % j == 0:
                y.add(i)
    print(y)
    for k in y:
        for l in b:
            if l % k == 0:
                z.add(l)
    #x = [i for i in range(2, 96) for j in [2, 4] if i%j == 0]

    print(z)

    #return len(m)

getTotalX([2, 4], [16, 32, 96])
