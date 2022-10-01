def check_naked_sets(self):
    """
    Eliminate possibilities based on matching pairs (or triplets).
    Focused on finding pairs. Triplets can be found incidentally.
    Naked: EXACT list of candidates in EXACT cells.
    """
    self.check_naked_cols()
    self.check_naked_rows()
    self.check_naked_boxes()



def check_naked_cols(self):
    """
    Search each col for matching pairs/triplets.
    """
    for col_step in range(9):
        col_missing_vals = {}

        # Collect all the missing value combinations in this col.
        for row_step in range(9):
            this_cell = (row_step, col_step)
            self.set_missing_val_table(this_cell, col_missing_vals)

        # Search this col's tally for pair/triplet matches.
        matches_vals, matches_locs = self.find_matches(col_missing_vals)

        # If there are matching sets, remove values as possibilities in other
        # boxes outside the set/pair/triplet.
        if len(matches_vals) > 0:
            for match in matches_vals:
                # Reduce within col.
                for row_step in range(9):
                    this_cell = (row_step, col_step)
                    self.clean_naked_sets(this_cell, match, 'col')

                # Reduce within box.
                self.remove_naked_in_box(match, matches_locs)

            # If anything's been reduced to one possibility:
            self.solve_queue()



def check_naked_rows(self):
    """
    Search each row for matching pairs/triplets.
    """
    for row_step in range(9):
        row_missing_vals = {}

        # Collect all the missing value combinations in this row.
        for col_step in range(9):
            this_cell = (row_step, col_step)
            self.set_missing_val_table(this_cell, row_missing_vals)

        # Search this row's tally for pair/triplet matches.
        matches_vals, matches_locs = self.find_matches(row_missing_vals)

        # If there are matching sets, remove values as possibilities in other
        # boxes outside the set/pair/triplet.
        if len(matches_vals) > 0:
            for match in matches_vals:
                # Reduce within row.
                for col_step in range(9):
                    this_cell = (row_step, col_step)
                    self.clean_naked_sets(this_cell, match, 'row')

                # Reduce within box.
                self.remove_naked_in_box(match, matches_locs)

            # If anything's been reduced to one possibility:
            self.solve_queue()



def check_naked_boxes(self):
    """
    Search a box for naked pairs that may not be on the same row or col.
    """
    for row_step in [0, 3, 6]:
        for col_step in [0, 3, 6]:
            coord = (row_step, col_step)
            self.check_naked_box(coord)



def check_naked_box(self, coord):
    """
    Search within box for a naked pair/triplet.
    coord defines the 3x3 box.
    """
    ref_row, ref_col = coord
    box_row = ref_row // 3
    box_col = ref_col // 3
    box_missing_vals = {}

    # Collect all the missing value combinations in this box.
    for row_step in range(3):
        for col_step in range(3):
            this_row = box_row * 3 + row_step
            this_col = box_col * 3 + col_step
            this_cell = (this_row, this_col)

            self.set_missing_val_table(this_cell, box_missing_vals)

    # Search for pair/triplet matches.
    matches_vals, matches_locs = self.find_matches(box_missing_vals)

    # If there are matching sets, remove those vals as poss_vals from the rest of the box.
    if len(matches_vals) > 0:
        for match in matches_vals:
            self.remove_naked_in_box(match, matches_locs)
        
        # Then check if cells have only one poss_val remaining.
        self.solve_queue()


























