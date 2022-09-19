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
    for row_step in range(9):  # iterate down rows.
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




def find_hidden_subset(self, subset_info, label, box_coord=None):
    """
    Searches for hidden subsets within a single row, col, or box.
    Then clean possibilities according to label mode.
    label mode is 'row', 'col', or 'box'.
    """
    for poss_key in subset_info.keys():
        item = subset_info[poss_key]
        subset_locs = item['subset_locs']
        subset_nums = item['missing_num']

        # Hidden subset identified.
        if len(subset_nums) == len(subset_locs):

            # testing
            print('\tmode: {0}\thidden subset: {1}\t\tlocations: {2}'
                .format(label, subset_nums, subset_locs))

            if label == 'col':
                self.clean_hidden_col(subset_locs, subset_nums)
            elif label == 'row':
                self.clean_hidden_row(subset_locs, subset_nums)
            elif label == 'box':
                self.clean_hidden_box(subset_locs, subset_nums, box_coord)



def clean_hidden_col(self, subset_locs, subset_vals):
    """
    A hidden subset has been identified.
    Goes down a col to clean subset possibilities.
    """
    # Get the column number.
    first_coord = subset_locs[0]
    coord_row, coord_col = first_coord

    # Clean up the column based on knowledge of subset.
    for row_step in range(9):  # row goes down. col is constant.
        coord = (row_step, coord_col)
        self.clean_hidden_subset(coord, subset_locs, subset_vals)



def clean_hidden_row(self, subset_locs, subset_vals):
    """
    A hidden subset has been identified.
    Goes across a row to clean subset possibilities.
    """
    # Get the row number.
    first_coord = subset_locs[0]
    coord_row, coord_col = first_coord

    # Clean up the row based on knowledge of subset.
    for col_step in range(9):  # col goes down. row is constant.
        coord = (coord_row, col_step)
        self.clean_hidden_subset(coord, subset_locs, subset_vals)



def clean_hidden_box(self, subset_locs, subset_vals, box_coord):
    """
    A hidden subset has been identified.
    Clean up possible values list of the whole 3x3 box.
    """
    # Get box info.
    box_row, box_col = box_coord
    ref_row = box_row // 3
    ref_col = box_col // 3

    # Clean up the box based on knowledge of subset.
    for row_step in range(3):
        for col_step in range(3):
            this_row = ref_row * 3 + row_step
            this_col = ref_col * 3 + col_step
            this_coord = (this_row, this_col)

            self.clean_hidden_subset(this_coord, subset_locs, subset_vals)



# #######################################
# General functions for hidden subsets
# #######################################
def format_hidden_subset_info(self, missing_vals_info):
    """
    missing_vals_info is a dict with possible values in each location.
    Format list of possibilties for subset analysis.
    """
    possible_subsets = {}
    for missing_num in missing_vals_info.keys():
        subset_locs = missing_vals_info[missing_num]

        # Formats location of subset into a string.
        subset_str = ''
        for loc in subset_locs:
            if len(subset_str) > 0:
                subset_str += '-'
            loc_row, loc_col = (loc)
            subset_str += '{0},{1}'.format(loc_row, loc_col)


        if subset_str not in possible_subsets:
            possible_subsets[subset_str] = {
                'subset_locs': subset_locs,
                'missing_num': [missing_num]
            }
        else:
            subset_info = possible_subsets[subset_str]
            subset_info['missing_num'].append(missing_num)

    return possible_subsets



def clean_hidden_subset(self, coord, subset_locs, subset_vals):
    """
    Reduces the possible_values of a single cell.
    """
    # Unsolved cell. Could be part of the subset or not.
    if coord in self.possible_values:
        poss_values = self.possible_values[coord]

        if coord in subset_locs:
            # coord IS part of the subset,
            # so keep this coord's poss_vals that are in subset_vals.
            new_poss_vals = \
                [poss_val for poss_val in poss_values if poss_val in subset_vals]
        else:
            # coord is NOT part of the subset,
            # so remove subset_vals from this coord's poss_values.
            new_poss_vals = \
                [poss_val for poss_val in poss_values if poss_val not in subset_vals]

        # new_poss_vals comes from the if/else statement.
        self.possible_values[coord] = new_poss_vals
        self.check_if_solved(coord, new_poss_vals)

















