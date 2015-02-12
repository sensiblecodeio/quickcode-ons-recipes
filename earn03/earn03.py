from databaker.constants import *

def per_file(tableset):
    return "1. NSA ind monthly figs"

def per_tab(tab):
    anchor=tab.filter("CDID").assert_one()
    obs = anchor.shift(DOWN).shift(RIGHT).fill(RIGHT).is_not_blank.fill(DOWN).is_not_blank

    tab.col('A').is_not_blank.dimension(TIME, DIRECTLY, LEFT)
    tab.filter("Agriculture, Forestry and Fishing").fill(LEFT).fill(RIGHT).is_not_blank.dimension('Broad Industry Group', CLOSEST, LEFT)
    anchor.shift(RIGHT).shift(RIGHT).shift(UP).fill(LEFT).fill(RIGHT).is_not_blank.dimension('AWE Breakdown', DIRECTLY, ABOVE)
    return obs
