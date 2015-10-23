# coding: utf8
from functions import *
from time import time
from random import randint
import numpy
__author__ = 'matheus'
from termcolor import colored
import sys

board_easy_1 = numpy.matrix("0 7 8 1 0 0 0 2 0;"
                            "1 0 0 0 6 2 0 0 3;"
                            "5 0 0 0 9 0 0 0 0;"
                            "8 0 0 0 0 0 4 0 6;"
                            "0 6 1 0 7 0 0 9 0;"
                            "0 9 0 0 0 0 3 0 0;"
                            "0 0 0 5 0 4 2 0 7;"
                            "6 0 0 0 8 0 0 3 0;"
                            "0 5 0 7 0 0 9 0 0")

board_hard_1 = numpy.matrix("9 0 0 0 0 2 0 0 0;"
                            "0 5 0 8 6 9 7 1 4;"
                            "6 0 0 0 3 0 0 0 5;"
                            "0 2 4 0 0 0 0 0 0;"
                            "0 9 6 0 8 0 1 0 0;"
                            "0 0 0 7 0 6 0 4 0;"
                            "0 0 0 0 1 8 3 0 0;"
                            "0 0 0 3 0 0 0 0 2;"
                            "0 0 9 0 0 0 0 7 1")

# board = board_easy_1.copy()
# print_board(board)
# print solve(board, 'info')
# print_board(board)

board = read_board()
print_board(board)
print solve(board, 'info')
print_board(board)

#
# read_board()


# print_board(board_easy_1)
# past = int(time())
# while True:
#     c = read_char()
#     if c == "e":
#         quit(1)
#     if int(time()) - past >= 1:
#         past = int(time())
#         clear()
#         print_board(board)
#