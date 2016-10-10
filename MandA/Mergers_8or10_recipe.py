# -*- coding: utf-8 -*-
"""
Created on Wed September 9th 13:55:41 2015

@author: Mike
"""

from __future__ import unicode_literals
from databaker.constants import *

def per_file(tabs):    
    return PARAMS(0)
   
    
def per_tab(tab):    
    
    anchor = tab.excel_ref('C3')
        
    obs = anchor.shift(0, 2).fill(DOWN).expand(RIGHT).is_not_blank()
    obs = obs - tab.excel_ref('R1').expand(DOWN).expand(RIGHT)
    obs = obs - tab.filter(contains_string ('indicates earliest revision')).expand(RIGHT).expand(DOWN)
        
    anchor.expand(RIGHT).is_not_blank().dimension("Category", CLOSEST, LEFT)
    measure_line = anchor.shift(DOWN).expand(RIGHT).is_not_blank()
    measure_line.dimension(MEASURETYPE, DIRECTLY, ABOVE)
        
    obs = obs - measure_line.shift(RIGHT).expand(DOWN)
    
    anchor.shift(LEFT).expand(DOWN).is_bold().dimension("TIME - DELETEME", CLOSEST, ABOVE)
        
    anchor.shift(LEFT).expand(DOWN).is_not_bold().is_not_blank().dimension(TIME, DIRECTLY, LEFT)
    
    yield obs
    

    
