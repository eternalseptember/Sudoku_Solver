def check_swordfish(self):
    """
    Row and col versions not necessary.
    """
    # First, fill a dict of all possible coord pairs.
    swordfish_cands = {}  # for all rows

    for row_step in range(9):
        val_lookup_row = {}  # for each row

        for col_step in range(9):
            this_cell = (row_step, col_step)

            if this_cell in self.possible_values:
                self.set_lookup_table(this_cell, val_lookup_row)

        # End of row.
        self.check_sf_cands(val_lookup_row)

        # Merge info from this row into dict for all rows.
        for poss_val in val_lookup_row.keys():
            if poss_val in swordfish_cands:
                swordfish_cands[poss_val].extend(val_lookup_row[poss_val])
            else:
                swordfish_cands[poss_val] = val_lookup_row[poss_val]
    

    # Eliminate poss_vals that can't be part of a swordfish.
    self.reduce_sf_list(swordfish_cands)


    # Then check each dict entry to see if there's a swordfish
    # within its list of coords.
    sf_found_dict = self.find_swordfish(swordfish_cands)




    # Commenting this out to rework for imperfect sworfish.
    """
    # Clean any swordfish found.
    # print('swordfish found:')
    if len(sf_found_dict) > 0:
        self.clean_swordfish(sf_found_dict)
    """

    # Check if anything's been solved.
    # self.solve_queue()






# #######################################
# General swordfish functions
# #######################################
def check_sf_cands(self, lookup_dict):
    """
    Conditions: for 2-2-2, at least 2 possible locations per row.
    If not met, then remove those entries from swordfish consideration.
    """
    remove_list = []

    for poss_val in lookup_dict.keys():
        poss_locs = lookup_dict[poss_val]

        # Check conditions.
        if len(poss_locs) < 2:
            remove_list.append(poss_val)

    # Remove entries.
    for poss_val in remove_list:
        lookup_dict.pop(poss_val)



def reduce_sf_list(self, swordfish_cands):
    """
    Initial cleanup of swordfish_cands list.
    Conditions: for 2-2-2, at least 6 coords total;
                at least 2 rows in at least 2 cols,
                because solved values can be part of the swordfish.
    """
    remove_list = []  # store poss_vals

    for poss_val in swordfish_cands.keys():
        poss_coords = swordfish_cands[poss_val]

        # Check conditions.
        # Condition: at least six coords total.
        if len(poss_coords) < 6:
            remove_list.append(poss_val)
    
        else:
            # Condition: at least two unique cols.
            unique_col_count = {}  # unique_col_count[col] = row_count

            for this_cell in poss_coords:
                this_row, this_col = (this_cell)

                # Add to dict if not already tracked.
                if this_col not in unique_col_count:
                    unique_col_count[this_col] = 1
                else:
                    unique_col_count[this_col] += 1

            # Remove if there are fewer than two unique cols.
            if len(unique_col_count.keys()) < 2:
                remove_list.append(poss_val)

            # Condition: at least two cols with at least two rows.
            else:
                valid_swordfish_cols = 0

                for this_col in unique_col_count.keys():
                    if unique_col_count[this_col] >= 2:
                        valid_swordfish_cols += 1

                if valid_swordfish_cols < 2:
                    remove_list.append(poss_val)


    # Remove entries.
    for poss_val in remove_list:
        swordfish_cands.pop(poss_val)



def find_swordfish(self, swordfish_cands):
    """
    Check if there is a swordfish in the cleaned swordfish_cands list.
    """
    sf_found = {}  # sf_found[poss_val] = [swordfish coords]


    # for poss_val in swordfish_cands.keys():
    for poss_val in [9]:  # simplifying for testing
        poss_coords = swordfish_cands[poss_val]
        col_tracker = {}  # col_tracker[row_num] = [col numbers]


        # First, break the list of coords down by rows.
        for poss_coord in poss_coords:
            this_row, this_col = poss_coord

            if this_row in col_tracker:
                col_tracker[this_row].append(this_col)
            else:
                col_tracker[this_row] = [this_col]


        # Look for a 9x9 setup, with either poss_val or a solved value in those spots.
        # i, j, k are generic counters for keeping track of three lists for comparison.
        num_of_rows = len(col_tracker.keys())
        col_tracker_keys = list(col_tracker.keys())


        # testing
        print('col_tracker list for poss_val: {0}'.format(poss_val))
        print('coords: {0}'.format(poss_coords))
        print()
        for item in col_tracker_keys:
            print('{0} - {1}'.format(item, col_tracker[item]))
        print()


        for i in range(0, num_of_rows-2):

            j_init = i + 1
            for j in range(j_init, num_of_rows-1):

                k_init = j + 1
                for k in range(k_init, num_of_rows):
                    row_1 = col_tracker_keys[i]
                    row_2 = col_tracker_keys[j]
                    row_3 = col_tracker_keys[k]

                    col_list_1 = col_tracker[row_1]
                    col_list_2 = col_tracker[row_2]
                    col_list_3 = col_tracker[row_3]

                    """
                    print('indices: ',end=' ')
                    print('{0}, {1}, {2}'.format(i, j, k))
                    print('row numbers: {0} \t cols: {1}'.format(row_1, col_list_1))
                    print('row numbers: {0} \t cols: {1}'.format(row_2, col_list_2))
                    print('row numbers: {0} \t cols: {1}'.format(row_3, col_list_3))
                    print()
                    """

                    # Search for a 2-2-2 combination.
                    row_list = [row_1, row_2, row_3]
                    cols_list = [col_list_1, col_list_2, col_list_3]
                    sf_list = self.two_search(poss_val, row_list, cols_list)





                    # swordfish found?
                    # sf_found[poss_val] = sf_coords




    return sf_found





