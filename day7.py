#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import statistics as stat

file = "day7.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    txt = f.read()  # takes the \n

h_positions = txt.split(',')
h_positions = list(map(int, h_positions))  # input in integers


def part1():
    total_fuel = 0
    for x in h_positions:
        median = stat.median(h_positions)  # median is the point that minimizes movements
        distance = abs(x - median)
        total_fuel += distance  # total fuel is equal to the distance made by every element to reach the median
    return total_fuel


def calculate_fuel(point, h_positions):
    """
    calculates the fuel assuming that every step needs 1 more unit of fuel than the previous, starting at 1
    :param point: point chosen to calculate the fuel needed to move there
    :param h_positions: list of all positions
    :return: total fuel
    """
    total_fuel = 0
    for x in h_positions:
        distance = abs(x - point)
        total_fuel += distance * (distance + 1) / 2  # sum of sequential integer numbers from 1 up to the final distance
    return total_fuel


def part2():
    i = 0
    avg = round(stat.mean(h_positions), 0)  # first guess
    total_fuel_guess = calculate_fuel(point=avg, h_positions=h_positions)  # calculate fuel for first guess
    total_fuel_above = calculate_fuel(point=avg + 1, h_positions=h_positions)  # calculate fuel for point above
    total_fuel_below = calculate_fuel(point=avg - 1, h_positions=h_positions)  # calculate fuel for point below
    if total_fuel_above < total_fuel_guess:  # if value is lower, continue to make iterations to find out the local min
        while True:
            i += 1
            total_fuel_iter = calculate_fuel(point=avg + 1 + i, h_positions=h_positions)
            if total_fuel_iter < total_fuel_above:
                total_fuel_above = total_fuel_iter
                continue
            else:
                return total_fuel_above
    elif total_fuel_below < total_fuel_guess:  # if value is lower, continue to make iterations to find out the local min
        while True:
            i += 1
            total_fuel_iter = calculate_fuel(point=avg - 1 - i, h_positions=h_positions)
            if total_fuel_iter < total_fuel_below:
                total_fuel_below = total_fuel_iter
                continue
            else:
                return total_fuel_below

    return total_fuel_guess


total_fuel = part2()
print(total_fuel)