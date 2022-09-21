def check_intersection_blocks(self):
    """
    Double-box, block-level eliminations.
    In each 3x3 box, check if unfilled values are in the same two rows or cols.
    Tally that info for each set of three boxes in the col and row directions.
    Then use that info to remove possible values in the third box of the set.
    """
    # keys: hashable string; value: dict containing info about missing vals
    # subdict keys: "missing_num", "in_cols" or "in_rows, "in_boxes"
    block_row_info = {}
    block_col_info = {}

    for row_step in [0, 3, 6]:

        for col_step in [0, 3, 6]:
            coord = (row_step, col_step)

            # Get list of missing vals and their poss locs in this box.
            poss_vals_in_box = self.get_box_poss_vals(coord)

            # For each missing val, get list of their possible locations.
            for missing_val in poss_vals_in_box.keys():
                poss_locs_list = poss_vals_in_box[missing_val]


                # Are they in the same two rows?
                in_rows_list = self.in_which_rows(poss_locs_list)

                if len(in_rows_list) == 2:
                    # Create a hashable key.
                    rows_str = '{0}-'.format(missing_val)
                    rows_str += ''.join(map(str, in_rows_list))

                    if rows_str not in block_row_info:
                        block_row_info[rows_str] = {
                            'missing_num': missing_val,
                            'in_rows': in_rows_list,
                            'in_boxes': [col_step]
                        }
                    else:
                        row_info = block_row_info[rows_str]
                        row_info['in_boxes'].append(col_step)


                # Are they in the same two cols?
                in_cols_list = self.in_which_cols(poss_locs_list)

                if len(in_cols_list) == 2:
                    # Create a hashable key.
                    cols_str = '{0}-'.format(missing_val)
                    cols_str += ''.join(map(str, in_cols_list))

                    if cols_str not in block_col_info:
                        block_col_info[cols_str] = {
                            'missing_num': missing_val,
                            'in_cols': in_cols_list,
                            'in_boxes': [row_step]
                        }
                    else:
                        col_info = block_col_info[cols_str]
                        col_info['in_boxes'].append(row_step)


    self.clean_rows_in_box(block_row_info)
    self.clean_cols_in_box(block_col_info)
    self.solve_queue()



def clean_rows_in_box(self, block_info):
    """
    Given info about a missing value and which two rows of which two boxes
    it's in, remove that possibility from the third box.
    """
    # Unpack block_info.
    # Key for dict on missing vals in two boxes, leading to eliminating
    # those missing vals as possibilities in third box.
    for block_key in block_info.keys():
        box_info = block_info[block_key]  # value is a dict.

        missing_num = box_info['missing_num']
        in_rows = box_info['in_rows']
        in_boxes = box_info['in_boxes']

        # Ignore if info does not span two boxes.
        if len(in_boxes) != 2:
            continue

        # Figure out the third box to remove missing value from.
        box_remaining = [0, 3, 6]  # box direction: row
        for box in in_boxes:
            box_remaining.remove(box)
        box_remaining = box_remaining[0]

        # Remove missing_num.
        for col_step in range(3):
            this_col = box_remaining + col_step

            for elim_row in in_rows:
                this_coord = (elim_row, this_col)
                self.possible_vals_check(this_coord, missing_num)



def clean_cols_in_box(self, block_info):
    """
    Given info about a missing value and which two cols of which two boxes
    it's in, remove that possibility from the third box.
    """
    # Unpack block_info.
    # Key for dict on missing vals in two boxes, leading to eliminating
    # those missing vals as possibilities in third box.
    for block_key in block_info.keys():
        box_info = block_info[block_key]  # value is a dict.

        missing_num = box_info['missing_num']
        in_cols = box_info['in_cols']
        in_boxes = box_info['in_boxes']

        # Ignore if info does not span two boxes.
        if len(in_boxes) != 2:
            continue

        # Figure out the box to remove info from.
        box_remaining = [0, 3, 6]  # box direction: col
        for box in in_boxes:
            box_remaining.remove(box)
        box_remaining = box_remaining[0]

        # Remove missing_num.
        for row_step in range(3):
            this_row = box_remaining + row_step

            for elim_col in in_cols:
                this_coord = (this_row, elim_col)
                self.possible_vals_check(this_coord, missing_num)












