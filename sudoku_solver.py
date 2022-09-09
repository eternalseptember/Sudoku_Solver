# The main function for solving a puzzle.
# Input a formatted file with a sudoku puzzle.


class Sudoku_Solver():
    from sudoku_print import print_board, print_possible_values, \
        print_solved_queue

    from sudoku_unique import check_all_unique, check_unique_row, \
        check_unique_col, check_unique_box, get_box_poss_vals, \
        set_lookup_table, solve_lookup_table

    from strats.naked_subset import check_naked_sets, check_naked_cols, \
        check_naked_rows, set_missing_val_table, find_matches, \
        in_same_box, remove_in_box, clean_naked_sets, check_naked_boxes, \
        check_naked_box

    from strats.intersection_elim import check_intersections, \
        check_intersection_boxes, check_intersection_box, in_which_rows, \
        in_which_cols, clean_row_outside_box, clean_col_outside_box, \
        clean_rows_in_box, clean_cols_in_box, check_block_elim

    from strats.hidden_subset import check_hidden_subsets, \
        check_hidden_sub_cols, check_hidden_sub_rows, check_hidden_sub_boxes, \
        check_hidden_sub_box, clean_hidden_col, clean_hidden_row, \
        clean_hidden_box, clean_hidden_subset, format_hidden_subset_info, \
        find_hidden_subset

    from strats.naked_triples import check_naked_triples, \
        check_naked_trips_rows, check_naked_trips_row, clean_trips_row, \
        check_naked_trips_cols, check_naked_trips_col, clean_trips_col

    from strats.naked_triples_util import find_naked_triples, \
        verify_triples_list, check_naked_trips_box, clean_trips_boxes, \
        clean_trips_box

    from strats.xwing_row import check_xwing, check_xw_by_rows, \
        check_xw_cands, clean_xw_list, check_xw_is_same_cols, \
        is_xwing_same_cols, clean_xw_col

    from strats.xwing_col import check_xw_by_cols, check_xw_is_same_rows, \
        is_xwing_same_rows, clean_xw_row

    from strats.swordfish import check_swordfish, check_sf_cands, \
        clean_sf_list, find_swordfish, clean_swordfish, intersection







    def __init__(self):
        self.input = None
        self.board = self.create_board()
        self.possible_values = {}  # {(row, col): [possible values]}
        self.solved_list = []
        self.solved_queue = []


    def create_board(self):
        """
        Creates a blank board upon creation of class.
        """
        board = [
            ['-' for col in range(9)] for row in range(9)
            ]
        return board


    def import_board(self, file_name):
        """
        Import sudoku puzzle from a text file, then update game states.
        """
        board_file = open(file_name, 'r')
        board_import = board_file.readlines()
        board_file.close()

        for row in range(9):
            board_line = board_import[row].rstrip()
            for col in range(9):
                cell_value = board_line[col]

                if cell_value == '-':
                    self.possible_values[(row, col)] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                else:
                    self.board[row][col] = int(cell_value)
                    self.possible_values[(row, col)] = [int(cell_value)]
                    self.solved_queue.append((row, col))


    def solve_queue(self):
        """
        solved_value is a reduced list after the first pass.
        """
        while len(self.solved_queue) > 0:
            solved_cell = self.solved_queue.pop()
            self.resolve(solved_cell)


    def resolve(self, coord):
        """
        Assign solved value to board and clean up lists.
        """
        self.solved_list.append(coord)

        row, col = coord
        solved_value = self.possible_values.pop(coord)
        # print('coord: {0} solved value: {1}'.format(coord, solved_value))
        self.board[row][col] = solved_value[0]  # Set the value on the board.
        self.remove_num(coord, solved_value[0])


    def remove_num(self, coord, solved_value):
        """
        After a number on the board has been filled in, remove it as a
        possibility in all affected areas.
        """
        self.remove_num_in_row(coord, solved_value)
        self.remove_num_in_col(coord, solved_value)
        self.remove_num_in_box(coord, solved_value)


    def remove_num_in_row(self, coord, solved_value):
        """
        Remove solved_value from the list of possible values of
        other unsolved cells in this row.
        """
        ref_row, ref_col = coord  # reference cell

        for col_step in range(9):
            if col_step != ref_col:
                this_cell = (ref_row, col_step)
                self.possible_vals_check(this_cell, solved_value)


    def remove_num_in_col(self, coord, solved_value):
        """
        Remove solved_value from the list of possible values of
        other unsolved cells in this col.
        """
        ref_row, ref_col = coord  # reference cell

        for row_step in range(9):
            if row_step != ref_row:
                this_cell = (row_step, ref_col)
                self.possible_vals_check(this_cell, solved_value)


    def remove_num_in_box(self, coord, solved_value):
        """
        Remove solved_value from the list of possible values of
        other unsolved cells in this box.
        """
        ref_row, ref_col = coord  # reference cell

        # Possible values: 0, 1, 2
        box_row = ref_row // 3
        box_col = ref_col // 3

        # Iterate through one box.
        for row_step in range(3):
            for col_step in range(3):
                row = box_row * 3 + row_step
                col = box_col * 3 + col_step
                this_cell = (row, col)
                self.possible_vals_check(this_cell, solved_value)


    def possible_vals_check(self, coord, solved_value):
        """
        Check if there is a stored list of possible values in this coord.
        If there isn't, then this location has been solved.
        Otherwise, remove solved_value as a possible choice in this coord.
        Then check if this coord has been solved.
        """
        if coord in self.possible_values:
            poss_vals = self.possible_values[coord]

            if solved_value in poss_vals:
                poss_vals.remove(solved_value)

            self.check_if_solved(coord, poss_vals)


    def check_if_solved(self, coord, poss_vals):
        """
        Check if this coord has been solved.
        It's assumed that this function is executed after doing some
        comparisons and assignments with poss_vals.
        Add to solved queue if only one possible value is remaining.
        """
        if len(poss_vals) == 1:
            if (coord not in self.solved_list) and \
                (coord not in self.solved_queue):
                self.solved_queue.append(coord)

                # print('added to solved queue: {0}'.format(coord))


    def solve(self, coord):
        """
        To MANUALLY resolve one individual cell.
        """
        self.resolve(coord)
        self.solve_queue()




















