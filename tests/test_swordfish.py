"""
    swordfish_1 (perfect)
Candidate: 8
(1, 0), (1, 4), (1, 6)
(2, 0), (2, 4), (2, 6)
(3, 0), (3, 4), (3, 6)

Remove 8 as a possible value from:
(1, 1), (1, 7)
(2, 1), (2, 8)
(3, 5)

    swordfish_2 (2-2-2 formation)
Candidate: 9
(2, 1), (2, 4), (2, 7)
(6, 1), (6, 4), (6, 7)
(8, 1), (8, 4), (8, 7)

Remove 9 as a possible value from:
(2, 3), (2, 5)
(6, 6)
(8, 3), (8, 5), (8, 6)
"""


import sys
sys.path.append('../')
from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
# sudoku.import_board("test_boards/swordfish_1.txt")
sudoku.import_board("test_boards/swordfish_2.txt")  # 2-2-2 swordfish
# sudoku.import_board("test_boards/swordfish_3.txt")  # 2-2-2 swordfish
# sudoku.import_board("test_boards/swordfish_4.txt")  # 2-2-2 swordfish
sudoku.print_board()
print('===============================')


print('Init reduce:')
sudoku.solve_queue()
# sudoku.print_board()
# sudoku.print_possible_values()
# print('===============================')


# board prep for swordfish_2
# hidden subset is incomplete, so calling functions individually.
sudoku.check_naked_sets()
sudoku.check_hidden_sub_cols()
sudoku.check_hidden_sub_rows()
sudoku.check_hidden_sub_boxes()


sudoku.print_board()
sudoku.print_possible_values()
print('===============================')






print('Check swordfish:')
sudoku.check_swordfish()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')








