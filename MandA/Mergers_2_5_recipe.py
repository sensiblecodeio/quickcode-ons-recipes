# -*- coding: utf-8 -*-
"""
Created on Wed September 9th 13:55:41 2015

@author: Mike
"""

from __future__ import unicode_literals
from databaker.constants import *

def per_file(tabs):    
    return ['Table 2', 'Table 3', 'Table 4', 'Table 5']
   
    
def per_tab(tab):    
    
    anchor = tab.excel_ref('B3')
    obs = anchor.shift(0, 5).fill(RIGHT).expand(DOWN).is_not_blank()
        
    unwanted = tab.filter(contains_string ('indicates earliest revision')).expand(RIGHT).expand(DOWN)      
    unwanted = unwanted | tab.excel_ref('V1').expand(RIGHT).expand(DOWN)
    unwanted = unwanted | tab.filter(contains_string ('Number')).shift(RIGHT).fill(DOWN)
    unwanted = unwanted | tab.filter(contains_string ('Value')).shift(RIGHT).fill(DOWN)
    obs = obs - unwanted       
        
    anchor.expand(DOWN).is_not_blank().is_not_bold().dimension(TIME, DIRECTLY, LEFT)
    
    anchor.expand(RIGHT).parent().is_not_blank().dimension('Category', CLOSEST, LEFT)
    inv1 = anchor.shift(DOWN).expand(RIGHT).parent().is_not_blank()
    inv1 = inv1 | tab.excel_ref('B4')
    inv1.dimension('Investment', CLOSEST, LEFT)
    
    anchor.shift(0, 2).expand(RIGHT).parent().is_not_blank().dimension(MEASURETYPE, CLOSEST, LEFT)    
    
    tab.excel_ref('C1').dimension('Category', CLOSEST, ABOVE)
    
    

    anchor.shift(0, 2).expand(RIGHT).parent().is_not_blank().dimension("Measure", CLOSEST, LEFT)
    
    
    yield obs
    

    
