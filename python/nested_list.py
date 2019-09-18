#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-18
# source: https://www.hackerrank.com/challenges/nested-list/problem
#=================================================================================

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    new_students = [i for i in students if i[1]!=min(i[1] for i in students)]
    result_names = [i[0] for i in new_students if i[1]==min(i[1] for i in new_students)]
    result_names.sort()
    for i in result_names:
        print(i)
