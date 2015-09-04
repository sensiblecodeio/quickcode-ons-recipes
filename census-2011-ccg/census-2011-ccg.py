from databaker.constants import *

def per_file(tableset):
    tablist = tableset.names         # get a list of names
    tablist.discard('Notes and Terms & Conditions')     # remove names from list
    return tablist

def per_tab(tab):
    obs = tab.filter("All Ages").assert_one().shift(DOWN).expand(RIGHT).expand(DOWN).is_number()

    tab.filter("All Ages").expand(RIGHT).dimension('Age group', DIRECTLY, ABOVE)
    tab.filter("Area Code").fill(DOWN).dimension('Area code', DIRECTLY, LEFT)
    tab.filter("Area Name").extrude(2,0).fill(DOWN).is_not_blank().dimension('Area name', DIRECTLY, LEFT)
    tab.dimension('group', tab.name)
    return obs
