def check_intersection_lines(self):
    """
    Tally up possible values in each row or column.
    Then check if all possible locations for a missing value is in the same box.
    If it is, then remove it from the rest of the box.
    """
    # self.check_intersection_rows()
    self.check_intersection_cols()


def check_intersection_rows(self):
    """
    Tally up all possible values in each row.
    Then check if all possible locations for a missing value is in the same box.
    If it is, then remove it from the rest of the box.
    """
    for row_step in range(9):
        row_missing_vals = {}

        # Collect list of missing values and their locations in this row.
        for col_step in range(9):
            this_cell = (row_step, col_step)
            self.set_lookup_table(this_cell, row_missing_vals)





def check_intersection_cols(self):
    """
    Tally up all possible values in each col.
    Then check if all possible locations for a missing value is in the same box.
    If it is, then remove it from the rest of the box.
    """
    for col_step in range(9):
        col_missing_vals = {}

        # Collect list of missing values and their locations in this col.
        for row_step in range(9):
            this_cell = (row_step, col_step)
            self.set_lookup_table(this_cell, col_missing_vals)


        # Check if missing values are all located in the same box.
        for missing_val in col_missing_vals.keys():
            missing_val_locs = col_missing_vals[missing_val]

            # If there are more than 3 locations, then can't be in the same box.
            if len(missing_val_locs) <= 3:
                is_same_box, box_loc = self.in_which_box(missing_val_locs)

                if is_same_box:
                    # print('\tmissing val: {0}\tin col: {1}\tbox: {2}\tlocs:{3}'
                    # 	.format(missing_val, col_step, box_loc, missing_val_locs))
                    self.clean_box_with_col(missing_val, box_loc, col_step)







def clean_box_with_row(self, eliminated_val, ref_box, in_row):
    """
    eliminated_val is in in_row.
    Remove that possibility from the rest of the box, where row is not in_row.
    ref_box defines the 3x3 box.
    """
    ref_row, ref_col = ref_box

    for row_step in range(3):
        this_row = ref_row * 3 + row_step

        if this_row == in_row:
            # skip if this_row is in_row.
            continue
        
        for col_step in range(3):
            this_col = ref_col * 3 + col_step
            this_cell = (this_row, this_col)
            self.possible_vals_check(this_cell, eliminated_val)





def clean_box_with_col(self, eliminated_val, ref_box, in_col):
    """
    eliminated_val is in in_col.
    Remove that possibility from the rest of the box, where col is not in_col.
    ref_box defines the 3x3 box.
    """
    ref_row, ref_col = ref_box

    for col_step in range(3):
        this_col = ref_col * 3 + col_step

        if this_col == in_col:
            # skip if this_col is in_col.
            continue

        for row_step in range(3):
            this_row = ref_row * 3 + row_step
            this_cell = (this_row, this_col)
            self.possible_vals_check(this_cell, eliminated_val)

















