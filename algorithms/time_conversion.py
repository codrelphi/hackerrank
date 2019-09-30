#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-30
# source: https://www.hackerrank.com/challenges/time-conversion/problem
#=================================================================================
import os
import sys

def timeConversion(s):
    hours = s[0:2]
    if s[8] == 'A':
        # AM time
        if hours == '12':
            hours = '00'
    else:
        # PM time
        t = {
            '01': '13',
            '02': '14',
            '03': '15',
            '04': '16',
            '05': '17',
            '06': '18',
            '07': '19',
            '08': '20',
            '09': '21',
            '10': '22',
            '11': '23',
            '12': '12'
        }
        hours = t[hours]

    return hours + ':' + s[3:8]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
