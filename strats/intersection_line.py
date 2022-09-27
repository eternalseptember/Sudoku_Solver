def check_intersection_lines(self):
    """
    Tally up possible values in each row or column.
    Then check if all possible locations for a missing value is in the same box.
    If it is, then remove it from the rest of the box.
    """
    print()



def check_intersection_rows(self):
    """
    Tally up all possible values in each row.
    """
    for row_step in range(9):
        row_missing_vals = {}

        # Collect list of missing values and their locations in this row.
        for col_step in range(9):
            this_cell = (row_step, col_step)
            self.set_lookup_table(this_cell, row_missing_vals)





def check_intersection_cols(self):
    return None


def check_intersection_row(self, coord):
    return None


def check_intersection_col(self, coord):
    return None










