#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-17
# source: https://www.hackerrank.com/challenges/list-comprehensions/problem
#=================================================================================

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # 0 <= i <= x ; 0 <= j <= y; 0 <= k <= z
    print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k) != n)])
