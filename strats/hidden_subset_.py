def check_hidden_subsets(self):
    """
    Like naked subset, except there are other candidates in the same cells.
    """
    # self.check_hidden_sub_cols()
    self.check_hidden_sub_rows()
    # self.check_hidden_sub_boxes()



def check_hidden_sub_cols(self):
    """
    Searches for hidden subsets in every col.
    """
    # Gets list of possible values for each location.
    for col_step in range(9):
        col_missing_vals = {}  # list of missing values in this col

        for row_step in range(9):  # row goes down. col is constant.
            this_cell = (row_step, col_step)
            self.set_lookup_table(this_cell, col_missing_vals)

        # Find any subsets and then clean col.
        possible_subsets = self.format_hidden_subset_info(col_missing_vals)
        self.find_hidden_subset(possible_subsets, 'col')
        # self.solve_queue()  # uncomment after testing



def check_hidden_sub_rows(self):
    """
    Searches for hidden subsets in every row.
    """
    # Gets list of possible values for each location.
    test_row = [4]  # testing

    for row_step in test_row:  # iterate down rows.
        row_missing_vals = {}  # list of missing values in this row

        for col_step in range(9):  # col goes across. row is constant.
            this_cell = (row_step, col_step)
            self.set_lookup_table(this_cell, row_missing_vals)

        # Find any subsets and then clean row.
        possible_subsets = self.format_hidden_subset_info(row_missing_vals)


        # testing
        for item in possible_subsets.keys():
            print('{0} - {1}'.format(item, possible_subsets[item]))


        self.find_hidden_subset(possible_subsets, 'row')
        # self.solve_queue()  # uncomment after testing




def check_hidden_sub_boxes(self):
    """
    Searches for hidden subsets in all 3x3 boxes.
    """
    # Gets list of possible values in each location.
    for row_step in [0, 3, 6]:
        for col_step in [0, 3, 6]:
            box_coord = (row_step, col_step)
            self.check_hidden_sub_box(box_coord)



def check_hidden_sub_box(self, box_coord):
    """
    Searches for hidden subsets within ONE 3x3 box.
    """
    ref_row, ref_col = box_coord
    box_missing_vals = {}  # list of missing values in this box

    for row_step in range(3):
        for col_step in range(3):
            this_cell = (ref_row + row_step, ref_col + col_step)
            self.set_lookup_table(this_cell, box_missing_vals)

    # Find any subsets and then clean box.
    possible_subsets = self.format_hidden_subset_info(box_missing_vals)
    self.find_hidden_subset(possible_subsets, 'box', box_coord)
    # self.solve_queue()  # uncomment after testing


























