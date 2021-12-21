#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os

file = "day1.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():

    # starts counter
    count = 0

    for i in range(1, len(lines)):
        if int(lines[i]) > int(lines[i - 1]):
            count += 1
    return count


def part2():

    j = 3  # start
    count = 0  # starts counter

    while j < len(lines):
        if int(lines[j]) - int(lines[j-3]) > 0:
            count += 1
        j += 1

    return count


count = part2()
print(count)

