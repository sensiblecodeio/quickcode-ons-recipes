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
     
    my_dict = {"6A_Top": 'CBAQ', "6A_Bottom": 'HCL3', "6D_Top": 'CBAS', "6D_Bottom":'HCL5',
               "7A_Top": 'CBAU', "7A_Bottom": 'HCK7', "7D_Top": 'CBAW', "7D_Bottom":'HCK9',
    }

    anchor = tab.filter(contains_string (my_dict[PARAMS(1)]))
    obs = anchor.shift(DOWN).expand(RIGHT).expand(DOWN).is_not_blank()

    # Getting all the junk out of the file
    unwanted = tab.excel_ref('AA1').expand(DOWN).expand(RIGHT)     
    unwanted = unwanted | anchor.expand(DOWN).filter(contains_string ('Area Analysis')).expand(RIGHT).expand(DOWN)
    unwanted = unwanted | tab.filter(contains_string ('indicates earliest revision')).expand(RIGHT).expand(DOWN)
    unwanted = unwanted | anchor.expand(DOWN).filter(contains_string ('Number')).shift(UP).expand(RIGHT).expand(DOWN)
    obs = obs - unwanted    
    
    # Dimension etc
    anchor.shift(0, -2).expand(RIGHT).is_not_blank().dimension("Area", CLOSEST, LEFT)
    anchor.shift(0, -1).expand(RIGHT).is_not_blank().dimension(MEASURETYPE, DIRECTLY, ABOVE)
    anchor.shift(-1, 0).expand(DOWN).is_not_blank().dimension(TIME, DIRECTLY, LEFT)        
    
    cat = tab.filter(contains_string (PARAMS(1)[0:2])).shift(RIGHT)
    cat.dimension("Mergers", CLOSEST, ABOVE)

    tab.dimension("Companies", "TempValue")
    
    yield obs
