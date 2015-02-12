from databaker.constants import *

def per_file(tableset):
    return "1. NSA ind monthly figs"

def per_tab(tab):
    anchor=tab.filter("CDID").assert_one()
    obs = anchor.shift(DOWN).shift(RIGHT).fill(RIGHT).fill(DOWN)

    tab.col('A').is_header(TIME,LEFT, strict=True)
    tab.filter("Agriculture, Forestry and Fishing").fill(LEFT).fill(RIGHT).is_not_blank.is_header('Broad Industry Group', LEFT)
    anchor.shift(RIGHT).shift(RIGHT).shift(UP).fill(LEFT).fill(RIGHT).is_not_blank.is_header('AWE Breakdown', UP, strict=True)

    return obs
