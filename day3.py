#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

file = "day3.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():
    # define variables
    count_zero = 0
    count_one = 0
    count_zero_array = []
    count_one_array = []
    gamma_rate = ''
    epsilon_rate = ''

    # iterates through nth number of each line and counts zeros and ones
    for i in transpose:
        for j in i:
            if j == '0':
                count_zero += 1
            else:
                count_one += 1

        # stores the count in arrays
        count_zero_array.append(count_zero)
        count_one_array.append(count_one)
        # reset counter for each element
        count_zero = 0
        count_one = 0

    # checks what is the most frequent (and the less)
    for index, i in enumerate(count_zero_array):
        if count_zero_array[index] > count_one_array[index]:
            gamma_rate = gamma_rate + '0'
            epsilon_rate = epsilon_rate + '1'
        else:
            gamma_rate = gamma_rate + '1'
            epsilon_rate = epsilon_rate + '0'

    # converts from binary to int
    gamma_rate_dec = int(gamma_rate, 2)
    epsilon_rate_dec = int(epsilon_rate, 2)

    return (gamma_rate_dec * epsilon_rate_dec)


def part2(list_numbers, transpose_numbers):
    # checks ratings
    co2_rating = determine_rating(gas='co2', list_numbers=list_numbers.copy(), transpose_numbers=transpose_numbers.copy())
    oxygen_rating = determine_rating(gas='oxygen', list_numbers=list_numbers.copy(),
                                     transpose_numbers=transpose_numbers.copy())

    return oxygen_rating * co2_rating


def determine_rating(gas, list_numbers, transpose_numbers):
    # defines variables
    bit = 1  # start in the first bit
    count_zero, count_one = 0, 0

    while True:
        for i in transpose_numbers[bit - 1]:  # checks the nth element of every number
            if i == '0':
                count_zero += 1
            elif i == '1':
                count_one += 1

        # compares zeros with ones
        if count_zero > count_one:
            if gas == 'oxygen':  # in the case of oxygen it's the most frequent digit
                digit = '0'
            elif gas == 'co2':  # co2 it's the other one
                digit = '1'
        else:
            if gas == 'oxygen':
                digit = '1'
            elif gas == 'co2':
                digit = '0'

        # reset counters
        count_zero, count_one = 0, 0

        i = 0
        # if the digit in nth element of the number is not the digit intended, take the element out
        while i < len(list_numbers):
            if list_numbers[i][bit - 1] != digit:
                list_numbers.pop(i)
            else:
                i += 1

        # when the list reaches one, it's the end and the rating can be determined
        if len(list_numbers) == 1:
            rating = list_numbers[0]
            rating = int(rating, 2)  # convert to binary
            return rating

        bit += 1
        # transpose the list after operations
        transpose_numbers = [''.join(chars) for chars in zip(*list_numbers)]


transpose = [''.join(chars) for chars in zip(*lines)]

list_numbers = lines.copy()
transpose_numbers = [''.join(chars) for chars in zip(*list_numbers)]

result = part2(list_numbers, transpose_numbers)
print(result)





