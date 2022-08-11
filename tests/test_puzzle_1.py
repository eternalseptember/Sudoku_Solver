"""
Test file for puzzle_1.
Solved by checking all unique once.
"""

import sys
sys.path.append('../')
from sudoku_solver import *


sudoku = Sudoku_Solver()
sudoku.import_board("test_boards/puzzle_1.txt")
sudoku.print_board()
print('===============================')


# Solve
print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


print('Unique lookup test:')
sudoku.check_all_unique()
sudoku.print_board()
# sudoku.print_possible_values()
print('===============================')






