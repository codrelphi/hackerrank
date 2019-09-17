#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-17
# source: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
#=================================================================================

if __name__ == '__main__':
    n = int(input())
    arr = input().strip().split(' ')
    if len(arr) != n:
        print("Error!")
        exit()
    arr = [int(i) for i in arr]
    #print(arr)
    actual_max = max(arr)
    for i in arr:
        if max(arr) == actual_max:
            arr.remove(actual_max)
        else:
            runner_up = max(arr)
            break
    print(runner_up)
