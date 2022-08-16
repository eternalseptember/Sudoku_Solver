# Checks naked triples in rows, cols, and boxes.

# Naked triple:
# Not all cells must contain all three candidates, but there must not be more
# than three candidates in the three cells all together.



def check_naked_triples(self):
    self.check_naked_triples_rows()
    # self.check_naked_triples_cols()



def check_naked_triples_rows(self):
    # Iterate through each row to find naked triples.
    for j in range(9):  # j is row number
        self.check_naked_triples_row(j)



def check_naked_triples_row(self, row_num):
    # Collect candidate cells and their possibilities.
    poss_trip_list = []

    # Get a list of cells that can be part of a triple.
    for i in range(9):  # i is col number
        this_cell = (row_num, i)

        # Skip over solved cells.
        if this_cell in self.possible_values:
            poss_vals = self.possible_values[this_cell]

            # Can't be part of a triple if there are more than 3 candidates.
            if len(poss_vals) <= 3:
                poss_trip_list.append(this_cell)

    # Analyze if triple exists.
    poss_trips_info = self.find_naked_triples(poss_trip_list, 'check_row')

    if len(poss_trips_info) > 0:
        self.clean_triple_row(poss_trips_info, row_num)
        self.solve_queue()



def clean_triple_row(self, poss_trips_info, row_num):
    # Remove trip possibilities in cells that are not part of the triple.
    for item in poss_trips_info.keys():

        # Decode key and turn it back into a list of numbers.
        trip_set = [int(trip_val) for trip_val in item]
        coords_set = poss_trips_info[item]

        # Remove trip values from cells not part of triple.
        for i in range(9):  # i is col number
            this_cell = (row_num, i)

            # Skip over cells that are part of this triple.
            if this_cell not in coords_set:
                if this_cell in self.possible_values:

                    # Remove vals in trip_set from this cell's possible vals.
                    poss_vals = self.possible_values[this_cell]

                    for trip_val in trip_set:
                        if trip_val in poss_vals:
                            poss_vals.remove(trip_val)

                    # Then check if this_cell has been solved.
                    self.check_if_solved(this_cell, poss_vals)







def check_naked_triples_cols(self):
    # Iterate through each col to find naked triples.
    for i in range(9):  # i is col number
        self.check_naked_triples_col(i)



def check_naked_triples_col(self, col_num):
    # Collect candidate cells and their possibilities.
    poss_trip_list = []

    # Get a list of cells that can be part of a triple.
    for j in range(9):
        this_cell = (j, col_num)

        # Skip over solved cells.
        if this_cell in self.possible_values:
            poss_vals = self.possible_values[this_cell]

            # Can't be part of a triple if there are more than 3 candidates.
            if len(poss_vals) <= 3:
                poss_trip_list.append(this_cell)

    # Analyze if triple exists.
    poss_trips_info = self.find_naked_triples(poss_trip_list, 'check_col')
    self.clean_triple_col(poss_trips_info, col_num)
    self.solve_queue()



def clean_triple_col(self, poss_trips_info, col_num):
    # Remove trip possibilities in cells that are not part of the triple.
    for item in poss_trips_info.keys():

        # Decode key and turn it back into a list of numbers.
        trip_set = [int(trip_val) for trip_val in item]
        coords_set = poss_trips_info[item]

        # Remove trip values from cells not part of triple.
        for j in range(9):  # j is row number
            this_cell = (j, col_num)

            # Skip over cells that are part of this triple.
            if this_cell not in coords_set:
                if this_cell in self.possible_values:

                    # Remove vals in trip_set from this cell's possible vals.
                    poss_vals = self.possible_values[this_cell]

                    for trip_val in trip_set:
                        if trip_val in poss_vals:
                            poss_vals.remove(trip_val)

                    # Then check if this_cell has been solved.
                    self.check_if_solved(this_cell, poss_vals)



















