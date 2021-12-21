#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np


file = "day15.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


class Point:
    instances = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cost = float('inf')
        self.visited = False

    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __lt__(self, other):
        return self.cost < other.cost

    @classmethod
    def new(cls, x, y):
        """
        Return instance with same value or create new.
        """
        for ins in cls.instances:
            if ins.x == x and ins.y == y:
                return ins
        new_ins = Point(x, y)
        cls.instances.append(new_ins)
        return new_ins

    @classmethod
    def get(cls, x, y):
        return [inst
                for inst in cls.instances
                if inst.x == x and inst.y == y
                ]


def get_adjacent_points(point, m, n):
    adjacent_points = []
    if point.x > 0:
        adjacent_points.append(Point.new(point.x - 1, point.y))
    if point.x + 1 < m:
        adjacent_points.append(Point.new(point.x + 1, point.y))
    if point.y > 0:
        adjacent_points.append(Point.new(point.x, point.y - 1))
    if point.y + 1 < n:
        adjacent_points.append(Point.new(point.x, point.y + 1))
    return adjacent_points

#
# i, j = 0, 0
# start = Point.new(0, 0)
# start.visited = True
# start.cost = 0
# point = start
# m, n = len(lines[0]), len(lines)
# unvisited_points = []
# i = 0
# while True:
#     print(i)
#     i+=1
#     adj = get_adjacent_points(point, m, n)
#     if len(adj) == 0:
#         break
#     for adj_point in adj:
#         if adj_point.visited:
#             continue
#         else:
#             adj_point.cost = min(adj_point.cost, point.cost + int(lines[adj_point.x][adj_point.y]))
#     unvisited_points = [x for x in Point.instances if not x.visited]
#     if len(unvisited_points) == 0:
#         break
#     next_point = min(unvisited_points, key=lambda x: x.cost)
#     if next_point.x == m - 1 and next_point.y == n - 1:
#         break
#     next_point.visited = True
#     point = next_point
#
# last = Point.get(m - 1, n - 1)[0]
# print(last.cost)




i, j = 0, 0
start = Point.new(0, 0)
start.visited = True
start.cost = 0
point = start
m, n = len(lines[0]), len(lines)
unvisited_points = {}

while True:
    print(point)
    adj = get_adjacent_points(point, m, n)
    if len(adj) == 0:
        break
    for adj_point in adj:
        if not adj_point.visited:
            unvisited_points[adj_point] = adj_point.cost
        if adj_point not in unvisited_points:
            continue
        else:
            adj_point.cost = min(adj_point.cost, point.cost + int(lines[adj_point.x][adj_point.y]))
    # unvisited_points = [x for x in Point.instances if not x.visited]
    # if len(unvisited_points) == 0:
    #     break
    next_point = min(unvisited_points, key=unvisited_points.get)
    if next_point.x == m - 1 and next_point.y == n - 1:
        break
    next_point.visited = True
    del unvisited_points[next_point]
    point = next_point

last = Point.get(m - 1, n - 1)[0]
print(last.cost)




