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



    # testing
    print()
    print('sf found?')
    for item in sf_found_dict.keys():
        print('{0} - {1}'.format(item, sf_found_dict[item]))




    # Commenting this out to rework for imperfect sworfish.
    """
    # Clean any swordfish found.
    # print('swordfish found:')
    if len(sf_found_dict) > 0:
        self.clean_swordfish(sf_found_dict)
    """

    # Check if anything's been solved.
    # self.solve_queue()



























