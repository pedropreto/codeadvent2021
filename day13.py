#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt

file = "day13.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def get_transformation(coord, fold_num):
    """
    transforms coordinates after a fold
    :param coord: x or y
    :param fold_num: coordinate of the fold
    :return: transformed coordinate
    """
    if coord > fold_num:
        t = abs((coord - fold_num)) * 2
        coord -= t
        return coord
    elif coord < fold_num:
        return coord


def get_folds(lines):
    """
    get all folds
    :param lines: lines of txt
    :return:
    """
    fold_coord = []
    folds = [x for x in lines if 'fold' in x]
    for f in folds:
        f = f.split(' ')
        fold_coord.append(f[-1])
    return fold_coord


def get_points(fold_coord, n_folds):
    """
    gets all the remaining points
    :param fold_coord: all the fold commands
    :param n_folds:
    :return: number of points, point coordinates
    """
    list_points = [x for x in lines if len(x) > 0]
    list_points = [x for x in list_points if 'fold' not in x]

    i = 0
    for fold in fold_coord:  # iterating folds
        if i == n_folds:  # if there is a limit of folds
            return len(list(set(list_points))), list_points
        list_points_new = []
        fold_split = fold.split('=')
        fold_num = int(fold_split[-1]) if len(fold_split) > 0 else []  # get coordinate of fold
        for line in list_points:  # for each set of coordinates
            line = line.split(',')
            line_x, line_y = int(line[0]), int(line[1])  # get x and y
            if 'x' in fold:
                if line_x == fold_num:  # if the point is on the fold, goodbye
                    continue
                else:
                    line_x = get_transformation(line_x, fold_num)  # transform x
            else:
                if line_y == fold_num:
                    continue
                else:
                    line_y = get_transformation(line_y, fold_num)  # transform y

            point = str(line_x) + ',' + str(line_y)
            list_points_new.append(point)  # save the point
            list_points = list_points_new
        i += 1

    return len(list(set(list_points))), list_points


def create_plot(list_points):
    x_list, y_list = [], []
    for point in list_points:
        coord = point.split(',')
        x_list.append(int(coord[0]))
        y_list.append(int(coord[1]))
    plt.scatter(x_list, y_list)
    plt.show()


def part1():
    fold_coord = get_folds(lines)
    result, _ = get_points(fold_coord, 1)
    return result


def part2():
    fold_coord = get_folds(lines)
    _, list_points = get_points(fold_coord, -1)
    create_plot(list_points)
    return 'olha o gráfico rapaz'


result = part2()
print(result)


