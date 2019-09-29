#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-30
# source: https://www.hackerrank.com/challenges/mini-max-sum/problem
#=================================================================================

# TODO:
# - create an optimized/generic version of this script
def miniMaxSum(arr):
    l = []
    for i in range(len(arr)):
        if i == 0:
            l.append(arr[1] + arr[2] + arr[3] + arr[4])
        if i == 1:
            l.append(arr[0] + arr[2] + arr[3] + arr[4])
        if i == 2:
            l.append(arr[0] + arr[1] + arr[3] + arr[4])
        if i == 3:
            l.append(arr[0] + arr[1] + arr[2] + arr[4])
        if i == 4:
            l.append(arr[0] + arr[1] + arr[2] + arr[3])

    print("{} {}".format(min(l), max(l)))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
