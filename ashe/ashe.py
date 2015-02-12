from databaker.constants import *

def per_file(tabs):
    "ignore tables named Notes or CV Notes"
    tablist = tabs.names  # get a list of names
    tablist.discard('Notes')
    tablist.discard('CV notes')
    return tablist

def per_tab(tab):
    tab.set_header("Table Header", tab.excel_ref("A1").value)
	
    obs = tab.excel_ref("H13").fill(RIGHT).fill(DOWN)

    anchor = tab.filter("18-21 ALL OCCUPATIONS").assert_one()
	
    anchor.shift(RIGHT).fill(DOWN).dimension("SOC", DIRECTLY, LEFT)
    descriptions = anchor.fill(DOWN)
    descriptions.dimension("description", DIRECTLY, LEFT) # feels like this'd make more sense with junction

    percentiles = tab.filter("Percentiles").assert_one().shift(DOWN).fill(RIGHT)
    percentiles.dimension("Percentiles", DIRECTLY, ABOVE)
    
    return obs
