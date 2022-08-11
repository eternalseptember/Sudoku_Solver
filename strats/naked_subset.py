# Functions that eliminate possibilities based on matching pairs (or triplets).
# Focused on finding pairs. Triplets can be found incidentally.
# Naked: EXACT list of candidates in EXACT cells.


def check_matching_sets(self):
	# Run this if checking unique doesn't solve everything.
	self.check_matching_cols()
	self.check_matching_rows()


def check_matching_cols(self):
	# Search each col for matching pairs/triplets.
	for col in range(9):
		col_missing_vals = {}

		# Collect all the missing value combinations in this col.
		for j in range(9):  # j goes down
			this_cell = (j, col)
			self.set_missing_val_table(this_cell, col_missing_vals)

		# Search this col's tally for pair/triplet matches.
		matches_vals, matches_locs = self.find_matches(col_missing_vals)

		# If there are matching sets, remove values as possibilities in other
		# boxes outside the set/pair/triplet.
		if len(matches_vals) > 0:
			for match in matches_vals:
				# Reduce within col.
				for j in range(9):  # j goes down
					this_cell = (j, col)
					self.remove_matching_sets(this_cell, match, 'col')

				# Reduce within box.
				self.remove_in_box(match, matches_locs)

			# If anything's been reduced to one possibility:
			self.solve_queue()


def check_matching_rows(self):
	# Search each row for matching pairs/triplets.
	for row in range(9):
		row_missing_vals = {}

		# Collect all the missing value combinations in this row.
		for i in range(9):  # i goes across
			this_cell = (row, i)
			self.set_missing_val_table(this_cell, row_missing_vals)

		# Search this row's tally for pair/triplet matches.
		matches_vals, matches_locs = self.find_matches(row_missing_vals)

		# If there are matching sets, remove values as possibilities in other
		# boxes outside the set/pair/triplet.
		if len(matches_vals) > 0:
			for match in matches_vals:
				# Reduce within row.
				for i in range(9):  # i goes across
					this_cell = (row, i)
					self.remove_matching_sets(this_cell, match, 'row')

				# Reduce within box.
				self.remove_in_box(match, matches_locs)

			# If anything's been reduced to one possibility:
			self.solve_queue()


def set_missing_val_table(self, coord, missing_val_dict):
	# Tallies the combinations of missing values in each area.
	if coord in self.possible_values:
		poss_values = self.possible_values[coord]

		# Convert to hashable key.
		poss_str = ''.join(map(str, poss_values))

		# Tally combinations of missing values.
		if poss_str not in missing_val_dict:
			missing_val_dict[poss_str] = [coord]
		else:
			missing_val_dict[poss_str].append(coord)


def find_matches(self, missing_val_dict):
	# Search the dictionary of missing values for matches between
	# possible values in a cell and
	# the number of cells with that exact list of possibilities.
	# Also keep track of matches' locations.
	matches_vals = []
	matches_locs = {}

	for missing_val in missing_val_dict.keys():
		if len(missing_val) == len(missing_val_dict[missing_val]):
			# Turn missing_val hash back into a list.
			missing_val_list = [int(val) for val in missing_val]
			matches_vals.append(missing_val_list)
			matches_locs[missing_val] = missing_val_dict[missing_val]

	return matches_vals, matches_locs


def in_same_box(self, coords_list):
	# Checks whether all values in match are in the same box.
	# coords_list is all of the cells in the match, sharing the same
	# list of possible values.
	# box_loc = (box_row, box_col)
	boxes = []

	for coord in coords_list:
		ref_row, ref_col = coord
		box_row = ref_row // 3
		box_col = ref_col // 3
		box = (box_row, box_col)
		boxes.append(box)

	# Are they all in the same box?
	# And if they are, which box?
	if len(set(boxes)) == 1:
		return True, boxes[0]
	else:
		return False, None


def remove_in_box(self, match, match_dict):
	# match is the list of values in the pair/triplet/set.
	# match_dict keeps track of where the match is with a hashable key.
	# If cells of the match are in the same box, then remove those values
	# as possibilities from the rest of the box.
	match_str = ''.join(map(str, match))
	match_loc = match_dict[match_str]
	is_same_box, box_loc = self.in_same_box(match_loc)

	if is_same_box:
		box_row, box_col = box_loc

		for i in range(3):
			for j in range(3):
				row = box_row * 3 + i
				col = box_col * 3 + j
				this_cell = (row, col)
				self.remove_matching_sets(this_cell, match, 'box')


def remove_matching_sets(self, coord, matched_set, label=''):
	# matched_set is a list of values in the pair/triplet/set.
	if coord in self.possible_values:
		poss_values = self.possible_values[coord]

		if poss_values == matched_set:
			# Don't want to erase the match.
			# print('{0} match found: {1} at {2}'
			# 	.format(label, matched_set, coord))
			return
		else:
			# Remove any values in the matched set.
			for val in matched_set:
				if val in poss_values:
					poss_values.remove(val)

			# Check if solved.
			self.check_if_solved(coord, poss_values)
















