"""
Col test:
3 is confined to (rows 6-8; col 0).
Remove 3 as possibilities from (7,1) and (8,2).

6 is confined to (rows 3-5 ; col 1).
Remove 6 as possibilities from (rows 3-5; col 2).
"""


import sys
sys.path.append('../')
from sudoku_solver import *


sudoku = Sudoku_Solver()
sudoku.import_board("test_boards/ints_line_col.txt")
sudoku.print_board()
print('===============================')


# Testing steps
print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


print('Check line intersections:')
sudoku.check_intersection_lines()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


