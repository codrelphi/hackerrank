#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-21
# source: https://www.hackerrank.com/challenges/python-mutations/problem
#=================================================================================

def mutate_string(string, position, character):
    # 1ère méthode
    #l = list(string)
    #l[position] = character
    #return "".join(l)

    # 2ème méthode
    return string[:position] + character + string[(position+1):]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
