#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-29
# source: https://www.hackerrank.com/challenges/plus-minus/problem
#=================================================================================


def plusMinus(arr):
    negative_values = positive_values = null_values = 0
    for i in arr:
        if i < 0:
            negative_values += 1
        elif i > 0:
            positive_values += 1
        else:
            null_values += 1

    print("%.6f" % (positive_values/len(arr)))
    print("%.6f" % (negative_values/len(arr)))
    print("%.6f" % (null_values/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
