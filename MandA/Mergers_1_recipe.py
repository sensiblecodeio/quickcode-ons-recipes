# -*- coding: utf-8 -*-
"""
Created on Wed September 9th 13:55:41 2015

@author: Mike
"""

from __future__ import unicode_literals
from databaker.constants import *

def per_file(tabs):    
    return 'Table 1'
   
    
def per_tab(tab):    
    
    anchor = tab.excel_ref('B3')
    obs = anchor.shift(0, 5).fill(RIGHT).expand(DOWN).is_not_blank()
        
    unwanted = tab.filter(contains_string ('indicates earliest revision')).expand(RIGHT).expand(DOWN)      
    unwanted = unwanted | tab.excel_ref('V1').expand(RIGHT).expand(DOWN)
    unwanted = unwanted | tab.filter(contains_string ('Number')).shift(RIGHT).fill(DOWN)
    unwanted = unwanted | tab.filter(contains_string ('Value')).shift(RIGHT).fill(DOWN)
    obs = obs - unwanted       
        
    anchor.expand(DOWN).is_not_blank().is_not_bold().dimension(TIME, DIRECTLY, LEFT)
    anchor.expand(RIGHT).parent().is_not_blank().dimension('Companies', CLOSEST, LEFT)
    anchor.shift(0, 2).expand(RIGHT).parent().is_not_blank().dimension(MEASURETYPE, CLOSEST, LEFT)
    anchor.shift(DOWN).expand(RIGHT).parent().is_not_blank().dimension('Transaction', CLOSEST, LEFT)
    
    anchor.expand(DOWN).is_not_blank().is_bold().dimension('TIMETYPE', CLOSEST, ABOVE)   
    
    yield obs
    

    
