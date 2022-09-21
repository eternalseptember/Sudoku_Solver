def check_intersections(self):
    """
    Functions that eliminate possibilities based on row/box/col intersections.
    """
    self.check_intersection_boxes()
    self.check_intersection_blocks()



def check_intersection_boxes(self):
    """
    Check all nine boxes.
    Within each 3x3 box, tally up whether unfilled values fit in a row or col.
    If so, then eliminate them as possibilities from neighboring boxes.
    """
    for row_step in [0, 3, 6]:
        for col_step in [0, 3, 6]:
            coord = (row_step, col_step)
            self.check_intersection_box(coord)
            self.solve_queue()



def check_intersection_box(self, coord):
    """
    coord defines the 3x3 box.
    Check ONE box to see whether missing values can be narrowed down to a
    specific row.
    """
    # Get the list of missing values and their possible locations in this box.
    poss_vals_in_box = self.get_box_poss_vals(coord)

    # For each missing value, analyze the list of their possible locations.
    for missing_val in poss_vals_in_box.keys():
        poss_locs_list = poss_vals_in_box[missing_val]

        # Are they in the same row?
        in_rows_list = self.in_which_rows(poss_locs_list)

        # If missing_val can only be in one row within this box, then remove
        # missing_val as possibilities in the rest of the row outside this box.
        if len(in_rows_list) == 1:
            self.clean_row_outside_box(missing_val, coord, in_rows_list[0])


        # Are they in the same col?
        in_cols_list = self.in_which_cols(poss_locs_list)

        # If missing_val can only be in one col within this box, then remove
        # missing_val as possibilities in the rest of the col outside this box.
        if len(set(in_cols_list)) == 1:
            self.clean_col_outside_box(missing_val, coord, in_cols_list[0])



def in_which_rows(self, coords_list):
    """
    In which rows could the cells be in?
    """
    rows = []

    # Unpack and tally rows here.
    for coord in coords_list:
        row, col = coord
        rows.append(row)

    # Not useful if it returns 3.
    return list(set(rows))



def in_which_cols(self, coords_list):
    """
    In which cols could the cells be in?
    """
    cols = []

    # Unpack and tally cols here.
    for coord in coords_list:
        row, col = coord
        cols.append(col)

    # Not useful if it returns 3.
    return list(set(cols))



def clean_row_outside_box(self, eliminated_val, ref_box, in_row):
    """
    eliminated_val is the value to be removed.
    ref_box defines the 3x3 box.
    """
    ref_row, ref_col = ref_box
    box_col = ref_col // 3  # Remove in row outside this box.

    for col_step in range(9):
        # Skip the box with coord.
        if col_step // 3 == box_col:
            continue

        # Remove eliminated_val as a possible val in this cell.
        this_cell = (in_row, col_step)
        self.possible_vals_check(this_cell, eliminated_val)



def clean_col_outside_box(self, eliminated_val, ref_box, in_col):
    """
    eliminated_val is the value to be removed.
    ref_box defines the 3x3 box.
    """
    ref_row, ref_col = ref_box
    box_row = ref_row // 3  # Remove in col outside this box.

    for row_step in range(9):
        # Skip the box with coord.
        if row_step // 3 == box_row:
            continue

        # Remove eliminated_val as a possible val in this cell.
        this_cell = (row_step, in_col)
        self.possible_vals_check(this_cell, eliminated_val)




















