#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-30
# source: https://www.hackerrank.com/challenges/mini-max-sum/problem
#=================================================================================

def miniMaxSum(arr):
    l = []

    # an optimized generic version to the problem
    for i in range(len(arr)):
        s = 0
        for j in range(len(arr)):
            if i != j:
                s += arr[j]
        l.append(s)

    print("{} {}".format(min(l), max(l)))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
