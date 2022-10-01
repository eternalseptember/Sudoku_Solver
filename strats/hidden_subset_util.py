# Utility functions for hidden subsets


def format_hidden_subset_info(self, missing_vals_info):
    """
    missing_vals_info is a dict with possible values in each location.
    Format list of possibilties for subset analysis.
    """
    possible_subsets = {}
    for missing_num in missing_vals_info.keys():
        subset_locs = missing_vals_info[missing_num]

        # Formats location of subset into a string.
        subset_str = ''
        for loc in subset_locs:
            if len(subset_str) > 0:
                subset_str += '-'
            loc_row, loc_col = (loc)
            subset_str += '{0},{1}'.format(loc_row, loc_col)


        if subset_str not in possible_subsets:
            possible_subsets[subset_str] = {
                'subset_locs': subset_locs,
                'missing_num': [missing_num]
            }
        else:
            subset_info = possible_subsets[subset_str]
            subset_info['missing_num'].append(missing_num)

    return possible_subsets



def clean_hidden_subset(self, coord, subset_locs, subset_vals):
    """
    Reduces the possible_values of a single cell.
    """
    # Unsolved cell. Could be part of the subset or not.
    if coord in self.possible_values:
        poss_values = self.possible_values[coord]

        if coord in subset_locs:
            # coord IS part of the subset,
            # so keep this coord's poss_vals that are in subset_vals.
            new_poss_vals = \
                [poss_val for poss_val in poss_values if poss_val in subset_vals]
        else:
            # coord is NOT part of the subset,
            # so remove subset_vals from this coord's poss_values.
            new_poss_vals = \
                [poss_val for poss_val in poss_values if poss_val not in subset_vals]

        # new_poss_vals comes from the if/else statement.
        self.possible_values[coord] = new_poss_vals
        self.check_if_solved(coord, new_poss_vals)









