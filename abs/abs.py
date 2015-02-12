from databaker.constants import *

def per_file(tabs):
    "ignore tables named Metadata"
    tablist = tabs.names  # get a list of names
    tablist.discard('Metadata')
    return tablist

def per_tab(tab):

    tab.filter("Description").fill(DOWN).is_not_blank.is_header("SIC",UP)
    tab.filter("Sizeband employment").fill(DOWN).is_header("Sizeband",LEFT,strict=True)
    
    tab.set_header(TIME, tab.name)
    
    anchor=tab.filter("Number of Enterprises").assert_one()
    anchor.fill(RIGHT).is_header("Turnover",UP,strict=True)
    
    obs=anchor.shift(DOWN).shift(DOWN).fill(RIGHT).fill(DOWN).is_not_blank
    
    return obs
