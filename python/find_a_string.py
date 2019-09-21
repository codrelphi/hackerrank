#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-21
# source: https://www.hackerrank.com/challenges/find-a-string/problem
#=================================================================================

def count_substring(string, sub_string):
    temp = []
    for i in range(len(string)):
        element = string.find(sub_string, i)
        if element not in temp and element!=-1:
            temp.append(element)
    return len(temp)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
