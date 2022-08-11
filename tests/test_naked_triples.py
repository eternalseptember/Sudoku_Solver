"""
Naked triple: 
Not all cells must contain all three candidates, but there must not be more
than three candidates in the three cells all together.

TRIPLE ROW 1:
[5,8,9] can only be in (4,3), (4,4), and (4,5);
	but some numbers are missing in (4,4) and (4,5).

TRIPLE COL 1:
[5,8,9] can only be in (3,4), (4,4), and (5,4);
	but some numbers are missing in (4,4) and (5,4).\


TRIPLE ROW 2:
[1,5,8] can only be in row 0.
[2,3,8] can only be in row 8.
(7,3) should be [9].


TRIPLE COL 2:
[1,5,8] can only be in col 0.
[2,3,8] can only be in col 8.
Clear them from the rest of their boxes.
(5,7) should be [9].
"""

import sys
sys.path.append('../')
from sudoku_solver import *


sudoku = Sudoku_Solver()
# sudoku.import_board("test_boards/naked_triple_row_1.txt")
# sudoku.import_board("test_boards/naked_triple_col_1.txt")
sudoku.import_board("test_boards/naked_triple_row_2.txt")
# sudoku.import_board("test_boards/naked_triple_col_2.txt")
sudoku.print_board()
print('===============================')


# Testing steps
print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')




print('Check for naked triples:')
sudoku.check_naked_triples()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')












