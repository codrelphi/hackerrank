#! /usr/bin/python3
# -*- coding: utf-8 -*-
#================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-15
# source: https://www.hackerrank.com/challenges/python-loops/problem
#================================================================================

if __name__ == "__main__":
    n = int(input())
    if n < 1 or n > 20:
        print("Error: 1 <= n <= 20 !")
        exit()
    for i in range(n):
        print(i * i)
