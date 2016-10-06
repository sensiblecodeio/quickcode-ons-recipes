# -*- coding: utf-8 -*-
"""
Created on Wed September 9th 13:55:41 2015

@author: Mike
"""

from __future__ import unicode_literals
from databaker.constants import *

def per_file(tabs):    
    return "Table 9"
   
    
def per_tab(tab):    
    
    anchor = tab.filter(contains_string ('Total')).assert_one()

    anchor.shift(0, -2).expand(RIGHT).is_not_blank().dimension("Expenditure", CLOSEST, LEFT)
    anchor.shift(0, -1).expand(RIGHT).is_not_blank().dimension("Expenditure 1", CLOSEST, LEFT)
    anchor.expand(RIGHT).is_not_blank().dimension("Expenditure 2", CLOSEST, LEFT)
    
    anchor.shift(LEFT).expand(DOWN).is_not_blank().dimension(TIME, DIRECTLY, LEFT)    

    anchor.shift(LEFT).expand(DOWN).is_bold().dimension("ExtraTime", CLOSEST, ABOVE)

    # Get obs,and get rid of lots of crap    
    obs = anchor.shift(0, 2).fill(DOWN).expand(RIGHT).is_not_blank()
    obs = obs - tab.excel_ref("V1").expand(DOWN).expand(RIGHT)
    obs = obs - tab.filter(contains_string ("earliest revision")).expand(RIGHT).expand(DOWN)
    obs = obs - anchor.expand(RIGHT).is_not_blank().shift(RIGHT).fill(DOWN)

    yield obs
    

    
