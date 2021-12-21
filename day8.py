#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from itertools import permutations


file = "day8.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():
    count = 0
    for i in lines:
        segment = i.split(' | ')
        output_string = segment[1]
        output_string = output_string.split(' ')
        for x in output_string:
            if len(x) in [2, 3, 4, 7]:
                count += 1
    return count


def is_contained(to_contain, contained):
    boolean_list = []
    for letter in contained:
        if letter in to_contain:
            boolean_list.append(True)
        else:
            boolean_list.append(False)
    if all(boolean_list):
        return True
    else:
        return False


def part2():
    acc = 0
    for i in lines:
        # initializing
        strings_to_num = {i: '' for i in list(range(0, 10))}  # create dict with matching between numbers and string
        five_letters, six_letters, one, four, seven, eight = [], [], [], [], [], []
        # parsing line
        segment = i.split(' | ')
        output_string = segment[1]
        entry = i.replace(' | ', ' ')
        entry = entry.split(' ')

        [five_letters.append(x) for x in entry if len(x) == 5]  # storing the numbers with five letters, 2, 3 and 5
        [six_letters.append(x) for x in entry if len(x) == 6]  # storing the numbers with six letters, 0, 6 and 9
        five_letters = list(set([''.join(sorted(x)) for x in five_letters]))  # uniques ordered
        six_letters = list(set([''.join(sorted(x)) for x in six_letters]))  # uniques ordered

        [one.append(''.join(sorted(x))) for x in entry if len(x) == 2 and len(one) == 0]  # find the 1
        [four.append(''.join(sorted(x))) for x in entry if len(x) == 4 and len(four) == 0]  # find the 4
        [seven.append(''.join(sorted(x))) for x in entry if len(x) == 3 and len(seven) == 0]  # find the 7
        [eight.append(''.join(sorted(x))) for x in entry if len(x) == 7 and len(eight) == 0]  # find the 8

        # convert lists of one element to single variables and assign them in the dict
        strings_to_num[1] = ''.join(map(str, one))
        strings_to_num[4] = ''.join(map(str, four))
        strings_to_num[7] = ''.join(map(str, seven))
        strings_to_num[8] = ''.join(map(str, eight))

        # analyze strings of six letters (could be 0, 6 or 9)
        for j in six_letters:
            # find if all letters of a digit are contained in the string
            four_contained = is_contained(to_contain=j, contained=strings_to_num[4])
            seven_contained = is_contained(to_contain=j, contained=strings_to_num[7])

            if four_contained and seven_contained:  # 9 contains four and seven
                strings_to_num[9] = j
            elif seven_contained and not four_contained:  # 0 contains seven but not four
                strings_to_num[0] = j
            else:  # 6 does not contain 4 nor 7
                strings_to_num[6] = j

        # analyze strings of five letters (could be 2, 3 or 5)
        for j in five_letters:
            one_contained = is_contained(to_contain=j, contained=strings_to_num[1])
            six_contains = is_contained(to_contain=strings_to_num[6], contained=j)

            if one_contained:  # 3 contains one
                strings_to_num[3] = j
            elif six_contains:  # six contains the 5
                strings_to_num[5] = j
            else:
                strings_to_num[2] = j

        output_string = output_string.split(' ')
        output_string = [''.join(sorted(x)) for x in output_string]

        output_number = []
        for s in output_string:
            for key, value in strings_to_num.items():
                if s == value:
                    output_number.append(str(key))

        output_number = int(''.join(output_number))
        acc += output_number
    return acc


result = part2()
print(result)