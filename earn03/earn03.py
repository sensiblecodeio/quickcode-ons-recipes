from databaker.constants import *

def per_file(tableset):
    return "1. NSA ind monthly figs"

def per_tab(tab):
    obs = tab.filter("CDID").assert_one().fill(RIGHT).fill(DOWN).is_not_blank()

    tab.col('A').dimension(TIME,DIRECTLY, LEFT)
    tab.excel_ref("A3").fill(RIGHT).is_not_blank().dimension('Broad Industry Group', CLOSEST, LEFT)
    tab.excel_ref("B6").expand(RIGHT).parent().is_not_blank().dimension('AWE Breakdown', DIRECTLY, ABOVE)

    return obs
