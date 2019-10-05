#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-03
# date(update): 2019-10-04
# source: https://www.hackerrank.com/challenges/between-two-sets/problem
#=================================================================================

def getTotalX(a, b):
    n1 = set(range(2, 6+1))
    n2 = set(range(24, 36+1))
    x = n1.union(n2)
    y = []
    z = []
    print(n1)
    print(n2)
    print(x)

    for i in list(x):
        if i % 2 == 0 and i % 6:
            y.append(i)
    print(y)
    for k in y:
        if 24 % k == 0 and 36 % k == 0:
            z.append(k)
    #x = [i for i in range(2, 96) for j in [2, 4] if i%j == 0]

    print(z)

getTotalX([2, 6], [24, 36])
