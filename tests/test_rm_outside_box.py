"""
Intersection eliminations.

Col test:
7 can't be in any other (4, col) locations.
In the central box, 7 can only be in (3, 4) and (5, 4),
so eliminate 7 as a possibility in the rest of (row, 4).

Row test:
7 can't be in any other (row, 4) locations.
In the central box, 7 can only be in (4, 3) and (4, 5),
so eliminate 7 as a possibility in the rest of (4, col).
"""

import sys
sys.path.append('../')
from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
sudoku.import_board("test_boards/rm_outside_box_row.txt")
# sudoku.import_board("test_boards/rm_outside_box_col.txt")
sudoku.print_board()
print('===============================')


# Testing steps
print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
# sudoku.print_possible_values()
print('===============================')


print('Check within box:')
sudoku.check_within_a_box((4, 4))
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')










