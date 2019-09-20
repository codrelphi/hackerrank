#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-20
# source: https://www.hackerrank.com/challenges/swap-case/problem
#=================================================================================

def swap_case(s):
    s = s.strip()
    result = ""
    for i in s:
        if i == i.upper():
            result += i.lower()
        else:
            result += i.upper()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
