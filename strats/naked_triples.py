# Checks naked triples in rows, cols, and boxes.

# Naked triple:
# Not all cells must contain all three candidates, but there must not be more
# than three candidates in the three cells all together.



def check_naked_triples(self):
	self.check_naked_triples_rows()
	self.check_naked_triples_cols()



def check_naked_triples_rows(self):
	# Iterate through each row to find naked triples.
	for j in range(9):  # j is row number
		self.check_naked_triples_row(j)

	self.solve_queue()



def check_naked_triples_row(self, row_num):
	# Collect candidate cells and their possibilities.
	poss_trip_list = []

	# Get a list of cells that can be part of a triple.
	for i in range(9):  # i is col number
		this_cell = (row_num, i)

		# Skip over solved cells.
		if this_cell in self.possible_values:
			poss_vals = self.possible_values[this_cell]

			# Can't be part of a triple if there are more than 3 candidates.
			if len(poss_vals) <= 3:
				poss_trip_list.append(this_cell)

	# Analyze if triple exists.
	poss_trips_info = self.find_naked_triples(poss_trip_list, 'check_row')
	self.clean_triple_row(poss_trips_info, row_num)



def clean_triple_row(self, poss_trips_info, row_num):
	# Remove trip possibilities in cells that are not part of the triple.
	for item in poss_trips_info.keys():

		# Decode key and turn it back into a list of numbers.
		trip_set = [int(trip_val) for trip_val in item]
		coords_set = poss_trips_info[item]

		# Remove trip values from cells not part of triple.
		for i in range(9):  # i is col number
			this_cell = (row_num, i)

			# Skip over cells that are part of this triple.
			if this_cell not in coords_set:
				if this_cell in self.possible_values:

					# Remove vals in trip_set from this cell's possible vals.
					poss_vals = self.possible_values[this_cell]

					for trip_val in trip_set:
						if trip_val in poss_vals:
							poss_vals.remove(trip_val)

					# Then check if this_cell has been solved.
					self.check_if_solved(this_cell, poss_vals)







def check_naked_triples_cols(self):
	# Iterate through each col to find naked triples.
	for i in range(9):  # i is col number
		self.check_naked_triples_col(i)

	self.solve_queue()



def check_naked_triples_col(self, col_num):
	# Collect candidate cells and their possibilities.
	poss_trip_list = []

	# Get a list of cells that can be part of a triple.
	for j in range(9):
		this_cell = (j, col_num)

		# Skip over solved cells.
		if this_cell in self.possible_values:
			poss_vals = self.possible_values[this_cell]

			# Can't be part of a triple if there are more than 3 candidates.
			if len(poss_vals) <= 3:
				poss_trip_list.append(this_cell)

	# Analyze if triple exists.
	poss_trips_info = self.find_naked_triples(poss_trip_list, 'check_col')
	self.clean_triple_col(poss_trips_info, col_num)



def clean_triple_col(self, poss_trips_info, col_num):
	# Remove trip possibilities in cells that are not part of the triple.
	for item in poss_trips_info.keys():

		# Decode key and turn it back into a list of numbers.
		trip_set = [int(trip_val) for trip_val in item]
		coords_set = poss_trips_info[item]

		# Remove trip values from cells not part of triple.
		for j in range(9):  # j is row number
			this_cell = (j, col_num)

			# Skip over cells that are part of this triple.
			if this_cell not in coords_set:
				if this_cell in self.possible_values:

					# Remove vals in trip_set from this cell's possible vals.
					poss_vals = self.possible_values[this_cell]

					for trip_val in trip_set:
						if trip_val in poss_vals:
							poss_vals.remove(trip_val)

					# Then check if this_cell has been solved.
					self.check_if_solved(this_cell, poss_vals)







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
	# will be passed a list of keys of triple boxes

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












