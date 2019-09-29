#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-29
# source: https://www.hackerrank.com/challenges/staircase/problem
#=================================================================================


def staircase(n):
    for i in range(n):
        print(" "*(n-i-1) + "#"*(i+1))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
