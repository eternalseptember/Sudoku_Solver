# Functions that print the state of the game.
# Import into the main sudoku_solver class.


def print_board(self):
	print()
	for row in range(9):
		if (row > 0) and (row % 3 == 0):
			print('-----------------------')

		for col in range(9):
			if (col == 0):
				print(' ', end='')
			elif (col % 3 == 0):
				print('| ', end='')

			print(self.board[row][col], end=' ')

		print()
	print()


def print_possible_values(self):
	print('Possible values:')
	for coord in self.possible_values.keys():
		possibilities = self.possible_values[coord]
		print('{0}: {1}'.format(coord, possibilities))
	print()


def print_solved_queue(self):
	print('Solved queue:', end=' ')
	for coord in self.solved_queue:
		print(coord, end=' ')
	print()



