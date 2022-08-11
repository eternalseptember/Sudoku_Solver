"""
Test file for puzzle_3.
Solved by checking all unique twice.
"""

import sys
sys.path.append('../')
from sudoku_solver import *


sudoku = Sudoku_Solver()
sudoku.import_board("test_boards/puzzle_3.txt")
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






