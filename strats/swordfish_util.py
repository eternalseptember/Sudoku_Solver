# General swordfish functions


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


    # #####
    # for poss_val in swordfish_cands.keys():
    # #####
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
        print('organized list: row - cols')
        for item in col_tracker_keys:
            print('{0} - {1}'.format(item, col_tracker[item]))
        print()


        # Three lists for comparison.
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

                    # naked pairs in (6, 1) and (8, 1); (2, 4) and (6, 4).
                    # in row 7, 9 is a valid candidate only in (2, 7) and (8, 7).
                    # then check the third spot.
                    ints_1 = self.intersection_of_two(col_list_1, col_list_2)
                    ints_2 = self.intersection_of_two(col_list_1, col_list_3)
                    ints_3 = self.intersection_of_two(col_list_2, col_list_3)


                    # If any of them are empty, then skip.
                    if (len(ints_1) == 0) or (len(ints_2) == 0) or (len(ints_3) == 0):
                        continue

                    print()
                    print('two search: {0}'.format(poss_val))
                    print('row numbers: {0} \t cols: {1}'.format(row_1, col_list_1))
                    print('row numbers: {0} \t cols: {1}'.format(row_2, col_list_2))
                    print('row numbers: {0} \t cols: {1}'.format(row_3, col_list_3))

                    print('\tintersection 1: {0}'.format(ints_1))
                    print('\tintersection 2: {0}'.format(ints_2))
                    print('\tintersection 3: {0}'.format(ints_3))



                    # testing one of these ways of looking for a swordfish
                    row_list = [row_1, row_2, row_3]
                    ints_list = [ints_1, ints_2, ints_3]
                    sf_coords = self.sf_check_loop(poss_val, row_list, ints_list)




                    # swordfish found?
                    # what if it found more than one set?
                    if len(sf_coords) >= 6:
                        sf_found[poss_val] = sf_coords




    return sf_found



def intersection_of_two(self, list_1, list_2):
    """
    Return a sorted list of the intersection of two lists.
    """
    return sorted(list(set(list_1) & set(list_2)))



