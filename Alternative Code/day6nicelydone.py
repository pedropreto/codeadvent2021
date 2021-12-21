#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np
import collections

file = "day6.txt"
file_path = os.path.join("../inputs", file)

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
    :return: collections deque to use rotate later
    """
    max_state = child_days_to_reproduce
    fish_timers = list(range(0, max_state))

    for idx, i in enumerate(fish_timers):
        fish_timers[idx] = init_state.count(i)

    return collections.deque(fish_timers)


def get_total_fish_nicely(total_days, fish_timers):
    for days in range(1, total_days + 1):
        fish_timers.rotate(-1)  # rotates the elements to the left, first goes to last
        fish_timers[days_to_reproduce - 1] += fish_timers[child_days_to_reproduce - 1]
    return sum(list(fish_timers))


def part1():
    fish_timers = get_fish_timers()
    fish = get_total_fish_nicely(total_days=80, fish_timers=fish_timers)
    return fish


def part2():
    fish_timers = get_fish_timers()
    fish = get_total_fish_nicely(total_days=256, fish_timers=fish_timers)
    return fish


fish = part1()
print(fish)
