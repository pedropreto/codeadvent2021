#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np
from io import StringIO


file = "day9.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    txt = f.read()  # takes the \n


txt = [x + ',' if x != '\n' else x for x in txt]  # put a comma between each real character
txt = ''.join(txt[0:len(txt)])  # join everything as a string
file = StringIO(txt)  # convert to a IO object - so that it can be read afterwards

matrix = np.loadtxt(file, delimiter=',', dtype=str)  # convert to a matrix of strings - last column will be a ''
matrix = np.delete(matrix, len(matrix.transpose()) - 1, 1)  # remove last column
matrix = matrix.astype(int)  # convert all elements to int

# # initializing
# # i = 0
# # local_risk = []
# # max_value = 9
# # for row in matrix:
# #     j = 0
# #     for element in row:
# #         top = max_value if i == 0 else matrix[i - 1][j]  # if in first row, top value 10 - bigger than max value
# #         bottom = max_value if i == len(matrix) - 1 else matrix[i + 1][j]  # if in last row
# #         left = max_value if j == 0 else matrix[i][j - 1]  # if in first column
# #         right = max_value if j == len(matrix.transpose()) - 1 else matrix[i][j + 1]  # if in last column
# #         # if every surrounding element is bigger, then its a min
# #         if element < top and element < bottom and element < right and element < left:
# #             local_risk.append(element + 1)  # risk its 1 + height
# #         j += 1
# #     i += 1
# #
# # print(sum(local_risk))


def scanline(matrix, i_min, j_min, step):
    count = 0
    j = j_min
    while True:
        if matrix[i_min][j] == 9 or j == 0 or j == len(matrix.transpose()) - 1:
            return count
        else:
            size = scancolumn(matrix, i_min, j)
        j += step


def scancolumn(matrix, i_current, j, step):
    count = 0
    i = i_current
    while True:
        if matrix[i][j] == 9 or i == 0 or i == len(matrix) - 1:
            return count
        else:
            count += 1
        i += step








# initializing
i = 0
local_risk = []
max_value = 9
size = []
for row in matrix:
    j = 0
    for element in row:
        top = max_value if i == 0 else matrix[i - 1][j]  # if in first row, top value 10 - bigger than max value
        bottom = max_value if i == len(matrix) - 1 else matrix[i + 1][j]  # if in last row
        left = max_value if j == 0 else matrix[i][j - 1]  # if in first column
        right = max_value if j == len(matrix.transpose()) - 1 else matrix[i][j + 1]  # if in last column
        # if every surrounding element is bigger, then its a min
        if element < top and element < bottom and element < right and element < left:
            local_risk.append(element + 1)  # risk its 1 + height
        j += 1
    i += 1

print(sum(local_risk))