def sf_check_loop(self, poss_val, row_list, ints_list):
    """
    Piece together the coords and check if they're in a loop.
    ints_list contains values found in the intersection of two rows.
    """

    print('check for loop for poss_val: {0}'.format(poss_val))

    row_1 = row_list[0]
    row_2 = row_list[1]
    row_3 = row_list[2]
    ints_1 = ints_list[0]
    ints_2 = ints_list[1]
    ints_3 = ints_list[2]

    # sort coordinates information by rows
    sf_cols_1 = sorted(set(ints_1 + ints_2))
    sf_cols_2 = sorted(set(ints_1 + ints_3))
    sf_cols_3 = sorted(set(ints_2 + ints_3))
    len_col_1 = len(sf_cols_1)


    # piece the loop coords together into sf_loop_coords
    sf_loop_coords = []


    # check poss_sf_coords
    print('checking poss_sf_coords:')
    print('\trow {0}: cols {1}'.format(row_1, sf_cols_1))
    print('\trow {0}: cols {1}'.format(row_2, sf_cols_2))
    print('\trow {0}: cols {1}'.format(row_3, sf_cols_3))




    # row_1 is already connected.
    # check whether poss_val in other rows is connected to row_1 by shared cols.
    for i in range(0, len_col_1-1):

        j_init = i+1
        for j in range(j_init, len_col_1):
            sf_row_1_col_1 = sf_cols_1[i]
            sf_row_1_col_2 = sf_cols_1[j]

            col_1_in_row_2 = False
            col_1_in_row_3 = False
            col_2_in_row_2 = False
            col_2_in_row_3 = False

            if sf_row_1_col_1 in sf_cols_2:
                col_1_in_row_2 = True
            if sf_row_1_col_1 in sf_cols_3:
                col_1_in_row_3 = True
            if sf_row_1_col_2 in sf_cols_2:
                col_2_in_row_2 = True
            if sf_row_1_col_2 in sf_cols_3:
                col_2_in_row_3 = True
            

            # checking things
            """
            print('\tcol_1_in_row_2: {0}'.format(col_1_in_row_2))
            print('\tcol_1_in_row_3: {0}'.format(col_1_in_row_3))
            print('\tcol_2_in_row_2: {0}'.format(col_2_in_row_2))
            print('\tcol_2_in_row_3: {0}'.format(col_2_in_row_3))
            """



            # then look if there is a col that is in row 2 and 3 only
            # If a col is in both rows 2 and 3, then no new information learned.
            # Can't be false in both rows because those got filtered out by earlier steps.
            check_sf_cols_3 = False
            sf_cols_3_pairs = []  # stores lists of coord pairs

            if (col_1_in_row_2 is True) and (col_1_in_row_3 is False):
                # check if col_2 and look for the third coord
                if (col_2_in_row_2 is False) and (col_2_in_row_3 is True):
                    check_sf_cols_3 = True
                    sf_cols_1_reduced = sf_cols_1.copy()
                    sf_cols_2_reduced = sf_cols_2.copy()
                    sf_cols_3_reduced = sf_cols_3.copy()

                    sf_cols_1_reduced.remove(sf_row_1_col_1)
                    sf_cols_1_reduced.remove(sf_row_1_col_2)
                    sf_cols_2_reduced.remove(sf_row_1_col_1)
                    sf_cols_3_reduced.remove(sf_row_1_col_2)

                    print('sf_row_1_col_1: {0}, sf_row_1_col_2: {1}'.format(sf_row_1_col_1, sf_row_1_col_2))
                    print('\tcol_1_in_row_2 is True and col_1_in_row_3 is False')
                    print('\t\tsf_cols_1_reduced: {0}'.format(sf_cols_1_reduced))
                    print('\t\tsf_cols_2_reduced: {0}'.format(sf_cols_2_reduced))
                    print('\t\tsf_cols_3_reduced: {0}'.format(sf_cols_3_reduced))


            elif (col_1_in_row_2 is False) and (col_1_in_row_3 is True):
                # check col_2
                if (col_2_in_row_2 is True) and (col_2_in_row_3 is False):
                    check_sf_cols_3 = True
                    sf_cols_1_reduced = sf_cols_1.copy()
                    sf_cols_2_reduced = sf_cols_2.copy()
                    sf_cols_3_reduced = sf_cols_3.copy()

                    sf_cols_1_reduced.remove(sf_row_1_col_1)
                    sf_cols_1_reduced.remove(sf_row_1_col_2)
                    sf_cols_2_reduced.remove(sf_row_1_col_2)
                    sf_cols_3_reduced.remove(sf_row_1_col_1)

                    print('sf_row_1_col_1: {0}, sf_row_1_col_2: {1}'.format(sf_row_1_col_1, sf_row_1_col_2))
                    print('\tcol_1_in_row_2 is False and col_1_in_row_3 is True')
                    print('\t\tsf_cols_1_reduced: {0}'.format(sf_cols_1_reduced))
                    print('\t\tsf_cols_2_reduced: {0}'.format(sf_cols_2_reduced))
                    print('\t\tsf_cols_3_reduced: {0}'.format(sf_cols_3_reduced))



            if check_sf_cols_3 is True:
                # piece together the third set of coords
                sf_cols_2_3 = self.intersection_of_two(sf_cols_2_reduced, sf_cols_3_reduced)
                print('\t\t\tintersection of cols 2 and 3: {0}'.format(sf_cols_2_3))

                for this_col in sf_cols_2_3:
                    coord_2 = (row_2, this_col)
                    coord_3 = (row_3, this_col)
                    is_naked_pair = self.sf_check_naked_pair(coord_2, coord_3)
                    
                    if is_naked_pair:
                        sf_cols_3_pairs.append([coord_2, coord_3])
                        print('\t\t\tnaked pair: {0}, {1}'.format(coord_2, coord_3))

                        # what were the first four coordinates?
                        sf_coord_1 = (sf_row_1_col_1)  # other coordinate?

            

            # checking stuff
            if len(sf_cols_3_pairs) > 0:
                print('\t\t\tsf_cols_3_pairs: {0}'.format(sf_cols_3_pairs))

            






    





    # if there are at least six coordinates, return the list of coords.
    # otherwise, return an empty list
    if len(sf_loop_coords) >= 6:
        return sf_loop_coords
    else:
        return []




def sf_check_naked_pair(self, coord_1, coord_2):
    """
    Check for naked pair: matching possible values of length 2.
    """
    poss_vals_1 = self.possible_values[coord_1]
    poss_vals_2 = self.possible_values[coord_2]

    if (len(poss_vals_1) == 2) and (len(poss_vals_2) == 2):
        return (poss_vals_1 == poss_vals_2)
    else:
        return False



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

        # Get lists of swordfish rows and cols.
        for this_coord in sf_coords:
            this_row, this_col = this_coord

            if this_row not in row_list:
                row_list.append(this_row)
            
            if this_col not in col_list:
                col_list.append(this_col)
        

        # Go through each cell.
        # If cell is in the same row or col as the swordfish set,
        # but it's not part of the sf set, then remove sf_val from its
        # list of possibilities.
        for row_step in range(9):
            for col_step in range(9):
                this_cell = (row_step, col_step)

                # Skip over solved cells.
                if this_cell not in self.possible_values:
                    continue


                # Check if this cell is in swordfish row or col.
                if row_step in row_list:
                    in_sf_row = True
                else:
                    in_sf_row = False
                
                if col_step in col_list:
                    in_sf_col = True
                else:
                    in_sf_col = False


                # If in row or col of a swordfish cell, 
                #     then check if it's a swordfish cell.
                # If it's not a sf cell,
                #     remove sf_val from its list of possible cells.
                if this_cell in sf_coords:
                    continue
                elif in_sf_row or in_sf_col:
                    self.possible_vals_check(this_cell, sf_val)
                






