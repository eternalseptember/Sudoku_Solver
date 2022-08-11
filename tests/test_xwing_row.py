"""
	xwing_row_test_1:
7 is locked to rows [1, 5] and cols [3, 7].
7 as a possible value is removed from:
	(0, 3)
	(4, 3)
	(7, 3) and (7, 7)
	(8, 3) and (8, 7)


	xwing_col_test_1:
2 is only in rows [4, 8] and cols [4, 7].
2 as a possible value is removed from:
	(4, 1); (4, 2); (4, 6); (4, 8)
	(8, 3) and (8, 8)

3 is only in rows [4, 8] and cols [1, 7].
3 as a possible value is removed from:
	(row 4; cols 0, 2, 6, 8)
	(row 8; cols 2, 3, 5, 8)
"""


import sys
sys.path.append('../')
from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
sudoku.import_board("test_boards/xwing_row_test_1.txt")
# sudoku.import_board("test_boards/xwing_col_test_1.txt")
sudoku.print_board()
print('===============================')


# Testing steps
print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


print('Check xwing:')
sudoku.check_xwing()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


"""
print('Check xwing again:')
sudoku.check_xwing()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')
"""







