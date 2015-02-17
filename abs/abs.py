from databaker.constants import *

def per_file(tabs):
    "ignore tables named Metadata"
    tablist = tabs.names  # get a list of names
    tablist.discard('Metadata')
    return tablist

def per_tab(tab):

    tab.filter("Description").fill(DOWN).is_not_blank().dimension("SIC",CLOSEST,ABOVE)
    tab.filter("Sizeband employment").fill(DOWN).dimension("Sizeband",DIRECTLY,LEFT)

    tab.dimension(TIME, tab.name)

    anchor=tab.filter("Number of Enterprises").assert_one()
    anchor.fill(RIGHT).dimension("Turnover",DIRECTLY,ABOVE)

    obs=anchor.shift(DOWN).shift(DOWN).fill(RIGHT).fill(DOWN).is_not_blank()

    return obs
