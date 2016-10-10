# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:31:27 2015

@author: Mike

The 'b' version of ASHE extraction script. All we want from the file is the oberservations (they are the CV values for the 'a' file).

therefore, everyhting has been stripped from the 'a' script except observations and one holding dimension (itll autofail with no dimensions)

"""

from __future__ import unicode_literals
import sys
from databaker.constants import *

def per_file(tabs):
    return '*'
    
    
def per_tab(tab):
       
    # Skip the notes tab
    if tab.name == 'Notes':
        return    
    if tab.name == 'CV notes':
        return
    # Pointless but required
    tab.dimension('Holding', 'Value')
    
    # Sort out the observations (i.e make sure we dont grab the key by mistake)
    obs = tab.excel_ref('C6').expand(RIGHT).expand(DOWN)
    obs = obs - tab.filter(contains_string ('CV > 10% and <= 20%')).shift(-1, -3).expand(RIGHT).expand(DOWN)
    
    # Now use the last parameter to skim off things below the table
    # PARAMS 8 is Y or N for shiftinh down from PARAMS 6
    if PARAMS(5) == 'N':
        obs = obs - tab.excel_ref('A1').fill(DOWN).filter(contains_string (PARAMS(3))).expand(RIGHT).expand(DOWN)
    else:
        obs = obs - tab.excel_ref('A1').fill(DOWN).filter(contains_string (PARAMS(3))).shift(DOWN).expand(RIGHT).expand(DOWN)

    # Get rid of the top duplicates for tables 20 and 21
    if PARAMS(4) == 'BoldnWhite':
        obs = obs - tab.excel_ref('A12').expand(RIGHT).expand(UP)


    yield obs