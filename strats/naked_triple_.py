def check_naked_triples(self):
    """
    Checks for naked triples in rows, cols, and boxes.

    Naked triple:
    Not all cells must contain all three candidates, but there must not be more
    than three candidates in the three cells all together.
    """
    self.check_naked_trips_rows()
    self.check_naked_trips_cols()



def check_naked_trips_rows(self):
    """
    Iterate through each row to find naked triples.
    Collect candidate cells and their possibilities.
    """
    for row_step in range(9):
        poss_trip_list = []

        # Get a list of cells that can be part of a triple.
        for col_step in range(9):
            this_cell = (row_step, col_step)

            # Skip over solved cells.
            if this_cell in self.possible_values:
                poss_vals = self.possible_values[this_cell]

                # Can't be part of a triple if there are more than 3 candidates.
                if len(poss_vals) <= 3:
                    poss_trip_list.append(this_cell)

        # Analyze if triple exists.
        poss_trips_info = self.find_naked_triples(poss_trip_list, 'check_row')

        if len(poss_trips_info) > 0:
            self.clean_trips_row(poss_trips_info, row_step)
            self.solve_queue()



def clean_trips_row(self, poss_trips_info, row_num):
    """
    Remove trip possibilities in cells that are not part of the triple.
    """
    for item in poss_trips_info.keys():

        # Decode key and turn it back into a list of numbers.
        trip_set = [int(trip_val) for trip_val in item]
        coords_set = poss_trips_info[item]

        # Remove trip values from cells not part of triple.
        for col_step in range(9):
            this_cell = (row_num, col_step)

            # Skip over cells that are part of this triple.
            if this_cell not in coords_set:

                # Remove vals in trip_set from this_cell's possible vals.
                # Then check if this_cell has been solved.
                for trip_val in trip_set:
                    self.possible_vals_check(this_cell, trip_val)



def check_naked_trips_cols(self):
    """
    Iterate through each col to find naked triples.
    Collect candidate cells and their possibilities.
    """
    for col_step in range(9):
        poss_trip_list = []

        # Get a list of cells that can be part of a triple.
        for row_step in range(9):
            this_cell = (row_step, col_step)

            # Skip over solved cells.
            if this_cell in self.possible_values:
                poss_vals = self.possible_values[this_cell]

                # Can't be part of a triple if there are more than 3 candidates.
                if len(poss_vals) <= 3:
                    poss_trip_list.append(this_cell)

        # Analyze if triple exists.
        poss_trips_info = self.find_naked_triples(poss_trip_list, 'check_col')

        if len(poss_trips_info) > 0:
            self.clean_trips_col(poss_trips_info, col_step)
            self.solve_queue()



def clean_trips_col(self, poss_trips_info, col_num):
    """
    Remove trip possibilities in cells that are not part of the triple.
    """
    for item in poss_trips_info.keys():

        # Decode key and turn it back into a list of numbers.
        trip_set = [int(trip_val) for trip_val in item]
        coords_set = poss_trips_info[item]

        # Remove trip values from cells not part of triple.
        for row_step in range(9):
            this_cell = (row_step, col_num)

            # Skip over cells that are part of this triple.
            if this_cell not in coords_set:

                # Remove vals in trip_set from this_cell's possible vals.
                # Then check if this_cell has been solved.
                for trip_val in trip_set:
                    self.possible_vals_check(this_cell, trip_val)


