def two_search(self, poss_val, row_list, cols_list):
    """
    Find a 2-2-2 pattern, where the third spot is either a solved value
    or it doesn't have the candidate as a possible value.
    """

    row_1 = row_list[0]
    row_2 = row_list[1]
    row_3 = row_list[2]

    col_list_1 = cols_list[0]
    col_list_2 = cols_list[1]
    col_list_3 = cols_list[2]


    # naked pairs in (6, 1) and (8, 1); (2, 4) and (6, 4).
    # in row 7, 9 is a valid candidate only in (2, 7) and (8, 7).
    # then check the third spot.
    ints_1 = self.intersection_of_two(col_list_1, col_list_2)
    ints_2 = self.intersection_of_two(col_list_1, col_list_3)
    ints_3 = self.intersection_of_two(col_list_2, col_list_3)


    # if any of them are empty, then skip
    if (len(ints_1) == 0) or (len(ints_2) == 0) or (len(ints_3) == 0):
        return []

    print('two search: {0}'.format(poss_val))
    print('row numbers: {0} \t cols: {1}'.format(row_1, col_list_1))
    print('row numbers: {0} \t cols: {1}'.format(row_2, col_list_2))
    print('row numbers: {0} \t cols: {1}'.format(row_3, col_list_3))

    print('\tintersection 1: {0}'.format(ints_1))
    print('\tintersection 2: {0}'.format(ints_2))
    print('\tintersection 3: {0}'.format(ints_3))
    print()




    # check if there's a naked pair that could be part of a swordfish. 
    naked_pairs = []
    for ints_col in ints_1:
        coord_1 = (row_1, ints_col)
        coord_2 = (row_2, ints_col)
        is_naked_pair = self.sf_check_naked_pair(coord_1, coord_2)

        if is_naked_pair:
            naked_pairs.extend((coord_1, coord_2))


        # what if multiple naked pairs?







    return




def intersection_of_two(self, list_1, list_2):
    return sorted(list(set(list_1) & set(list_2)))



def sf_check_naked_pair(self, coord_1, coord_2):
    poss_vals_1 = self.possible_values[coord_1]
    poss_vals_2 = self.possible_values[coord_2]
    return (poss_vals_1 == poss_vals_2)










def clean_swordfish(self, sf_dict):
    """
    Goes through every cell and removes the swordfish val from the cell's list
    of possibilities if the cell is not part of the swordfish.

    sf_dict[poss_val] = [swordfish coords]
    """
    
    for sf_val in sf_dict.keys():
        sf_coords = sf_dict[sf_val]
        row_list = []
        col_list = []

        print('cleaning swordfish val: {0}'.format(sf_val))
        print('coords: {0}'.format(sf_coords))

        # get lists of swordfish rows and cols.
        for this_coord in sf_coords:
            this_row, this_col = this_coord

            if this_row not in row_list:
                row_list.append(this_row)
            
            if this_col not in col_list:
                col_list.append(this_col)
        

        # go through each cell.
        # if cell is in the same row or col as the swordfish set,
        # but it's not part of the sf set, then remove sf_val from its
        # list of possibilities.
        for row_step in range(9):
            for col_step in range(9):
                this_cell = (row_step, col_step)

                # skip over solved cells.
                if this_cell not in self.possible_values:
                    continue


                # check if this cell is in swordfish row or col.
                if row_step in row_list:
                    in_sf_row = True
                else:
                    in_sf_row = False
                
                if col_step in col_list:
                    in_sf_col = True
                else:
                    in_sf_col = False


                # if in row or col of a swordfish cell, then check if it's a swordfish cell.
                # if it's not a sf cell, remove sf_val from its list of possible cells.
                if this_cell in sf_coords:
                    continue
                elif in_sf_row or in_sf_col:
                    self.possible_vals_check(this_cell, sf_val)
                







    
















