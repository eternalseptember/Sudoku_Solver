def check_swordfish(self):
    """
    Row and col versions not necessary.
    """
    # First, fill a dict of all possible coord pairs.
    swordfish_cands = {}  # for all rows

    for row_step in range(9):
        val_lookup_row = {}

        for col_step in range(9):
            this_coord = (row_step, col_step)

            if this_coord in self.possible_values:
                self.set_lookup_table(this_coord, val_lookup_row)

        # End of row.
        self.check_sf_cands(val_lookup_row)

        # Compile dict of potential swordfish coords.
        for poss_val in val_lookup_row.keys():
            if poss_val in swordfish_cands:
                swordfish_cands[poss_val].extend(val_lookup_row[poss_val])
            else:
                swordfish_cands[poss_val] = val_lookup_row[poss_val]


    # Eliminate poss_vals that can't be part of a swordfish.
    self.clean_sf_list(swordfish_cands)


    # Then check each dict entry to see if there's a swordfish
    # within its list of coords.
    swordfish_found = self.find_swordfish(swordfish_cands)






# #######################################
# General swordfish functions
# #######################################
def check_sf_cands(self, lookup_dict):
    """
    Conditions: at least 3 possible locations per row.
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



def clean_sf_list(self, swordfish_cands):
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

            for this_coord in poss_coords:
                this_row, this_col = (this_coord)

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
    swordfish_found = []  # stores dicts[poss_val] of swordfish coords
    
    # print('checking swordfish cands')
    for poss_val in swordfish_cands.keys():
        print('poss_val: {0}, coords: {1}'.format(poss_val, swordfish_cands[poss_val]))
        col_count = {}  # key is col? and stores a list of row numbers?


    return swordfish_found




def intersection(self, list_1, list_2):
    """
    Returns the intersection of list1 and list2 in a list.
    """
    return list(set(list_1) & set(list_2))





def clean_swordfish(self, poss_val, coords_list):
    """
    """
    return None


















