#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-16
# source: https://www.hackerrank.com/challenges/write-a-function/problem
#=================================================================================

def is_leap(year):
    leap = False
    if year % 4 == 0: # leap year unless
        if year % 100 == 0: # not a leap year unless
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap

if __name__ == "__main__":
    year = int(input())
    if 1900 <= year and year <= 10**5:
        print(is_leap(year))
    else:
        print("Error: 1900 <= year <= 10^5 !")
