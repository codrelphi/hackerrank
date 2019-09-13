#! /usr/bin/python3
# -*- coding: utf-8 -*-
#================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-13
# source: https://www.hackerrank.com/challenges/py-if-else/problem
#================================================================================
import sys

if __name__ == "__main__":
    n = int(input())
    if n < 1 or n > 100:
        print("Error: 1 <= n <= 100 !")
        exit()
    if n % 2:
        # n is odd
        print("Weird")
    else:
        # n is even
        if n in range(2, 5) or n == 5:
            print("Not Weird")
        if n in range(6, 20) or n == 20:
            print("Weird")
        if n > 20:
            print("Not Weird")
