#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-17
# source: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
#=================================================================================

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = [int(i) for i in arr]
    new_arr = [i for i in arr if i!=max(arr)]
    runner_up = max(new_arr)
    print(runner_up)
    
