# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:31:27 2015

@author: Mike
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
    
    # Get the time out of the filename
    if sys.argv[1] == '--preview':
        filename = sys.argv[3]
    else:
        filename = sys.argv[2]
    filename = filename[:-4]
    if filename[:-2] == 'CV':
        filename = filename[:-3]
    year = filename[-4:]
    tab.dimension(TIME, year)

    # Set the earnings/hours dimension to whatever the tables uniquely measuring
    # example 'Paid Hours Worked'
    tab.dimension('Earnings', PARAMS(0))

    # Iterate and scrape the required header rows
    use_row = 1
    for x in range(3, 6):
        tab.excel_ref(str(x)).dimension("Default Title " + str(use_row), DIRECTLY, ABOVE)
        use_row = use_row + 1
        
    # Populate sex based on tab name    
    if 'Female' in tab.name:
        Sex = 'Female'
    elif 'Male' in tab.name:
        Sex = 'Male'
    else:
        Sex = 'All'
    tab.dimension("Sex", Sex)
    
    # Populate Work time based on tab.name    
    if 'Full-Time' in tab.name:
        Working_Pattern = 'Full-Time'
    elif 'Part-Time' in tab.name:
        Working_Pattern = 'Part-Time'
    else:
        Working_Pattern = 'All'
    tab.dimension("Working Pattern", Working_Pattern) 

    # Capture column A based on how the data is represented
    # i.e bold and indentation denotes or can denote a hierarcial relationship
    if PARAMS(4) == 'NoBold' or PARAMS(4) == 'NoBoldClipped':
        # It's a Geography one.
        # Take the first and second columns with names provide by PARAMS
        tab.excel_ref('A6').expand(DOWN).dimension(PARAMS(4), DIRECTLY, LEFT)
        tab.excel_ref('B6').expand(DOWN).dimension(PARAMS(5), DIRECTLY, LEFT)
    elif PARAMS(4) == 'Bold':
        # Decription Hierarchy marked by Bold. Gonna Take some fixing
        tab.excel_ref('A6').expand(DOWN).is_bold().is_not_blank().dimension(PARAMS(1), CLOSEST, ABOVE)
        tab.excel_ref('A6').expand(DOWN).is_not_blank().dimension(PARAMS(2) + ' 1', DIRECTLY, LEFT)
        tab.excel_ref('B6').expand(DOWN).dimension(PARAMS(2), DIRECTLY, LEFT)
    elif PARAMS(4) == 'BoldnWhite':
        # Hierarchy created from a mix of Bold and Whitespace indentation (2 spaces)
        tab.excel_ref('A6').expand(DOWN).is_bold().is_not_blank().dimension(PARAMS(2), CLOSEST, ABOVE)
        tab.excel_ref('A6').expand(DOWN).is_not_blank().spaceprefix(3).dimension(PARAMS(2) + ' 1', CLOSEST, ABOVE)
        tab.excel_ref('A6').expand(DOWN).is_not_blank().spaceprefix(3).dimension(PARAMS(2) + ' 2', CLOSEST, ABOVE) # irrelivent?
        tab.excel_ref('B6').expand(DOWN).dimension(PARAMS(2) + ' 3', DIRECTLY, LEFT)
     
    # Sort out the observations (i.e make sure we dont grab the key by mistake)
    obs = tab.excel_ref('C6').expand(RIGHT).expand(DOWN)
    obs = obs - tab.filter(contains_string ('CV > 10% and <= 20%')).shift(-1, -3).expand(RIGHT).expand(DOWN)
    
    # Now use the last parameter to skim off things below the table
    if PARAMS(5) == 'N':
        obs = obs - tab.excel_ref('A1').fill(DOWN).filter(contains_string (PARAMS(3))).expand(RIGHT).expand(DOWN)
    else:
        obs = obs - tab.excel_ref('A1').fill(DOWN).filter(contains_string (PARAMS(3))).shift(DOWN).expand(RIGHT).expand(DOWN)

    # Get rid of the top duplicates for tables 20 and 21
    if PARAMS(4) == 'BoldnWhite':
        obs = obs - tab.excel_ref('A12').expand(RIGHT).expand(UP)
        
    # Get rid of the top duplicates for tables 12 and 12
    if PARAMS(4) == 'NoBoldClipped':
        obs = obs - tab.excel_ref('A13').expand(RIGHT).expand(UP) 

    yield obs
