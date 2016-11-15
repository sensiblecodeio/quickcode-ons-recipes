# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 13:55:41 2015

@author: Mike
"""

from __future__ import unicode_literals
from databaker.constants import *

def per_file(tabs):    
    return ["2.3", "3.3", "4.3"]
    
def per_tab(tab):
    
    anchor = tab.filter(contains_string (' fishing')).assert_one()
    
    obs = anchor.fill(DOWN).expand(RIGHT).is_not_blank()
    unwanted = tab.filter(contains_string ('Source: Office'))
    obs = obs-unwanted

    anchor.shift(LEFT).expand(DOWN).is_not_blank().dimension(TIME, DIRECTLY, LEFT)

    anchor.expand(RIGHT).parent().is_not_blank().dimension("Investment", DIRECTLY, ABOVE)
    
    tab.dimension(PARAMS(0), PARAMS(1))    
    
    tab.excel_ref('A2').dimension('Type', CLOSEST, ABOVE)    
    
    tab = waterfall(tab)
    
    yield obs
   
   
"""
Standardcode for extracting "waterfall" type geography presentation. This is the same for every recipe
"""

def remove_below(bag, tab):
    """ Custom function. If the bag has two cells touching each other vertically get rid of the lower one"""
    
    previous_y = -2     # we're looking for vertical repeats, -2 is outside the 0 indexed axis so will do to start us off
    droplist = []       # for y property (think "row number" + 1) of the cells we're chucking


    # extrude to grab any 2 line area names
    for cell in bag:
        cell = cell.extrude(1,0)        

    # now get rid of and duplicates
    for cell in bag:
        if (cell.y - 1) == previous_y:
            droplist.append(cell.y + 1)            
        previous_y = cell.y
        
    for _y in droplist:
        bag = bag - tab.excel_ref('A' + str(_y)).expand(RIGHT)

    return bag
    
    
def waterfall(tab):
    
    # Get A
    colA = remove_below(tab.excel_ref('A').is_not_blank().is_not_whitespace(), tab)
    
    # Get B
    colB = remove_below(tab.excel_ref('B').is_not_blank().is_not_whitespace(), tab)
    colB = colB | colA.shift(RIGHT)
    colB = colB - colB.filter(contains_string("of which"))
    # Get C
    colC = remove_below(tab.excel_ref('C').is_not_blank().is_not_whitespace(), tab)
    colC = colC | colB.shift(RIGHT)    
    
    tab.dimension("Area", [
                colA.subdim(CLOSEST, ABOVE),
                colB.subdim(CLOSEST, ABOVE),
                colC.subdim(CLOSEST, ABOVE)    
                ])
    
    return tab
    
