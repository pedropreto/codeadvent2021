#!/usr/bin/env python
# -*- coding: utf-8 -*-------.-
import os
from itertools import product


file = "day20.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n

decode_list = lines[0]
image = lines[2:]
base_col, base_row = 3, 3
base_matrix = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
dict = {'.': 0, '#': 1}
new_image = image


def adjacent_grid(centre):
    steps = product([-1, 0, 1], repeat=len(centre))
    all_points = list((tuple(c+d for c, d in zip(centre, delta)) for delta in steps))
    return all_points


for idx_x, line in enumerate(image):
    for idx_y, pixel in enumerate(line):
        print(base_matrix)
        base_matrix = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        adj_points = adjacent_grid((idx_x, idx_y))
        for point in adj_points:
            x, y = point[0], point[1]
            base_x = x - idx_x + 1
            base_y = y - idx_y + 1
            if x < 0 or y < 0:
                print('')  # do nothing
            else:
                base_matrix[base_x][base_y] = image[x][y]

        string = ''
        for base_line in base_matrix:
            string = string + ''.join(base_line)
        for key, value in dict.items():
            string = string.replace(key, str(value))
        number = int(string, 2)
        decode = decode_list[number]
        new_image[idx_x][idx_y] = decode

        print(number, decode)

print(new_image)