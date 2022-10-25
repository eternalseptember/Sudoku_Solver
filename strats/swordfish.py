def check_swordfish(self):
    """
    Row and col versions not necessary.
    """
    # First, fill a dict of all possible coord pairs.
    swordfish_cands = {}  # for all rows

    for row_step in range(9):
        val_lookup_row = {}

        for col_step in range(9):
            this_cell = (row_step, col_step)

            if this_cell in self.possible_values:
                self.set_lookup_table(this_cell, val_lookup_row)

        # End of row.
        self.check_sf_cands(val_lookup_row)

        # Compile dict of potential swordfish coords.
        for poss_val in val_lookup_row.keys():
            if poss_val in swordfish_cands:
                swordfish_cands[poss_val].extend(val_lookup_row[poss_val])
            else:
                swordfish_cands[poss_val] = val_lookup_row[poss_val]


    # Eliminate poss_vals that can't be part of a swordfish.
    self.reduce_sf_list(swordfish_cands)


    # Then check each dict entry to see if there's a swordfish
    # within its list of coords.
    swordfish_found = self.find_swordfish(swordfish_cands)


    # Clean any swordfish found.
    # print('swordfish found:')
    for swordfish_set in swordfish_found:
        print('{0}'.format(swordfish_set))


    # Check if anything's been solved.
    # self.solve_queue()






# #######################################
# General swordfish functions
# #######################################
def check_sf_cands(self, lookup_dict):
    """
    Conditions: at least 3 possible locations per row.
    If not met, then remove those entries from swordfish consideration.
    """
    remove_list = []

    for poss_val in lookup_dict.keys():
        poss_locs = lookup_dict[poss_val]

        # Check conditions.
        if len(poss_locs) < 3:
            remove_list.append(poss_val)

    # Remove entries.
    for poss_val in remove_list:
        lookup_dict.pop(poss_val)



def reduce_sf_list(self, swordfish_cands):
    """
    Initial cleanup of swordfish_cands list.
    Conditions: at least 9 coordinates total; at least 3 coords in each col.
    """
    remove_list = []  # store poss_vals

    for poss_val in swordfish_cands.keys():
        poss_coords = swordfish_cands[poss_val]

        # Check conditions.
        if len(poss_coords) < 9:
            remove_list.append(poss_val)
    
        else:
            unique_col_count = {}  # key: col; val: count

            for this_cell in poss_coords:
                this_row, this_col = (this_cell)

                # Add to dict if not already tracked.
                if this_col not in unique_col_count:
                    unique_col_count[this_col] = 1
                else:
                    unique_col_count[this_col] += 1

            # Check that there are at least three cols.
            if len(unique_col_count.keys()) < 3:
                remove_list.append(poss_val)

            # Then check count in all cols.
            else:
                swordfish_cols_count = 0  # at least 3 cols need at least 3 locations

                for this_col in unique_col_count.keys():
                    if unique_col_count[this_col] >= 3:
                        swordfish_cols_count += 1


                if swordfish_cols_count <= 2:
                    remove_list.append(poss_val)


    # Remove entries.
    for poss_val in remove_list:
        swordfish_cands.pop(poss_val)



def find_swordfish(self, swordfish_cands):
    """
    Check if there is a swordfish in the cleaned swordfish_cands list.
    """
    swordfishes_found = []  # stores dicts[poss_val] of swordfish coords
    
    print('checking swordfish cands')
    for poss_val in swordfish_cands.keys():
        swordfish_found = {}  # swordfish_found[poss_val] = [list of coords]
        poss_coords = swordfish_cands[poss_val]
        row_tracker = {}  # row_tracker[col] = [row numbers]

        print('poss_val: {0}, coords: {1}'.format(poss_val, poss_coords))

        # first, sort the list of coords
        for poss_coord in poss_coords:
            this_row, this_col = poss_coord

            if this_col in row_tracker:
                row_tracker[this_col].append(this_row)
            else:
                row_tracker[this_col] = [this_row]


        # then compare each entry in row_tracker to see if the same three
        # row numbers show up in three different cols.



    return swordfishes_found




def intersection_of_three(self, list_1, list_2, list_3):
    """
    Returns the intersection of list_1, list_2, and list_3 in a list.
    """
    return list(set(list_1) & set(list_2) & set(list_3))





def clean_swordfish(self, poss_val, coords_list):
    """
    """
    # possible_vals_check() or check_if_solved()
    return None


















