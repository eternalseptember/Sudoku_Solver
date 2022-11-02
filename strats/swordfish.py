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
    Conditions: at least 9 coords total; at least 3 rows in at least 3 cols.
    """
    remove_list = []  # store poss_vals

    for poss_val in swordfish_cands.keys():
        poss_coords = swordfish_cands[poss_val]

        # Check conditions.
        # Condition: at least nine coords total.
        if len(poss_coords) < 9:
            remove_list.append(poss_val)
    
        else:
            # Condition: at least three unique cols.
            unique_col_count = {}  # unique_col_count[col] = row_count

            for this_cell in poss_coords:
                this_row, this_col = (this_cell)

                # Add to dict if not already tracked.
                if this_col not in unique_col_count:
                    unique_col_count[this_col] = 1
                else:
                    unique_col_count[this_col] += 1

            # Remove if there are fewer than three unique cols.
            if len(unique_col_count.keys()) < 3:
                remove_list.append(poss_val)

            # Condition: at least three cols with at least three rows.
            else:
                valid_swordfish_cols = 0

                for this_col in unique_col_count.keys():
                    if unique_col_count[this_col] >= 3:
                        valid_swordfish_cols += 1

                if valid_swordfish_cols < 3:
                    remove_list.append(poss_val)


    # Remove entries.
    for poss_val in remove_list:
        swordfish_cands.pop(poss_val)



def find_swordfish(self, swordfish_cands):
    """
    Check if there is a swordfish in the cleaned swordfish_cands list.
    """
    swordfishes_found = []  # stores dicts[poss_val] of swordfish coords

    for poss_val in swordfish_cands.keys():
        swordfish_found = {}  # swordfish_found[poss_val] = [list of coords]
        poss_coords = swordfish_cands[poss_val]
        col_tracker = {}  # col_tracker[row_num] = [col numbers]


        # first, sort the list of coords
        for poss_coord in poss_coords:
            this_row, this_col = poss_coord

            if this_row in col_tracker:
                col_tracker[this_row].append(this_col)
            else:
                col_tracker[this_row] = [this_col]


        # then compare each entry in col_tracker to see if the same three
        # col numbers show up in three different rows.

        print('col tracking for poss val: {0}'.format(poss_val))
        for row_num in col_tracker.keys():
            print('row: {0} cols: {1}'.format(row_num, col_tracker[row_num]))


        num_of_rows = len(col_tracker.keys())
        col_tracker_keys = list(col_tracker.keys())

        print('col tracker list: {0}'.format(col_tracker_keys))

        # i, j, k are generic counters for keeping track of three lists for comparison
        for i in range(0, num_of_rows-2):

            j_init = i + 1
            for j in range(j_init, num_of_rows-1):

                k_init = j + 1
                for k in range(k_init, num_of_rows):
                    print('{0}, {1}, {2}'.format(i, j, k))
                    row_0 = col_tracker_keys[0]
                    row_1 = col_tracker_keys[1]
                    row_2 = col_tracker_keys[2]
                    print('row numbers: ', end=" ")
                    print('{0}, {1}, {2}'.format(row_0, row_1, row_2))
                    col_list_0 = col_tracker[row_0]
                    col_list_1 = col_tracker[row_1]
                    col_list_2 = col_tracker[row_2]




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


















