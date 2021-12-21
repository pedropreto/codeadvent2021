#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np

file = "day6.txt"
file_path = os.path.join("../inputs", file)

# opens the file
with open(file_path) as f:
    txt = f.read()  # takes the \n

init_state = txt.split(',')
init_state = list(map(int, init_state))

day = 1
max_day = 80
timer_list = init_state.copy()

while day <= max_day:
    length = len(timer_list)
    for i in range(0, length):
        timer_list[i] -= 1
        if timer_list[i] < 0:
            timer_list.append(8)  # seventh son of the seventh son
            timer_list[i] = 6

    day += 1

print(len(timer_list))
