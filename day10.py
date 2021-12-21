#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import statistics as stat


file = "day10.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n

open_close = {'(': ')', '[': ']', '{': '}', '<': '>'}


def get_points(rules):
    """
    get points part 1
    :param rules: conversion of points
    :return: points of all incorrect lines
    """
    points = 0
    for line in lines:
        open_history, close_history = [], []
        for char in line:
            if char in open_close.keys():  # if character is an open bracket
                open_history.append(char)  # append to open list
            else:
                close_history.append(char)  # append to close list
                if close_history[-1] == open_close[open_history[-1]]:  # if close matches the last open
                   open_history = open_history[:-1]  # cuts the last open
                else:
                    points += rules[char]  # counts the points according to failed closing character
                    break
    return points


def get_score(rules):
    """
    calculates the score of each incomplete line and puts it in a list
    :param rules: conversion of points
    :return: list of scores, of each incomplete line
    """
    list_scores = []
    for line in lines:
        incomplete_line = True
        open_history, close_history = [], []
        for char in line:
            if char in open_close.keys():  # if character is an open bracket
                open_history.append(char)  # append to open list
            else:
                close_history.append(char)  # append to close list
                if close_history[-1] == open_close[open_history[-1]]:  # if close matches the last open
                   open_history = open_history[:-1]  # cuts the last open
                else:
                    incomplete_line = False  # if it has an incorrect character it is not an incomplete line
                    break  # pass the incorrect lines
        if incomplete_line:
            total_score = 0
            open_history.reverse()
            for char_open in open_history:
                total_score = total_score * 5 + rules[open_close[char_open]]  # calculates the score
            list_scores.append(total_score)  # stores into a list of scores for each incomplete line

    return list_scores


def part1():
    rules = {')': 3, ']': 57, '}': 1197, '>': 25137}
    points = get_points(rules)
    return points


def part2():
    rules = {')': 1, ']': 2, '}': 3, '>': 4}
    list_scores = get_score(rules)
    list_scores.sort()
    return stat.median(list_scores)


result = part2()
print(result)
