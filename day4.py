#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np

file = "day4.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    txt = f.read()  # takes the \n


txt = txt.split('\n\n')

numbers_drawn = txt[0].split(',')
list_board = []
list_board_aux = []


class Bingoboard:
    """
    Class Bingo Board
    Stores information about his number array, his winner_position and other important atributes
    """
    def __init__(self, array):
        self.array = array
        self.score = None
        self.sum = 0
        self.last_number_drawn = None
        self.position = None
        self.rows = len(self.array)
        self.columns = len(self.array[0])
        self.aux_array = np.zeros((self.rows, self.columns))

    def __repr__(self):
        return str(self.position)

    def calculate_score(self):
        """
        calculates the score based on the sum of the numbers that weren't matched * last number drawn before the win
        :return: nothing, stores the attribute score
        """
        for x in range(0, self.rows):
            for y in range(0, self.columns):
                if self.aux_array[x][y] == 0:  # if it has a zero, it was not matched, so sum
                    self.sum += self.array[x][y]
        self.score = self.sum * self.last_number_drawn


def generate_board(board):
    """
    generates an individual bingo board
    :param board: board in form of text
    :return: board as a instance of class Bingoboard
    """
    board = board.split('\n')
    total_list = []
    board_row = []
    for i in board:
        row = i.split(" ")

        for j in row:
            next if j == '' else board_row.append(int(j))
        total_list.append(board_row)  # stores the board here, appends the rows
        board_row = []

    matrix = np.array(total_list)  # converts it into a matrix
    return Bingoboard(matrix)


def generate_boards():
    """
    generates all bingo boards
    :return: list with all instances of boards
    """
    for i in range(1, len(txt)):  # goes through all boards
        board = generate_board(txt[i])
        list_board.append(board)
    return list_board


def check_winner(list_board):
    """
    checks the boards that are being completed and updates their attributes
    :param list_board: list of all boards in form of an instance
    """
    position = 1
    end = False
    for i in numbers_drawn:  # goes through numbers drawn
        if end: break
        for index, j in enumerate(list_board):  # goes through bingo boards
            if end: break
            aux = list_board[index].aux_array  # stores the auxiliary board of zeros
            break_out_loop = False
            for x in range(0, j.rows):
                if break_out_loop: break
                for y in range(0, j.columns):
                    if int(i) == j.array[x][y]:  # if the number drawn is in the board
                        aux[x][y] = 1  # store a 1 in the auxiliary board in that position
                        if (np.all(aux[x] == 1) or np.all(aux[:, y] == 1)) and j.position is None:
                            # if the column or the row is full of 1, end
                            print(f'The board {index+1} won!')
                            j.position = position  # store the finishing position in the board attribute
                            j.last_number_drawn = int(i)  # store the last number drawn in the board attribute
                            j.calculate_score()  # calculate score of each board, as an attribute
                            position += 1
                            if position > len(list_board):  # if all boards won
                                end = True
                                break_out_loop = True
                                break
                            break_out_loop = True
                            break


def retrieve_score(list_board, position):
    """
    retrieves a score for a certain board
    :param list_board: list of all boards
    :param position: finish position of the board
    :return: score
    """
    for x in list_board:
        if x.position == position:
            return x.score


def simulate_game():
    """
    simulates a game of bingo
    :return: list of boards after the game
    """
    list_board = generate_boards()
    check_winner(list_board)
    return list_board


def part1():
    list_board = simulate_game()
    score = retrieve_score(list_board, 1)
    return score


def part2():
    list_board = simulate_game()
    score = retrieve_score(list_board, len(list_board))
    return score


score = part1()
print(score)

