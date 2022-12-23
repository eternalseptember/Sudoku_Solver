# Utility functions for naked subsets


def set_missing_val_table(self, coord, missing_val_dict):
    """
    Tallies the combinations of missing values in each area.
    """
    if coord in self.possible_values:
        poss_values = self.possible_values[coord]

        # Convert to hashable key.
        poss_str = ''.join(map(str, poss_values))

        # Tally combinations of missing values.
        if poss_str not in missing_val_dict:
            missing_val_dict[poss_str] = [coord]
        else:
            missing_val_dict[poss_str].append(coord)



def find_naked_matches(self, missing_val_dict):
    """
    Search the dictionary of missing values for matches between
    possible values in a cell and
    the number of cells with that exact list of possibilities.
    Also keep track of the matches' locations.
    """
    matches_vals = []
    matches_locs = {}

    for missing_val in missing_val_dict.keys():
        if len(missing_val) == len(missing_val_dict[missing_val]):
            # Turn missing_val hash back into a list.
            missing_val_list = [int(val) for val in missing_val]
            matches_vals.append(missing_val_list)
            matches_locs[missing_val] = missing_val_dict[missing_val]

    return matches_vals, matches_locs



def remove_naked_in_box(self, match, match_dict):
    """
    match is the list of values in the pair/triplet/set.
    match_dict keeps track of where the match is with a hashable key.
    If cells of the match are in the same box, then remove those values
    as possibilities from the rest of the box.
    """
    match_str = ''.join(map(str, match))
    match_loc = match_dict[match_str]
    is_same_box, box_loc = self.in_which_box(match_loc)

    if is_same_box:
        box_row, box_col = box_loc

        for row_step in range(3):
            for col_step in range(3):
                row = box_row * 3 + row_step
                col = box_col * 3 + col_step
                this_cell = (row, col)
                self.clean_naked_sets(this_cell, match, 'box')



def in_which_box(self, coords_list):
    """
    Checks whether all values in match are in the same box.
    coords_list is all of the cells in the match, sharing the same
    list of possible values.
    Used in other strats as well.
    """
    boxes = []  # box_loc = (box_row, box_col)

    for coord in coords_list:
        ref_row, ref_col = coord
        box_row = ref_row // 3
        box_col = ref_col // 3
        box = (box_row, box_col)
        boxes.append(box)

    # Are they all in the same box?
    # And if they are, which box?
    if len(set(boxes)) == 1:
        # Multiply box_row and box_col by 3.
        return True, boxes[0]
    else:
        return False, None



def clean_naked_sets(self, coord, matched_set, label):
    """
    matched_set is a list of values in the pair/triplet/set.
    """
    if coord in self.possible_values:
        poss_values = self.possible_values[coord]

        if poss_values == matched_set:
            # Don't want to erase the match.
            # print('{0} match found: {1} at {2}'
            # 	.format(label, matched_set, coord))
            return
        else:
            # Outside of the match, remove any values of the matched set.
            # Then check if coord has been solved.
            for val in matched_set:
                self.possible_vals_check(coord, val)









            
                