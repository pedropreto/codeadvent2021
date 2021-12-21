#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np

file = "day5.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def generate_grid(part):
    """
    generates an array that adds 1 when a lines passes through those coordinates
    :param part: part1 or part2 of the problem
    :return: a filled array
    """
    for idx, x in enumerate(lines):
        x = x.split(' -> ')
        init, final = x[0].split(','), x[1].split(',')
        x1, y1 = int(init[0]), int(init[1])
        x2, y2 = int(final[0]), int(final[1])
        if idx == 0:
            aux_array = np.zeros((max(y1, y2) + 1, max(x1, x2) + 1))  # generates the array
        else:
            if max(x1, x2) + 1 > len(aux_array.transpose()):  # checks if array needs to be enlarged to the right
                extra_columns = max(x1, x2) + 1 - len(aux_array.transpose())
                aux_array = np.hstack((aux_array, np.zeros((len(aux_array), extra_columns))))  # adds columns of zeros
            if max(y1, y2) + 1 > len(aux_array):  # checks if array needs to be enlarged downwards
                extra_rows = max(y1, y2) + 1 - len(aux_array)
                aux_array = np.vstack((aux_array, np.zeros((extra_rows, len(aux_array.transpose())))))
                # add rows of zeros

        if x1 == x2:
            range_y = range(min(y1, y2), max(y1, y2) + 1)
            for i in range_y:
                aux_array[i][x1] += 1
        elif y1 == y2:
            range_x = range(min(x1, x2), max(x1, x2) + 1)
            for i in range_x:
                aux_array[y1][i] += 1
        else:  # diagonal part
            if part != 'part2':
                continue
            range_x = range(min(x1, x2), max(x1, x2) + 1)
            if x1 == min(x1, x2):
                i, i2 = y1, y2
            else:
                i, i2 = y2, y1
            step = int((i2 - i)/abs(i2-i))
            for j in range_x:
                aux_array[i][j] += 1
                i += step

    return aux_array


def part1():
    aux_array = generate_grid(part="part1")
    return np.count_nonzero(aux_array > 1)


def part2():
    aux_array = generate_grid(part="part2")
    return np.count_nonzero(aux_array > 1)


result = part1()
print(result)

