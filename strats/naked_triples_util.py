# Utility functions for sudoku_naked_triples.


def find_naked_triples(self, poss_trip_list, mode):
    # Make a list of every possible merged triplet set.
    # 'mode' is 'check_row' or 'check_col'. Pass to verify function.
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
        return self.verify_triples_list(poss_trips_info, mode)
    else:
        return poss_trips_info



def verify_triples_list(self, poss_trips_info, mode):
    print('verify triples list. mode: {0} list: {1} '.format(mode, poss_trips_info))
    # 'mode' is 'check_row' or 'check_col'.

    # Remove entries from poss_trips_info if triple is not valid.
    entries_to_remove = []  # List of str keys.

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

        # Length of list: Need 3 coords.
        if len(coords_list) != 3:
            entries_to_remove.append(trip_str)

        # No coord is in more than one trip set.
        for coord in coords_list:
            if coord not in trips_coords:
                trips_coords.append(coord)
            else:
                # print('coord in multiple trip: {0}'.format(coord))
                entries_to_remove.append(trip_str)

                # For finding the first occurance to remove.
                coords_in_mult_trips.append(coord)


        # No possible value is in more than one trip set.
        for trip_val in trip_vals_list:
            if trip_val not in trips_vals:
                trips_vals.append(trip_val)
            else:
                # print('val in multiple trip: {0}'.format(trip_val))
                entries_to_remove.append(trip_str)

                # For finding the first occurance to remove.
                vals_in_mult_trips.append(trip_val)


    # Search through the list for the FIRST occurance.
    # Remove from triplet consideration: coords and vals in multiple trips.
    if len(coords_in_mult_trips) > 0:
        for entry in poss_trips_info.keys():
            coords_list = poss_trips_info[entry]

            # Check if coord is in multiple trips here.
            for coord in coords_in_mult_trips:
                if coord in coords_list:
                    entries_to_remove.append(entry)

                    # Once entry has been added to entries_to_remove,
                    # break to next entry.
                    break


    if len(vals_in_mult_trips) > 0:
        # get coordinates and put them in entries_to_remove
        for trip_str in poss_trips_info.keys():
            trip_vals_list = list(map(int, trip_str))  # convert

            # Check if val is in multiple trips here.
            for val in vals_in_mult_trips:
                if val in trip_vals_list:
                    entries_to_remove.append(trip_str)

                    # Once trip_str has been added to entries_to_remove,
                    # break to next trip_str.
                    break


    # Remove duplicates first, then remove triplet candidates.
    entries_to_remove = list(set(entries_to_remove))
    for item in entries_to_remove:
        poss_trips_info.pop(item)


    # Triples have been verified. Check if they're in the same box.
    self.check_naked_triples_box(poss_trips_info, mode)

    return poss_trips_info



def check_naked_triples_box(self, poss_trips_info, mode):
    # Unlike the row and col versions of this function, this is called
    # from verify_triples_list.
    # 'mode' is 'check_row' or 'check_col'.

    # poss_trips_info[trip_str] = [list of coords]
    triple_boxes = []  # store trip_str if coords are in the same box

    for trip_vals in poss_trips_info.keys():
        trip_coords = poss_trips_info[trip_vals]

        box_row = None
        box_col = None
        same_row = True
        same_col = True

        # check this section
        for coord in trip_coords:
            this_row, this_col = (coord)

            # set row and col if they're unset
            # compare if they match
            if box_row is None:
                box_row = this_row
            elif box_row != this_row:
                same_row = False
                break  # go to the next trip_vals

            if box_col is None: 
                box_col = this_col
            elif box_col != this_col:
                same_col = False
                break  # go to the next trip_vals

        # IF GETTING CALLED FROM CHECK_ROW, THEN SAME_ROW CAN'T COUNT.
        if (mode == 'check_row') and same_col:
            triple_boxes.append(trip_vals)

        if (mode == 'check_col') and same_row:
            triple_boxes.append(trip_vals)


    # If there are any triples inside a box, clean them.
    if len(triple_boxes) > 0:
        self.clean_triple_boxes(poss_trips_info, triple_boxes)



def clean_triple_boxes(self, poss_trips_info, trip_box_info):
    # Will be passed a list of keys of triple boxes.

    for trip_box in trip_box_info:
        trip_coords = poss_trips_info[trip_box]
        print('clean triple box: {0}\tcoords: {1}'.format(trip_box, trip_coords))
        self.clean_triple_box(trip_box, trip_coords)



def clean_triple_box(self, trip_vals, trip_coords):
    # Info for a single 3x3 box.

    # Determine box info.
    ref_row, ref_col = trip_coords[0]
    box_vals = [int(trip_val) for trip_val in trip_vals]
    box_row = ref_row // 3
    box_col = ref_col // 3

    # Go through the box.
    for i in range(3):
        for j in range(3):
            this_row = box_row * 3 + i
            this_col = box_col * 3 + j
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











