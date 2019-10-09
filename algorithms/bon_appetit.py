#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-09
# source: https://www.hackerrank.com/challenges/bon-appetit/problem
#=================================================================================
import math
import os
import random
import re
import sys


def bonAppetit(bill, k, b):
    bill_declined = bill[k]
    bill_actual = int((sum(bill) - bill_declined) / 2)
    if bill_actual == b:
        print('Bon Appetit')
    else:
        overcharged = b - bill_actual
        print(overcharged)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
