#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import collections


file = "day12.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def check_small_caves(original_path, part):
    """
    check if there is a lower already twice in the array
    :param original_path: array
    :param part: 1 or 2
    :return: boolean
    """
    if part == 2:
        lowers = [x for x in original_path if x.islower()]  # get all lowers
        for l in lowers:
            if original_path.count(l) == 2:  # if any occurs twice, True, it cannot occur twice with any other lower
                return True
        return False
    else:
        return True  # part 1 is always True, this part does not matter


def count_char(original_path, char):
    return original_path.count(char)  # counts char in array


def find_adjacent(connections, original_path, final_paths, part):
    """
    from one path, gets all the possibilities in adjacent caves
    :param connections: connections between caves
    :param original_path: array where we are right now
    :param final_paths: list of possibilities
    :param part: 1 or 2
    :return: all paths possible
    """
    new_paths = []
    point = original_path[-1]  # gets last cave
    for x in connections[point]:  # for every connection to the last cave
        # for part 1 it only matters if the lowercase repeats, so if the lower > 0, skip
        # for part 2 it matters if there is any lowercase that has already 2 occurences, if yes, check if
        # the iterated lowercase has occured once
        if x == 'start' or (x.islower() and check_small_caves(original_path, part) and count_char(original_path, x) > 0):
            continue
        else:
            new_path = original_path.copy()
            new_path.append(x)  # adds new cave to the path
            new_paths.append(new_path)  # adds to the array of possibilities
    for new_path in new_paths:
        if new_path[-1] == 'end':  # if any possibility already ended, appends to the final paths (completed) and skips
            final_paths.append(new_path)
            continue
        new_paths = find_adjacent(connections, new_path, final_paths, part)  # reiterates uncompleted paths
    return final_paths


def read_connetions():
    """
    puts every connection in a dict
    :return: dict
    """
    connections = collections.defaultdict(list)
    for line in lines:
        split = line.split('-')
        first, second = split[0], split[1]
        connections[first].append(second)
        connections[second].append(first)
    return connections


def part2():
    connections = read_connetions()
    final_paths = []
    for x in connections['start']:
        path = ['start']
        path.append(x)
        paths = find_adjacent(connections, path, final_paths, 2)
    return len(paths)


def part1():
    connections = read_connetions()
    final_paths = []
    for x in connections['start']:
        path = ['start']
        path.append(x)
        paths = find_adjacent(connections, path, final_paths, 1)
    return len(paths)


result = part2()
print(result)



