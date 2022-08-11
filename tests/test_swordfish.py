"""
Swordfish candidate: 8
(1, 0), (1, 4), (1, 6)
(2, 0), (2, 4), (2, 6)
(3, 0), (3, 4), (3, 6)


Remove 8 as a possible value from
(1, 1), (1, 7)
(2, 1), (2, 8)
(3, 5)
"""


import sys
sys.path.append('../')
from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
sudoku.import_board("test_boards/swordfish.txt")
sudoku.print_board()
print('===============================')


print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


# hidden pair here to reduce the possibilities list some more?


print('Check swordfish:')
sudoku.check_swordfish()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')








