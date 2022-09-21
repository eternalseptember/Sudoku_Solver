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


# Board values found.
print('Unique lookup test:')
sudoku.check_all_unique()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


# Board values found and poss vals have been reduced.
print('Boxed intersection eliminations:')
sudoku.check_intersection_boxes()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


# Poss vals have been reduced.
print('Double-box, block-level eliminations:')
sudoku.check_intersection_blocks()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


# Board values found and poss vals have been reduced.
print('Check unique locations:')
sudoku.check_all_unique()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


# Poss vals reduced for one location.
print('Boxed intersection eliminations:')
sudoku.check_intersection_boxes()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')
































