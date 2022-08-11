"""
#
# HAVE SOLUTION
#
HIDDEN SUBSET COL 1:
[1,9] can only be in (4,8) and (6,8).

HIDDEN SUBSET ROW 1:
[4,7] can only be in (0,0) and (0,1).

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
sudoku.import_board("test_boards/hidden_sub_col_2.txt")
# sudoku.import_board("test_boards/hidden_sub_row_1.txt")
# sudoku.import_board("test_boards/hidden_sub_row_2.txt")
# sudoku.import_board("test_boards/hidden_sub_box_1.txt")
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

"""
# preliminary cleaning of board candidates for hidden_sub_row_2.txt
print('Getting to the point where the test follows the example:')
sudoku.check_matching_sets()  # naked_subset
sudoku.check_matching_sets()  # naked_subset
sudoku.check_within_boxes()  # intersection elim

sudoku.print_board()
sudoku.print_possible_values()
print('===============================')
"""


print('Find hidden subset:')
sudoku.check_hidden_subsets()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')










