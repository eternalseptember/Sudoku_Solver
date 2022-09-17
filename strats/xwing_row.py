def check_xwing(self):
    """
    X-wing: a candidate in four cells that form a rectangle.
    """
    # print('check xwing by rows')
    self.check_xw_by_rows()

    # print('check xwing by cols')
    self.check_xw_by_cols()



def check_xw_by_rows(self):
    """
    When there are
    * only two possible cells for a value in each of two different rows,
    * and these candidates lie also in the same columns,
    then all other candidates for this value in the columns can be eliminated.
    """
    xwing_candidates = {}  # For all rows.
    xwings_found = []  # stores dicts[poss_val] of xwing coords

    # First, fill a dict of all possible coord pairs.
    # Then, initial cleanup of xwings cands list at the end of each row.
    for row_step in range(0, 9):

        val_lookup_row = {}
        for col_step in range(0, 9):
            this_coord = (row_step, col_step)

            if this_coord in self.possible_values:
                self.set_lookup_table(this_coord, val_lookup_row)

        # End of row.
        self.check_xw_cands(val_lookup_row)

        # Compile dict of potential xwing components.
        for poss_val in val_lookup_row.keys():
            if poss_val in xwing_candidates:
                xwing_candidates[poss_val].extend(val_lookup_row[poss_val])
            else:
                xwing_candidates[poss_val] = val_lookup_row[poss_val]


    # Eliminate entries without enough possible candidates be part of an xwing.
    self.clean_xw_list(xwing_candidates)


    # Then check each dict entry to see if there's an xwing
    # within the list of coords.
    for poss_val in xwing_candidates.keys():
        poss_coords = xwing_candidates[poss_val]
        xwing_sets = self.check_xw_is_same_cols(poss_val, poss_coords)

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
        self.clean_xw_col(poss_val, xwing_coords)

    self.solve_queue()



def check_xw_is_same_cols(self, poss_val, list_of_coords):
    """
    Matches are already in same rows. If they are also in same cols,
    then an xwing is found.
    Returns a list of lists of four coordinates.
    """
    xwing_sets = []  # each item a list of four coords

    # Check list_of_coords in groups of two.
    # Need to account for four coords at a time.
    for each_pair_1 in range(0, len(list_of_coords), 2):
        # Reference coordinates:
        row_1_coord_1 = list_of_coords[each_pair_1]
        row_1_coord_2 = list_of_coords[each_pair_1 + 1]
        row_1_coords = (row_1_coord_1, row_1_coord_2)

        # print('\t{0} {1}:'.format(row_1_coord_1, row_1_coord_2), end=' ')

        # Check if there's more coords to compare to.
        if (each_pair_1 + 2) >= len(list_of_coords):
            # print('no more coords to compare to')
            break

        # Rest of coords to compare to.
        xwing_row_2_cands = list_of_coords[(each_pair_1 + 2):]
        # print('{0}'.format(xwing_row_2_cands))

        for each_pair_2 in range(0, len(xwing_row_2_cands), 2):
            row_2_coord_1 = xwing_row_2_cands[each_pair_2]
            row_2_coord_2 = xwing_row_2_cands[each_pair_2 + 1]
            row_2_coords = (row_2_coord_1, row_2_coord_2)

            is_same_cols = self.is_xwing_same_cols(row_1_coords, row_2_coords)

            if is_same_cols:
                xwing_coords = \
                    [row_1_coord_1, row_1_coord_2, row_2_coord_1, row_2_coord_2]
                xwing_sets.append(xwing_coords)


    # Return a list of four coordinates in the xwing.
    return xwing_sets



def is_xwing_same_cols(self, coords_row_1, coords_row_2):
    """
    coords_row_1 and coords_row_2 are lists.
    Returns a boolean.
    """
    coord_1, coord_2 = (coords_row_1)
    coord_3, coord_4 = (coords_row_2)

    row_1, col_1 = (coord_1)
    row_2, col_2 = (coord_2)
    row_3, col_3 = (coord_3)
    row_4, col_4 = (coord_4)

    if (col_1 == col_3) and (col_2 == col_4):
        return True
    else:
        return False



def clean_xw_col(self, poss_val, coords_list):
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

    clean_col_1 = col_1
    clean_col_2 = col_2
    coords_col_1 = [coord_1, coord_3]
    coords_col_2 = [coord_2, coord_4]

    for row_step in range(9):  # row_step goes down.
        clean_coord_1 = (row_step, clean_col_1)
        clean_coord_2 = (row_step, clean_col_2)

        # Remove poss_val in col outside of coords_col_1.
        if clean_coord_1 not in coords_col_1:
            self.possible_vals_check(clean_coord_1, poss_val)

        if clean_coord_2 not in coords_col_2:
            self.possible_vals_check(clean_coord_2, poss_val)



# #######################################
# General xwing functions
# #######################################
def check_xw_cands(self, lookup_dict):
    """
    Check this condition:
    Only two possible cells for a val in this row or col.
    """
    remove_list = []

    for poss_val in lookup_dict.keys():
        poss_locs = lookup_dict[poss_val]

        # Add to dict if there are only two possible locations.
        if len(poss_locs) != 2:
            remove_list.append(poss_val)

    # Remove entries.
    for poss_val in remove_list:
        lookup_dict.pop(poss_val)



def clean_xw_list(self, xwing_candidates):
    """
    Remove unsolved candidates that can't be part of an xwing.
    """
    remove_list = []  # store poss_vals

    for poss_val in xwing_candidates.keys():
        poss_coords = xwing_candidates[poss_val]

        # xwing candidates need at least four possible locations.
        if len(poss_coords) < 4:
            remove_list.append(poss_val)

    # Remove entries.
    for poss_val in remove_list:
        xwing_candidates.pop(poss_val)
















