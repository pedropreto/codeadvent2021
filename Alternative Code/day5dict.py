#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np

file = "day5.txt"
file_path = os.path.join("../inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def generate_map_coordinates(diagonals):
    """
    generates a dict with all the coordinates that were visited at least once
    :param diagonals: boolean, if you want to ignore diagonal lines or not
    :return: dict with points and how many times they were visited
    """
    map_coordinates = {}
    for idx, z in enumerate(lines):
        z = z.split(' -> ')
        init, final = z[0], z[1]
        x1, y1 = int(init.split(',')[0]), int(init.split(',')[1])
        x2, y2 = int(final.split(',')[0]), int(final.split(',')[1])

        step_x = np.sign(x2 - x1)  # slope x
        step_y = np.sign(y2 - y1)  # slope y
        number_steps = max(abs(x2 - x1), abs(y2 - y1))

        i, j = 0, 0
        while abs(i) <= number_steps and abs(j) <= number_steps:  # while x or y haven't reached the end point
            if step_x != 0 and step_y != 0 and not diagonals:  # if ignoring the diagonals break here
                break
            x = x1 + i
            y = y1 + j
            coordinates = str(x) + "," + str(y)
            if coordinates in map_coordinates.keys():  # if they are already in dict, join 1, if not, create them with 1
                map_coordinates[coordinates] += 1
            else:
                map_coordinates[coordinates] = 1
            i += step_x
            j += step_y
    return map_coordinates


def count_intersected_points(map_coordinates, n_min_intersections):
    """
    counts number of points that have a min of intersections
    :param map_coordinates: dict with all the coordinates visited at least once
    :param n_min_intersections: minimum of how many times a point was visited
    :return: count of points with n_min_intersections or more
    """
    count = 0
    for value in map_coordinates.values():
        if value >= n_min_intersections:
            count += 1
    return count


def part1():
    map_coordinates = generate_map_coordinates(diagonals=False)
    count = count_intersected_points(map_coordinates, n_min_intersections=2)
    return count


def part2():
    map_coordinates = generate_map_coordinates(diagonals=True)
    count = count_intersected_points(map_coordinates, n_min_intersections=2)
    return count


count = part1()
print(count)