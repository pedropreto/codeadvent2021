#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np
from io import StringIO


file = "day11.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    txt = f.read()  # takes the \n


def generate_matrix(txt):
    txt = [x + ',' if x != '\n' else x for x in txt]  # put a comma between each real character
    txt = ''.join(txt[0:len(txt)])  # join everything as a string
    file = StringIO(txt)  # convert to a IO object - so that it can be read afterwards

    matrix = np.loadtxt(file, delimiter=',', dtype=str)  # convert to a matrix of strings - last column will be a ''
    matrix = np.delete(matrix, len(matrix.transpose()) - 1, 1)  # remove last column
    matrix = matrix.astype(int)  # convert all elements to int
    return matrix


def check_flashes(matrix):
    if np.any(matrix > 9):
        flash_idxs = np.where(matrix > 9)
        row_idx, col_idx = flash_idxs[0], flash_idxs[1]
        matrix[matrix > 9] = 0
        i = 0
        for row in row_idx:
            col = col_idx[i]
            if row == 0 and col == 0:
                matrix[row][col + 1] += 1 if matrix[row][col + 1] != 0 else 0  # right
                matrix[row + 1][col + 1] += 1 if matrix[row + 1][col + 1] != 0 else 0  # down right
                matrix[row + 1][col] += 1 if matrix[row + 1][col] != 0 else 0  # down
            elif row == len(matrix) - 1 and col == len(matrix.transpose()) - 1:
                matrix[row][col - 1] += 1 if matrix[row][col - 1] != 0 else 0  # left
                matrix[row - 1][col] += 1 if matrix[row - 1][col] != 0 else 0  # up
                matrix[row - 1][col - 1] += 1 if matrix[row - 1][col - 1] != 0 else 0  # up left
            elif row == 0 and col == len(matrix.transpose()) - 1:
                matrix[row + 1][col - 1] += 1 if matrix[row + 1][col - 1] != 0 else 0  # down left
                matrix[row][col - 1] += 1 if matrix[row][col - 1] != 0 else 0  # left
                matrix[row + 1][col] += 1 if matrix[row + 1][col] != 0 else 0  # down
            elif row == len(matrix) - 1 and col == 0:
                matrix[row - 1][col] += 1 if matrix[row - 1][col] != 0 else 0  # up
                matrix[row - 1][col + 1] += 1 if matrix[row - 1][col + 1] != 0 else 0  # up right
                matrix[row][col + 1] += 1 if matrix[row][col + 1] != 0 else 0  # right
            elif row == 0:
                matrix[row][col + 1] += 1 if matrix[row][col + 1] != 0 else 0  # right
                matrix[row][col - 1] += 1 if matrix[row][col - 1] != 0 else 0  # left
                matrix[row + 1][col] += 1 if matrix[row + 1][col] != 0 else 0  # down
                matrix[row + 1][col + 1] += 1 if matrix[row + 1][col + 1] != 0 else 0  # down right
                matrix[row + 1][col - 1] += 1 if matrix[row + 1][col - 1] != 0 else 0  # down left
            elif row == len(matrix) - 1:
                matrix[row][col + 1] += 1 if matrix[row][col + 1] != 0 else 0  # right
                matrix[row][col - 1] += 1 if matrix[row][col - 1] != 0 else 0  # left
                matrix[row - 1][col] += 1 if matrix[row - 1][col] != 0 else 0  # up
                matrix[row - 1][col + 1] += 1 if matrix[row - 1][col + 1] != 0 else 0  # up right
                matrix[row - 1][col - 1] += 1 if matrix[row - 1][col - 1] != 0 else 0  # up left
            elif col == 0:
                matrix[row - 1][col] += 1 if matrix[row - 1][col] != 0 else 0  # up
                matrix[row - 1][col + 1] += 1 if matrix[row - 1][col + 1] != 0 else 0  # up right
                matrix[row + 1][col + 1] += 1 if matrix[row + 1][col + 1] != 0 else 0  # down right
                matrix[row][col + 1] += 1 if matrix[row][col + 1] != 0 else 0  # right
                matrix[row + 1][col] += 1 if matrix[row + 1][col] != 0 else 0  # down
            elif col == len(matrix.transpose()) - 1:
                matrix[row - 1][col] += 1 if matrix[row - 1][col] != 0 else 0  # up
                matrix[row - 1][col - 1] += 1 if matrix[row - 1][col - 1] != 0 else 0  # up left
                matrix[row + 1][col - 1] += 1 if matrix[row + 1][col - 1] != 0 else 0  # down left
                matrix[row][col - 1] += 1 if matrix[row][col - 1] != 0 else 0  # left
                matrix[row + 1][col] += 1 if matrix[row + 1][col] != 0 else 0  # down
            else:
                matrix[row - 1][col] += 1 if matrix[row - 1][col] != 0 else 0  # up
                matrix[row - 1][col + 1] += 1 if matrix[row - 1][col + 1] != 0 else 0  # up right
                matrix[row - 1][col - 1] += 1 if matrix[row - 1][col - 1] != 0 else 0  # up left
                matrix[row + 1][col] += 1 if matrix[row + 1][col] != 0 else 0  # down
                matrix[row + 1][col + 1] += 1 if matrix[row + 1][col + 1] != 0 else 0  # down right
                matrix[row + 1][col - 1] += 1 if matrix[row + 1][col - 1] != 0 else 0  # down left
                matrix[row][col + 1] += 1 if matrix[row][col + 1] != 0 else 0  # right
                matrix[row][col - 1] += 1 if matrix[row][col - 1] != 0 else 0  # left

            i += 1

        matrix = check_flashes(matrix)
        return matrix
    else:
        return matrix


def part1():
    matrix = generate_matrix(txt)
    i = 1
    count = 0
    while True:
        matrix = matrix + 1
        matrix = check_flashes(matrix)
        count += matrix[matrix == 0].shape[0]
        if i == 100:
            return count
        i += 1


def part2():
    matrix = generate_matrix(txt)
    i = 1
    while True:
        matrix = matrix + 1
        matrix = check_flashes(matrix)
        iter_count = matrix[matrix == 0].shape[0]
        if iter_count == 100:
            return i
        i += 1


result = part2()
print(result)