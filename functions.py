# coding: utf8
from __future__ import print_function
import sys
import select
import os
import numpy
import random
__author__ = 'matheus'


def read_char():
    i, o, e = select.select([sys.stdin], [], [], 0.0001)
    for s in i:
        if s == sys.stdin:
            return sys.stdin.readline()[0]


def print_board(b):
    print('╔', end="")
    print('═' * 7, end="╦")
    print('═' * 7, end="╦")
    print('═' * 7, end="╗")
    print('')
    for i in range(9):
        if i == 3 or i == 6:
            print('╠', end="")
            print('═' * 7, end="╬")
            print('═' * 7, end="╬")
            print('═' * 7, end="╣")
            print("")
            print('║', end=" ")

        else:
            print('║', end=" ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print('║', end=" ")
            if b[i, j] == 0:
                print(" ", end=" ")
            else:
                print(b[i, j], end=" ")
        print('║')
    print('╚', end="")
    print('═' * 7, end="╩")
    print('═' * 7, end="╩")
    print('═' * 7, end="╝")
    print('')


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def find_first_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i, j] == 0:
                return i, j


def get_candidates(board, coordinate):
    x = coordinate[0]
    y = coordinate[1]
    candidates = range(1, 10)

    for i in range(9):
        if board[x, i] in candidates:
            candidates.remove(board[x, i])
        if board[i, y] in candidates:
            candidates.remove(board[i, y])

    if 0 <= x <= 2:
        square_x = 0
    elif 3 <= x <= 5:
        square_x = 3
    else:
        square_x = 6

    if 0 <= y <= 2:
        square_y = 0
    elif 3 <= y <= 5:
        square_y = 3
    else:
        square_y = 6

    for i in range(square_x, square_x + 3):
        for j in range(square_y, square_y + 3):
            # noinspection PyBroadException
            if board[i, j] in candidates:
                candidates.remove(board[i, j])

    return candidates


def solve(board, flag):
    if flag == "!info":
        return depth_first(board, None)
    elif flag == "info":
        return best_first(board)


def depth_first(board, candidates):
    element = find_first_empty(board)

    if not element:
        return True

    if candidates is None:
        candidates = get_candidates(board, element)

    while candidates:
        x = candidates.pop()
        board[element] = x
        # noinspection PyTypeChecker
        if depth_first(board, None):
            return True
        else:
            board[element] = 0
            return depth_first(board, candidates)
    return False


def read_board():
    string = sys.stdin.readline()

    while len(string) != 82:
        print("Please enter a 82 character string")
        string = sys.stdin.readline()

    string = string.replace('.', '0')
    string = string.strip()
    string = ';'.join([string[i:i + 9] for i in range(0, len(string), 9)])
    string = " ".join(string).replace(" ;", ";")

    return numpy.matrix(string)


past = []
# closed = numpy.zeros((9, 9, 5))


def best_first(board):
    el = find_first_empty(board)
    aux = board.copy()

    if not el:
        return True

    best = None
    candidates_best = [None] * 10

    while el:
        candidates = get_candidates(aux, el)
        if len(candidates) < len(candidates_best):
            candidates_best = candidates
            best = el
        aux[el] = -1
        el = find_first_empty(aux)

    if candidates_best:
        if len(candidates_best) > 1:
            x = candidates_best.pop()

            while x in closed[best]:
                x = candidates_best.pop()
            past.append(board.copy())
        else:
            x = candidates_best.pop()
        print(best)
        print(candidates_best)
        print(x)
        print_board(board)
        board[best] = x

        if best_first(board):
            return True
        else:
            numpy.append(closed[best], board[best])
            board[best] = 0
            return best_first(past.pop())

    return False
