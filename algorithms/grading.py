#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-01
# source: https://www.hackerrank.com/challenges/grading/problem
#=================================================================================
import math
import os
import random
import re
import sys

def gradingStudents(grades):
    new_grades = []
    for grade in grades:
        if grade < 38:                      # no rounding
            grade = grade
        else:
            rgrade = math.ceil(grade/5) * 5 # next round grade
            if rgrade - grade < 3:          # round the grade
                grade = rgrade
            else:                           # no rounding
                grade = grade
        new_grades.append(grade)
    return new_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
