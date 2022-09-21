"""
Test file for puzzle_5.
Solved after checking for block-level eliminations and naked triples.
"""

import sys
sys.path.append('../')
from sudoku_solver import *


sudoku = Sudoku_Solver()
sudoku.import_board("test_boards/puzzle_5.txt")
sudoku.print_board()
print('===============================')


# Solve
print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
# sudoku.print_possible_values()
print('===============================')


print('Check matching sets:')
sudoku.check_naked_sets()
sudoku.print_board()
# sudoku.print_possible_values()
print('===============================')


print('Boxed intersection eliminations:')
sudoku.check_intersection_boxes()
sudoku.print_board()
# sudoku.print_possible_values()
print('===============================')


print('Double-box, block-level eliminations:')
sudoku.check_intersection_blocks()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


print('Check unique locations:')
sudoku.check_all_unique()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


print('Check for naked triples:')
sudoku.check_naked_triples()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')













