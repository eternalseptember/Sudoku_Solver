"""
Intersection eliminations.

Col test 1:
7 can't be in any other (4, col) locations.
In the central box, 7 can only be in (3, 4) and (5, 4),
so eliminate 7 as a possibility in the rest of (row, 4).

Col test 2:
5 is in (0, 6) or (1, 6).
Remove 5 from (6, 6).

Col test 3:
1 is in (3, 2) or (5, 2).
Remove 1 from (rows 0-2; col 2) and (rows 6-8; col 2)


Row test 1:
7 can't be in any other (row, 4) locations.
In the central box, 7 can only be in (4, 3) and (4, 5),
so eliminate 7 as a possibility in the rest of (4, col).

Row test 2:
5 is in (2, 0) or (2, 1).
Remove 5 from (2, 6).

Row test 3:
1 is in (6, 3) or (6, 5).
Remove 1 from (row 6; cols 0-2) and (row 6; cols 6-8).
"""


import sys
sys.path.append('../')
from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
# sudoku.import_board("test_boards/ints_rm_out_box_col_1.txt")
# sudoku.import_board("test_boards/ints_rm_out_box_col_2.txt")
sudoku.import_board("test_boards/ints_rm_out_box_col_3.txt")
# sudoku.import_board("test_boards/ints_rm_out_box_row_1.txt")
# sudoku.import_board("test_boards/ints_rm_out_box_row_2.txt")
# sudoku.import_board("test_boards/ints_rm_out_box_row_3.txt")
sudoku.print_board()
print('===============================')


# Testing steps
print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
# sudoku.print_possible_values()
print('===============================')


"""
# Used for first set of tests
print('Check intersection in box:')
sudoku.check_intersection_box((4, 4))
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')
"""

print('Check intersection in box:')
sudoku.check_intersection_boxes()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')













