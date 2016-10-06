# -*- coding: utf-8 -*-
"""
Created on Thursday July 17 10:47:26 2015
@author: Mike

"""

from databaker.constants import *

def per_file(tabs):
    return ["1.01", "1.02"]
    
 
def set_standard_dimensions(tab, i, anchor, output):    
    
    MyDict = {"1.01":"UK Residents", "1.02":"Overseas Residents"}    
    
    MyLists = [["Visitors", MyDict[tab.name], "Count", "1000", "Visits (Thousands)"], \
             ["Nights Stayed", MyDict[tab.name], "Count", "1000000", "Nights (Millions)"], \
             ["Spending", MyDict[tab.name], "Value", "1000000", "Spending (Millions)"]]
             
    # Set common dimensions in function, so we dont have to keep retyping
    
    anchor.expand(RIGHT).dimension("Category", CLOSEST, LEFT)
    anchor.shift(LEFT).fill(DOWN).is_not_blank().dimension(TIME, DIRECTLY, LEFT)
    tab.dimension(MEASURETYPE, MyLists[i][1])
    tab.dimension(UNITMULTIPLIER, MyLists[i][3])
    tab.dimension(UNITOFMEASURE, MyLists[i][4])   
    output.dimension("Output", CLOSEST, ABOVE)
    
def per_tab(tab):
    
    Col_B = tab.excel_ref('B').is_not_blank()       # Get the output and anchor to the second value in B
    count = 0
    for each in Col_B:
        if count == 0:
            output = each
        if count == 1:
            anchor = each
        count += 1

    unwanted = tab.excel_ref('A').filter(contains_string ("verage annual")).expand(RIGHT).expand(DOWN).is_not_blank()

    i = 0
    set_standard_dimensions(tab, i, anchor, output)
    obs = anchor.shift(0, 4).fill(DOWN).is_not_blank() - unwanted           
    yield obs
 
    i = 1
    set_standard_dimensions(tab, i, anchor, output)  
    obs = anchor.shift(3, 4).fill(DOWN).is_not_blank() - unwanted
    yield obs

    i = 2
    set_standard_dimensions(tab, i, anchor, output)
    obs = anchor.shift(6, 4).fill(DOWN).is_not_blank()
    obs = obs - unwanted          
    yield obs
    
    i = 2
    set_standard_dimensions(tab, i, anchor, output)
    obs = anchor.shift(9, 4).fill(DOWN).is_not_blank()
    obs = obs - unwanted          
    yield obs
    
    