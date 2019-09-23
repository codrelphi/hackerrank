#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-23
# source: https://www.hackerrank.com/challenges/python-lists/problem
#=================================================================================

if __name__ == '__main__':
    n = int(input())
    list = []
    commands = ["insert", "print", "remove", "append", "sort", "pop", "reverse"]
    for i in range(n):
        line = input()
        cmd = line.split()[0]
        if cmd == commands[0]:
            """ insert i e: Insert integer e at position i """
            list.insert(int(line.split()[1]), int(line.split()[2]))
        if cmd == commands[1]:
            """ print: Print the list """
            print(list)
        if cmd == commands[2]:
            """ remove e: Delete the first occurrence of integer e """
            list.remove(int(line.split()[1]))
        if cmd == commands[3]:
            """ append e: Insert integer e at the end of the list """
            list.append(int(line.split()[1]))
        if cmd == commands[4]:
            """ sort: Sort the list """
            list.sort()
        if cmd == commands[5]:
            """ pop: Pop the last element from the list """
            list.pop()
        if cmd == commands[6]:
            """ reverse: Reverse the list """
            list.reverse()
