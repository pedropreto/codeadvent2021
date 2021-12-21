#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np
import collections

file = "day6.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    txt = f.read()  # takes the \n

init_state = txt.split(',')
init_state = list(map(int, init_state))  # input in integers

child_days_to_reproduce = 9  # 9 days for a newborn to reproduce
days_to_reproduce = 7  # 7 days for a elder lanternfish to reproduce again


def get_fish_timers():
    """
    builds the fish timers for the initial state
    :return: dict - keys represent the days until reproduction, values represent the number of fish in that state
    """
    days_list = [x for x in range(0, max(child_days_to_reproduce, days_to_reproduce))]  # define all timers possible
    fish_timers = {i: 0 for i in days_list}  # dict with all timers, values all 0

    for key in fish_timers.keys():
        fish_timers[key] = init_state.count(key)  # count the values of each timer for the initial state

    return fish_timers


def get_total_fish(total_days, fish_timers):
    """
    finds out how many fish are in each timer after x days
    :param total_days:
    :param fish_timers: dict with initial state
    :return: fish_timers in final state
    """
    day = 0
    while day < total_days:
        fish_to_reproduce = fish_timers[0]
        for key in fish_timers.keys():
            fish_timers[key] = fish_timers[min(key+1, len(fish_timers)-1)]
        fish_timers[child_days_to_reproduce - 1] = fish_to_reproduce
        fish_timers[days_to_reproduce - 1] += fish_to_reproduce
        day += 1

    fish = 0
    for value in fish_timers.values():
        fish += value
    return fish


def part1():
    fish_timers = get_fish_timers()
    fish = get_total_fish(total_days=80, fish_timers=fish_timers)
    return fish


def part2():
    fish_timers = get_fish_timers()
    fish = get_total_fish(total_days=256, fish_timers=fish_timers)
    return fish


fish = part1()
print(fish)

