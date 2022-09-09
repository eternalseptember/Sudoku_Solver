# Utility functions for sudoku_naked_triples.


def find_naked_triples(self, poss_trip_list, mode):
    """
    Make a list of every possible merged triplet set.
    'mode' is 'check_row' or 'check_col'. Pass to verify_triples_list.
    """
    poss_trips_info = {}  # [trip_str] = [list of coords]
    number_of_cells = len(poss_trip_list)

    for cell in range(number_of_cells-1):
        cell_1 = poss_trip_list[cell]
        cell_2 = poss_trip_list[cell+1]
        item_1 = self.possible_values[cell_1]
        item_2 = self.possible_values[cell_2]
        combined_poss = sorted(list(set(item_1 + item_2)))
        trip_str = ''.join(map(str, combined_poss))
        trip_coords = [cell_1, cell_2]

        # Two cells combined and have fewer than 3 possible combinations are
        # taken care by other functions.
        if len(combined_poss) <= 3:
            # New possible triplet.
            if trip_str not in poss_trips_info:
                poss_trips_info[trip_str] = trip_coords

            # Otherwise, add coord to existing triplet.
            else:
                saved_info = poss_trips_info[trip_str]

                for coord in trip_coords:
                    if coord not in saved_info:
                        saved_info.append(coord)

                poss_trips_info[trip_str] = saved_info


    # Exit the process if possible triples list is empty.
    if len(poss_trips_info) > 0:
        # verify_triples_list could return an empty dict as well
        # if no valid triple was found in that process.
        return self.verify_triples_list(poss_trips_info, mode)
    else:
        return poss_trips_info  # an empty dict



def verify_triples_list(self, poss_trips_info, mode):
    """
    Checks each entry of poss_trips_info for valid triples conditions.
    'mode' is 'check_row' or 'check_col'.
    """
    # Remove entries from poss_trips_info if triple is not valid.
    entries_to_remove = []  # list of str keys

    # List of vals and coords in possible triplets.
    # Used for finding vals and coords in multiple possible trips.
    trips_coords = []
    trips_vals = []

    # Used for finding the first set for removal.
    coords_in_mult_trips = []
    vals_in_mult_trips = []


    # First pass at cleaning up poss_trips_info.
    for trip_str in poss_trips_info.keys():
        coords_list = poss_trips_info[trip_str]
        trip_vals_list = list(map(int, trip_str))  # converted to list

        # Length of list: Need 3 coords (for now).
        if len(coords_list) != 3:
            entries_to_remove.append(trip_str)

        # No coord is in more than one trip set.
        for coord in coords_list:
            if coord not in trips_coords:
                trips_coords.append(coord)
            else:
                # print('coord in multiple trips: {0}'.format(coord))
                entries_to_remove.append(trip_str)
                coords_in_mult_trips.append(coord)

        # No possible value is in more than one trip set.
        for trip_val in trip_vals_list:
            if trip_val not in trips_vals:
                trips_vals.append(trip_val)
            else:
                # print('val in multiple trips: {0}'.format(trip_val))
                entries_to_remove.append(trip_str)
                vals_in_mult_trips.append(trip_val)


    # Remove from triplet consideration: coords and vals in multiple trips.
    # Search through poss_trips_info for the FIRST occurrence.
    if len(coords_in_mult_trips) > 0:
        for trip_str in poss_trips_info.keys():
            coords_list = poss_trips_info[trip_str]

            # Check if coord is in multiple trips here.
            # Once trip_str has been added to entries_to_remove,
            # break to next trip_str.
            for coord in coords_in_mult_trips:
                if coord in coords_list:
                    entries_to_remove.append(trip_str)
                    break


    if len(vals_in_mult_trips) > 0:
        for trip_str in poss_trips_info.keys():
            trip_vals_list = list(map(int, trip_str))  # convert

            # Check if val is in multiple trips here.
            # Once trip_str has been added to entries_to_remove,
            # break to next trip_str.
            for val in vals_in_mult_trips:
                if val in trip_vals_list:
                    entries_to_remove.append(trip_str)
                    break


    # Remove duplicates and invalid triplet candidates.
    entries_to_remove = list(set(entries_to_remove))
    for item in entries_to_remove:
        poss_trips_info.pop(item)


    # Triples have been verified. Check if they're in the same box.
    # Exit the process if possible triples list is empty.
    if len(poss_trips_info) > 0:
        self.check_naked_trips_box(poss_trips_info, mode)
        return poss_trips_info
    else:
        return poss_trips_info  # an empty dict



