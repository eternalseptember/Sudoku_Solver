# Used in main xwing function.


def check_xw_by_cols(self):
    """
    When there are
    * only two possible cells for a value in each of two different cols,
    * and these candidates lie also in the same rows,
    then all other candidates for this value in the rows can be eliminated.
    """
    xwing_candidates = {}  # For all cols.
    xwings_found = []  # stores dicts of xwing coords

    # First, fill a dict of all possible coord pairs.
    # Then, initial cleanup of xwings cands list at the end of each col.
    for col_step in range(0, 9):

        val_lookup_col = {}
        for row_step in range(0, 9):
            this_cell = (row_step, col_step)

            if this_cell in self.possible_values:
                self.set_lookup_table(this_cell, val_lookup_col)

        # End of col.
        self.check_xw_cands(val_lookup_col)

        # Compile dict of potential xwing components.
        for poss_val in val_lookup_col.keys():
            if poss_val in xwing_candidates:
                xwing_candidates[poss_val].extend(val_lookup_col[poss_val])
            else:
                xwing_candidates[poss_val] = val_lookup_col[poss_val]


    # Eliminate entries without enough possible candidates be part of an xwing.
    self.reduce_xw_list(xwing_candidates)


    # Then check each dict entry to see if there's an xwing
    # within the list of coords.
    for poss_val in xwing_candidates.keys():
        poss_coords = xwing_candidates[poss_val]
        xwing_sets = self.check_xw_is_same_rows(poss_val, poss_coords)

        if len(xwing_sets) > 0:
            # print('xwing_set: {0} - {1}'.format(poss_val, xwing_sets))

            for xwing_set in xwing_sets:
                xwing_dict = {}
                xwing_dict[poss_val] = xwing_set

                xwings_found.append(xwing_dict)

        # else:
        # 	print('xwing_set is empty')


    # Clean xwing.
    for xwing_set in xwings_found:
        poss_val = list(xwing_set.keys())[0]
        xwing_coords = xwing_set[poss_val]
        self.clean_xw_row(poss_val, xwing_coords)
    
    self.solve_queue()



def check_xw_is_same_rows(self, poss_val, list_of_coords):
    """
    Matches are already in same cols. If they are also in same rows,
    then an xwing is found.
    Returns a list of lists of four coordinates.
    """
    xwing_sets = []  # a list of a set

    # Check list_of_coords in groups of two.
    # Need to account for four coords at a time.
    for each_pair_1 in range(0, len(list_of_coords), 2):
        # Reference coordinates:
        col_1_coord_1 = list_of_coords[each_pair_1]
        col_1_coord_2 = list_of_coords[each_pair_1 + 1]
        col_1_coords = (col_1_coord_1, col_1_coord_2)

        # print('\t{0} {1}:'.format(col_1_coord_1, col_1_coord_2), end=' ')

        # Check if there's more coords to compare to.
        if (each_pair_1 + 2) >= len(list_of_coords):
            # print('no more coords to compare to')
            break

        # Rest of coords to compare to.
        xwing_col_2_cands = list_of_coords[(each_pair_1 + 2):]
        # print('{0}'.format(xwing_col_2_cands))

        for each_pair_2 in range(0, len(xwing_col_2_cands), 2):
            col_2_coord_1 = xwing_col_2_cands[each_pair_2]
            col_2_coord_2 = xwing_col_2_cands[each_pair_2 + 1]
            col_2_coords = (col_2_coord_1, col_2_coord_2)

            is_same_rows = self.is_xwing_same_rows(col_1_coords, col_2_coords)

            if is_same_rows:
                xwing_coords = \
                    [col_1_coord_1, col_1_coord_2, col_2_coord_1, col_2_coord_2]
                xwing_sets.append(xwing_coords)


    # Return a list of [four coordinates]-lists.
    return xwing_sets



def is_xwing_same_rows(self, coords_col_1, coords_col_2):
    """
    coords_col_1 and coords_col_2 are lists.
    Returns a boolean.
    """
    coord_1, coord_2 = (coords_col_1)
    coord_3, coord_4 = (coords_col_2)

    row_1, col_1 = (coord_1)
    row_2, col_2 = (coord_2)
    row_3, col_3 = (coord_3)
    row_4, col_4 = (coord_4)

    if (row_1 == row_3) and (row_2 == row_4):
        return True
    else:
        return False



def clean_xw_row(self, poss_val, coords_list):
    """
    Coords in coords_list is listed in a specific order.
    """
    coord_1 = coords_list[0]
    coord_2 = coords_list[1]
    coord_3 = coords_list[2]
    coord_4 = coords_list[3]

    row_1, col_1 = (coord_1)
    row_2, col_2 = (coord_2)
    row_3, col_3 = (coord_3)
    row_4, col_4 = (coord_4)

    clean_row_1 = row_1
    clean_row_2 = row_2
    coords_row_1 = [coord_1, coord_3]
    coords_row_2 = [coord_2, coord_4]

    for col_step in range(9):  # col_step goes across.
        clean_coord_1 = (clean_row_1, col_step)
        clean_coord_2 = (clean_row_2, col_step)

        # Remove poss_val in row outside of coords_row_1.
        if clean_coord_1 not in coords_row_1:
            self.possible_vals_check(clean_coord_1, poss_val)

        if clean_coord_2 not in coords_row_2:
            self.possible_vals_check(clean_coord_2, poss_val)















