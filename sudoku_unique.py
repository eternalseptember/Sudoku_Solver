# Functions for finding unique possibilities.
# Import into the main sudoku_solver class.


def check_all_unique(self):
	beg_count = 0
	end_count = len(self.solved_list)

	while (end_count - beg_count) > 0:
		beg_count = len(self.solved_list)

		# Check all rows.
		if len(self.solved_list) < 81:
			for row in range(9):
				self.check_unique_row((row, 0))

		# Check all cols.
		if len(self.solved_list) < 81:
			for col in range(9):
				self.check_unique_col((0, col))

		# Check all boxes.
		if len(self.solved_list) < 81:
			for i in [0, 3, 6]:
				for j in [0, 3, 6]:
					coord = (i, j)
					self.check_unique_box(coord)

		end_count = len(self.solved_list)


def check_unique_row(self, coord):
	# Check for unsolved values with only one possible location
	# within the row referenced by coord.
	ref_row, ref_col = coord  # Reference cell
	val_lookup = {}  # {value: [(possible cells)]}

	# List all possible locations of all missing values.
	for i in range(9):
		this_cell = (ref_row, i)
		self.set_lookup_table(this_cell, val_lookup)

	self.solve_lookup_table(val_lookup)


def check_unique_col(self, coord):
	# Check for unsolved values with only one possible location
	# within the col referenced by coord.
	ref_row, ref_col = coord  # Reference cell
	val_lookup = {}  # {value: [(possible cells)]}

	# List all possible locations of all missing values.
	for j in range(9):
		this_cell = (j, ref_col)
		self.set_lookup_table(this_cell, val_lookup)

	self.solve_lookup_table(val_lookup)


def check_unique_box(self, coord):
	# Check for unsolved values with only one possible location
	# within the 3x3 box referenced by coord.
	val_lookup = self.get_box_poss_vals(coord)
	self.solve_lookup_table(val_lookup)


def get_box_poss_vals(self, coord):
	# Generate a lookup table of remaining unsolved values and all of their
	# possible locations within a 3x3 box.
	ref_row, ref_col = coord  # Reference cell
	val_lookup = {}  # {value: [(possible cells)]}

	# Possible values: 0, 1, 2
	box_row = ref_row // 3
	box_col = ref_col // 3

	# List all possible locations of all missing values.
	for i in range(3):
		for j in range(3):
			row = box_row * 3 + i
			col = box_col * 3 + j
			this_cell = (row, col)
			self.set_lookup_table(this_cell, val_lookup)

	return val_lookup


def set_lookup_table(self, coord, lookup_dict):
	# List all possible locations for each missing values.
	if coord in self.possible_values:
		poss_values = self.possible_values[coord]

		for poss_value in poss_values:
			if poss_value not in lookup_dict:
				lookup_dict[poss_value] = [coord]
			else:
				lookup_dict[poss_value].append(coord)


def solve_lookup_table(self, lookup_dict):
	# Does any missing value have only one possible location?
	for poss_value in lookup_dict.keys():
		poss_locs = len(lookup_dict[poss_value])

		if poss_locs == 1:
			new_coord = lookup_dict[poss_value][0]
			self.possible_values[new_coord] = [poss_value]

			# print('{0} is in {1}'.format(poss_value, new_coord))
			self.solved_queue.append(new_coord)

			# Could run this somewhere else.
			self.solve_queue()




