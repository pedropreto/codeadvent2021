#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os

file = "day2.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():

    # starts counters
    depth = 0
    h_position = 0

    for i in lines:
        command, amount = i.split(" ")
        amount = int(amount)
        if command == 'forward':
            h_position += amount  # horizontal position changes
        elif command == 'down':
            depth += amount  # depth changes
        elif command == 'up':
            depth -= amount  # depth changes

    return h_position, depth


def part2():

    # starts counters
    depth = 0
    h_position = 0
    aim = 0

    for i in lines:
        command, amount = i.split(" ")
        amount = int(amount)
        if command == 'forward':
            h_position += amount  # horizontal position changes
            depth += int(amount) * aim  # depth changes
        elif command == 'down':
            aim += amount  # aim changes
        elif command == 'up':
            aim -= amount  # aim changes

    return h_position, depth, aim


h_position, depth, aim = part2()
print(h_position, depth, aim, h_position * depth)
