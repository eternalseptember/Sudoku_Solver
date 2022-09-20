"""
#
# HAVE SOLUTION
#
HIDDEN SUBSET COL 1:
[1,9] can only be in (4,8) and (6,8).

HIDDEN SUBSET ROW 1:
[4,7] can only be in (0,0) and (0,1).
Can be solved by adding solve_queue() to functions.

HIDDEN SUBSET BOX 1:
[1,8] can only be in (4,3) and (4,5).


#
# TESTS STILL GETTING WORKED ON
#
HIDDEN SUBSET COL 2: (hidden triple) (NEW)
[1,3, ???] can only be in (3,4), (5,4), and (7,4).
is 9 part of the triple?

HIDDEN SUBSET ROW 2: (hidden triple) (NEW) (CURRENTLY TESTING)
[1,2,6] can only be in (4,0), (4,5), and (4,7).

HIDDEN SUBSET TRIP 1: (NEW) (VERY HARD)
???

HIDDEN SUBSET QUAD 1:
???
"""


import sys
sys.path.append('../')
from sudoku_solver import *


sudoku = Sudoku_Solver()
# sudoku.import_board("test_boards/hidden_sub_col_1.txt")
# sudoku.import_board("test_boards/hidden_sub_row_1.txt")
# sudoku.import_board("test_boards/hidden_sub_box_1.txt")

# sudoku.import_board("test_boards/hidden_sub_col_2.txt")
sudoku.import_board("test_boards/hidden_sub_row_2.txt")
# sudoku.import_board("test_boards/hidden_sub_quad_1.txt")
# sudoku.import_board("test_boards/hidden_sub_trip_1.txt")
sudoku.print_board()
print('===============================')


# Testing steps
print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')




# Preliminary reduction of board candidates for hidden_sub_row_2.txt
print('Getting to the point where the test follows the example:')

# [2] can only be at (6,1) and (8,1). Remove [2] from the rest of col 1.
print('check intersection')
sudoku.check_intersection_boxes()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')
# Reducing possible values list.
print('check naked subsets')
sudoku.check_naked_sets()
sudoku.check_naked_sets()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')
# Trying to eliminate [1] at (4,2) and (4,3) (test row) and (7,2) (to match example).




print('Find hidden subset:')
sudoku.check_hidden_subsets()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')










