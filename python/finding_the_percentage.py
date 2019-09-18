#! /usr/bin/python3
# -*- coding: utf-8 -*-
#================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-18
# source: https://www.hackerrank.com/challenges/finding-the-percentage/problem
#================================================================================

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        all_scores = student_marks[query_name]
        mean = sum(all_scores)/len(all_scores)
        print("%.2f" % mean)
    else:
        print("Error:", query_name, "does't exist !")
        exit()
