#! /usr/bin/python3
# -*- coding: utf-8 -*-
#================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-13
# source: https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
#================================================================================
import sys


if __name__ == "__main__":
    a = int(input())
    if a < 1 or a > 10**10:
        print("Error: 1 <= a <= 10**10 !")
        exit()
    b = int(input())
    if b < 1 or b > 10**10:
        print("Error: 1 <= b <= 10**10 !")
        exit()

    # sum
    print(a + b)
    # difference
    print(a - b)
    # product
    print(a * b)
