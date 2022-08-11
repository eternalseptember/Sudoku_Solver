"""
Test file for puzzle_6.
"""

import sys
sys.path.append('../')
from sudoku_solver import *


sudoku = Sudoku_Solver()
sudoku.import_board("test_boards/puzzle_6.txt")
sudoku.print_board()
print('===============================')


# Solve
print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
# sudoku.print_possible_values()
print('===============================')


# board values found
print('Unique lookup test:')
sudoku.check_all_unique()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


# board values found and possible values list has been reduced
print('Single-box block-level eliminations:')
sudoku.check_within_boxes()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


# possible values list has been reduced
print('Double-boxed block-level eliminations:')
sudoku.check_block_elim()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


# board values found and possible values list has been reduced
print('Check unique locations:')
sudoku.check_all_unique()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


# poss vals list reduced for one location
print('Single-box block-level eliminations:')
sudoku.check_within_boxes()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')
































