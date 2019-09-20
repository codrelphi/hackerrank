#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-20
# source: https://www.hackerrank.com/challenges/python-string-split-and-join/problem
#=================================================================================

def split_and_join(line):
    line = line.strip()
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
