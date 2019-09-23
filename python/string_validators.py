#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-23
# source: https://www.hackerrank.com/challenges/string-validators/problem
#=================================================================================
""" Tutorials
str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

str.isdigit()
This method checks if all the characters of a string are digits (0-9).

str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).

str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).
"""
if __name__ == '__main__':
    s = input()
    al_num = al = di = lo = up = False
    for i in s:
        if i.isalnum():
            al_num = True
        if i.isalpha():
            al = True
        if i.isdigit():
            di = True
        if i.islower():
            lo = True
        if i.isupper():
            up = True
    print(al_num)
    print(al)
    print(di)
    print(lo)
    print(up)
