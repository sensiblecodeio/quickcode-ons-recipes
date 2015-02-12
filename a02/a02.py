from databaker.constants import *

def per_file(tableset):
    return "*"

def per_tab(tab):
    obs = tab.filter("MGSL").assert_one().shift(DOWN).fill(RIGHT).fill(DOWN).filter(is_number).is_not_italic

    tab.col('A').one_of(['Male', 'Female', 'All Persons']).dimension('gender', CLOSEST, ABOVE)
    tab.col('A').regex("...-... (?:19|20)\d\d").dimension(TIME, DIRECTLY, LEFT)
    tab.regex("All aged .*").dimension('ages', CLOSEST, UP)
    tab.filter("Total economically active").fill(LEFT).fill(RIGHT).is_not_blank.dimension('indicator', DIRECTLY, ABOVE)

    tab.set_header('adjusted_yn', tab.name)
    return obs
