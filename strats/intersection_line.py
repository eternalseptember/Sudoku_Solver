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
                    print('missing val: {0}\tbox: {1}\tlocs:{2}'
                        .format(missing_val, box_loc, missing_val_locs))







def clean_box_with_row(self, eliminated_val, ref_box, in_row):
    return None





def clean_box_with_col(self, eliminated_val, ref_box, in_col):
    return None

















