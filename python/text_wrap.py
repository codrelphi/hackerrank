#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-22
# source: https://www.hackerrank.com/challenges/text-wrap/problem
#=================================================================================

import textwrap

""" wrap(self, text) ==> []
    fill(self, text) ==> str
"""
def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    return wrapper.fill(text=string)

if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
