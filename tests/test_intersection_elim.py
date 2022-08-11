"""
Intersection eliminations.

BLOCK ELIM ROWS:
In the central row of boxes:
8 can't be in (row 3; cols 2-3) and (row 5; cols 2-3).
8 can only be in (row 3; cols 0-1, 4-5) and (row 5; cols 0-1, 4-5).


So in the third box:
8 can only be in (row 4; cols 6-8).
Eliminate 8 from (row 3; cols 6-8) and (row 5; cols 6-8).


BLOCK ELIM COLS:
In the top two rows:
8 can't be in (rows 2 and 3).

In the middle box of the last row:
8 can only be in (rows 6-8; col 4).
Eliminate 8 from (rows 6-8; col 3) and (rows 6-8; col 5).
"""

import sys
sys.path.append('../')
from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
# sudoku.import_board("test_boards/block_elim_row.txt")
sudoku.import_board("test_boards/block_elim_col.txt")
sudoku.print_board()
print('===============================')


# Testing steps
print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
# sudoku.print_possible_values()
print('===============================')


print('Intersection eliminations:')
sudoku.check_within_boxes()
sudoku.check_block_elim()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')





