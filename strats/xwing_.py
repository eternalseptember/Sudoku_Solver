def check_xwing(self):
    """
    X-wing: a candidate in four cells that form a rectangle.
    """
    self.check_xw_by_rows()
    self.check_xw_by_cols()



def check_xw_cands(self, lookup_dict):
    """
    At the end of row or col, check this condition:
    Only two possible cells for a val in this row or col.
    If not met, then remove those entries from xwing consideration.
    """
    remove_list = []

    for poss_val in lookup_dict.keys():
        poss_locs = lookup_dict[poss_val]

        # Add to dict if there are only two possible locations.
        if len(poss_locs) != 2:
            remove_list.append(poss_val)

    # Remove entries.
    for poss_val in remove_list:
        lookup_dict.pop(poss_val)



def reduce_xw_list(self, xwing_candidates):
    """
    Remove unsolved candidates that can't be part of an xwing.
    """
    remove_list = []  # store poss_vals

    for poss_val in xwing_candidates.keys():
        poss_coords = xwing_candidates[poss_val]

        # xwing candidates need at least four possible locations.
        if len(poss_coords) < 4:
            remove_list.append(poss_val)

    # Remove entries.
    for poss_val in remove_list:
        xwing_candidates.pop(poss_val)







