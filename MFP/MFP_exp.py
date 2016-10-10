# -*- coding: utf-8 -*-
"""
Created on Thursday July 13 10:47:26 2015

@author: Mike

"""

from databaker.constants import *


def per_file(tabs):
    return ["Table 1", "Table 2"]
    
def per_tab(tab):
    
    anchor = tab.excel_ref('C').filter(contains_string ("able")).assert_one()

    obs = anchor.shift(0, 2).expand(RIGHT).expand(DOWN).is_not_blank()
    if tab.name == "Table 1":
        unwanted = tab.excel_ref("B").filter(contains_string ("Notes")).expand(RIGHT).expand(DOWN)
        obs = obs - unwanted
        
    anchor.shift(DOWN).expand(RIGHT).is_not_blank().dimension(TIME, DIRECTLY, ABOVE)
    
    Category = anchor.shift(LEFT).fill(DOWN).is_bold().filter(contains_string ("GVA"))
    Category.dimension("Category", CLOSEST, ABOVE)

    anchor.shift(LEFT).fill(DOWN).is_not_blank().is_not_bold().dimension("Industry", DIRECTLY, LEFT)
        
    Type = anchor.shift(LEFT).fill(DOWN).is_not_blank().is_bold() - Category
    Type = Type | anchor.shift(-1, 2)
    Type.dimension("Category 2", CLOSEST, ABOVE)


    yield obs

    
    