def check_naked_trips_box(self, poss_trips_info, mode):
    """
    This is called from verify_triples_list.
    'mode' is 'check_row' or 'check_col'.
    poss_trips_info[trip_str] = [list of coords]
    """
    # Check if the triples coordinates are in the same box.
    triple_boxes = []  # Stores trip_str if coords are in the same box.

    for trip_vals in poss_trips_info.keys():
        trip_coords = poss_trips_info[trip_vals]

        row_list = []  # One unique value if mode is 'check_row'.
        col_list = []  # One unique value if mode is 'check_col'.
        box_1 = [] # 0, 1, 2
        box_2 = [] # 3, 4, 5
        box_3 = [] # 6, 7, 8

        for coord in trip_coords:
            this_row, this_col = (coord)
            row_list.append(this_row)
            col_list.append(this_col)

        if mode == 'check_col':
            row_count = list(set(row_list))

            for this_row in row_count:
                if this_row <= 2:
                    box_1.append(this_row)
                elif this_row <= 5:
                    box_2.append(this_row)
                elif this_row <= 8:
                    box_3.append(this_row)

            if (len(box_1) == 3) or (len(box_2) == 3) or (len(box_3) == 3):
                triple_boxes.append(trip_vals)


        elif mode == 'check_row':
            col_count = list(set(col_list))

            for this_col in col_count:
                if this_col <= 2:
                    box_1.append(this_col)
                elif this_col <= 5:
                    box_2.append(this_col)
                elif this_col <= 8:
                    box_3.append(this_col)

            if (len(box_1) == 3) or (len(box_2) == 3) or (len(box_3) == 3):
                triple_boxes.append(trip_vals)


    # If there are any triples inside a box, clean them.
    if len(triple_boxes) > 0:
        # print('clean triple box: {0}'.format(triple_boxes))
        self.clean_trips_boxes(poss_trips_info, triple_boxes)



def clean_trips_boxes(self, poss_trips_info, trip_box_info):
    """
    trip_box_info is a list of str keys for poss_trips_info.
    """
    for trip_box in trip_box_info:
        trip_coords = poss_trips_info[trip_box]
        self.clean_trips_box(trip_box, trip_coords)



def clean_trips_box(self, trip_vals, trip_coords):
    """
    Info for a single 3x3 box.
    """
    # Determine box info.
    ref_row, ref_col = trip_coords[0]
    box_vals = [int(trip_val) for trip_val in trip_vals]
    box_row = ref_row // 3
    box_col = ref_col // 3

    # Go through the box.
    for row_step in range(3):
        for col_step in range(3):
            this_row = box_row * 3 + row_step
            this_col = box_col * 3 + col_step
            this_cell = (this_row, this_col)

            # First, skip over solved cells.
            if this_cell not in self.possible_values:
                continue

            # If the cell is in trip_coords, then skip over.
            if this_cell in trip_coords:
                continue

            # Otherwise, remove the values in trip_coords.
            poss_vals_in_this_cell = self.possible_values[this_cell]

            for trip_val in box_vals:
                if trip_val in poss_vals_in_this_cell:
                    poss_vals_in_this_cell.remove(trip_val)

            # Then check if this_cell has been solved.
            self.check_if_solved(this_cell, poss_vals_in_this_cell)











