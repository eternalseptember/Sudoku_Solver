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



def in_which_box_row(self):
    return None



def in_which_box_col(self):
    return None














