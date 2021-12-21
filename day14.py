#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from collections import Counter


file = "day14.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def get_data():
    """
    read data
    :return: template - initial string and rules_dict - conversion of pairs
    """
    template = lines[0]
    rules = [x for x in lines if '->' in x]
    # create the dict with the rules
    rules_dict = {}
    for rule in rules:
        rule = rule.split(' -> ')
        rules_dict[rule[0]] = rule[1]

    return template, rules_dict


def get_polymer(template, rules_dict, n_steps):
    """
    get the final string after the conversions of pairs
    :param template: initial string
    :param rules_dict: conversion rules NN -> C for example
    :param n_steps: how many iterations
    :return: most common value - least common value
    """
    step = 0
    final_string = template
    while step <= n_steps:
        total_string = final_string
        final_string = ''
        for i in range(0, len(total_string)):
            pair = total_string[i:i + 2]  # pair to be evaluated
            if len(pair) == 2:  # if it is a pair
                new_string = pair[0] + rules_dict[pair] + pair[1]  # put the new letter in between
                # ignore the first letter when concatenating, because the pairs have one letter in common
                # (unless it's the first pair)
                final_string = final_string + new_string[1:] if i > 0 else final_string + new_string[:]

        step += 1
    letter_counts = Counter(total_string)
    most_common = letter_counts.most_common(1)[0]
    least_common = letter_counts.most_common()[-1]
    return most_common[1] - least_common[1]


def get_init_dict(template):
    """
    convert string to dict of pairs
    :param template: initial string
    :return: dict with counts of pairs
    """
    pair_dict = {}
    for i in range(0, len(template)):
        pair = template[i:i + 2]
        if pair in pair_dict.keys():
            pair_dict[pair] += 1
        else:
            if len(pair) == 2:
                pair_dict[pair] = 1
    return pair_dict


def get_polymer_dict(template, rules_dict, n_steps):
    """
    get the count of pairs after x iterations
    :param template: initial string
    :param rules_dict: conversion rules
    :param n_steps: iterations
    :return: final number of pairs
    """
    pair_dict = get_init_dict(template)
    new_pair_dict = pair_dict
    step = 0
    while step < n_steps:
        pair_dict = new_pair_dict.copy()
        for key, value in pair_dict.items():
            if value > 0:
                new_pairs = [key[0] + rules_dict[key], rules_dict[key] + key[1]]
                new_pair_dict[key] -= value
                for new_pair in new_pairs:
                    if new_pair in new_pair_dict.keys():
                        new_pair_dict[new_pair] += value
                    else:
                        new_pair_dict[new_pair] = value
        step += 1
    return new_pair_dict


def count_letters(pair_dict, template):
    """
    pairs have one letter in common, so its counts the last letter of the pair and adds the first letter in the end
    :param pair_dict: count of pairs
    :param template: initial string
    :return: count of letters
    """
    count_dict = {}
    for key, value in pair_dict.items():
        new_key = key[1]  # counts the last letter of the pair
        if new_key in count_dict.keys():
            count_dict[new_key] += value
        else:
            count_dict[new_key] = value

    first_letter = template[0]
    count_dict[first_letter] += 1  # adds the first letter of the initial string
    return count_dict


def part1():
    template, rules_dict = get_data()
    result = get_polymer(template, rules_dict, 10)
    return result


def part2():
    template, rules_dict = get_data()
    pair_dict = get_polymer_dict(template, rules_dict, 40)
    count_dict = count_letters(pair_dict, template)
    all_values = count_dict.values()
    max_value = max(all_values)
    min_value = min(all_values)
    return max_value - min_value


result = part2()
print(result)
