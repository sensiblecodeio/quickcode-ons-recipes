# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 13:49:10 2016

@author: Mike
"""

from __future__ import unicode_literals
from databaker.constants import *


def per_file(tabs):
    return [PARAMS(1), PARAMS(2)]
           
    
def per_tab(tab):

    whats_my_dimension = {
                          '18':'Region',
                          '19':'Region',
                          '21':'Sizeband',
                          '22':'Sizeband',
                         }
                         
    # NOT using an anchor as the point it changes slightly between the 2 datasets, works better as an absolute
              
    obs = tab.excel_ref('B7').fill(RIGHT).expand(DOWN).is_not_blank().is_not_whitespace()
    
    tab.excel_ref('B7').expand(DOWN).is_not_blank().is_not_whitespace().dimension('R&D', DIRECTLY, LEFT)    

    tab.dimension(whats_my_dimension[tab.name], [
                                                tab.excel_ref('B4').expand(RIGHT).subdim(DIRECTLY, ABOVE),  
                                                tab.excel_ref('B5').expand(RIGHT).subdim(DIRECTLY, ABOVE),
                                                tab.excel_ref('B6').expand(RIGHT).subdim(DIRECTLY, ABOVE),  
                                               ])
    
    # Add the time. It will be provided on the command line
    tab.dimension(TIME, PARAMS(0))
    
    # Get the statunit
    tab.excel_ref('A3').expand(RIGHT).is_not_blank().is_not_whitespace().dimension(STATUNIT, CLOSEST, ABOVE)
    
    # Now get rid of everything from one line above the footer
    obs = obs - tab.filter(contains_string('Source: Office for National Statistics')).shift(UP).expand(RIGHT).expand(LEFT).expand(DOWN)

    yield obs
 