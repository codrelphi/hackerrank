#! /usr/bin/python3
# -*- coding: utf-8 -*-
#================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-19
# source: https://www.hackerrank.com/challenges/python-tuples/problem
#================================================================================

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_tuple = tuple(integer_list)
    print(hash(integer_tuple))
