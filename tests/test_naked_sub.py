"""
Testing smaller functions for eliminating based on matched pairs.

COL:
[4,7] can only be in (0,0) and (4,0).
Remove [4,7] from the rest of the col, leaving 
	[1] in (1,0);
	[2] in (5,0);
	[6] in (3,0)

ROW:
[4,7] can only be in (0,4) and (0,8).
Remove [4,7] from the rest of the col, leaving 
	[1] in (0,7);
	[2] in (0,3);
	[6] in (0,5)
"""

import sys
sys.path.append('../')
from sudoku_solver import *


sudoku = Sudoku_Solver()
# sudoku.import_board("test_boards/naked_sub_col.txt")
sudoku.import_board("test_boards/naked_sub_row.txt")
sudoku.print_board()
print('===============================')


# Testing steps
print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
# sudoku.print_possible_values()
print('===============================')


print('Check matching sets:')
sudoku.check_matching_sets()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')







