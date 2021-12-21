#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

file = "day17.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    txt = f.read()  # takes the \n


txtx = txt.split('x=')[1]
txty = txt.split('y=')[1]
txtx =txtx.split(',')[0]
area_init_x, area_final_x = int(txtx.split('..')[0]), int(txtx.split('..')[1])
area_init_y, area_final_y = int(txty.split('..')[0]), int(txty.split('..')[1])


seconds = 0
max_y = 0
x, y = 0, 0
maxy = []
position_x, position_y = 0, 0
count = 0

missed = False
i = 6
for i in range(1, area_final_x + 1):
    x = i
    j = area_init_y
    bigger_y = True

    while bigger_y:
        stop_x = False
        missed = False
        if i == 0 and j == 0:
            break

        while True:
            seconds += 1

            x = max(x - 1, 0) if seconds > 1 else x
            y = j - (seconds - 1) if seconds > 1 else j
            if x == 0 and (position_x > area_final_x or position_x < area_init_x):
                bigger_y = False
                stop_x = True
                break
            position_x = position_x + x
            position_y = position_y + y
            max_y = position_y if position_y > max_y else max_y

            if area_init_x <= position_x <= area_final_x and area_init_y <= position_y <= area_final_y:
                maxy.append(max_y)
                count += 1
                position_x, position_y, x, y = 0, 0, i, 0
                max_y = 0
                seconds = 0
                break
            elif position_x > area_final_x or position_y < area_init_y:
                missed = True
                position_x, position_y, x, y = 0, 0, i, 0
                max_y = 0
                seconds = 0
                break
            else:
                continue

        if len(maxy) == 0 and not stop_x:
            bigger_y = True
        elif max_y == max(maxy) and not missed and not stop_x:
            bigger_y = True
        else:
            bigger_y = False

        j += 1
        print(j)



print(max(maxy), count)
