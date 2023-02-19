# Info

* Coordinates are formatted in this order: (row, col)
* Index range is [0, 8], where (0, 0) is the top left corner.
* Folder root contains the most basic core of solving and printing the sudoku board to the terminal.
* More advanced strategies are in the strats folder.
* Executable tests are in the test folder. Text files of test boards are in the test_boards folder.

## Definitions (used for this project)

* Naked Pair: Two cells in a group contain an identical pair of candidates and only those two candidates.
* Hidden Pair: Two cells in a group contain a pair of candidates (hidden amongst other candidates) that are not found in any other cells in that group.
* Naked Triple: Three cells in a group contain no candidates other than the same three candidates. The cells DON'T have to contain every candidate of the triple.
* Hidden Triple: Three candidates are restricted to three cells in a given group. All other candidates in those three cells can be excluded.
* X-wing is 2x2.
* Swordfish is 3x3.
