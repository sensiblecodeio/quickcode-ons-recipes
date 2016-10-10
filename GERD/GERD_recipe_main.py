# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 09:01:00 2016

@author: Mike
"""

from __future__ import unicode_literals
from databaker.constants import *


def per_file(tabs):
    return ['10', '11','12', '13', '14', '16', '24']
    
    
def per_tab(tab):
    
    tab_names = {
                '10':'Current and capital expenditure on R&D',
                '11':'Current expenditure on R&D',
                '12':'Extramural expenditure by R&D by UK Business',
                '13':'Sources of Funds for R&D in UK Business',
                '14':'Employment in R&D for UK Business',
                '16':'Civil and defence R&D expenditure in UK business',
                '24':'R&D Expenditure in UK business (UK or overseas ownership)',
                }

    # Set anchor and obs    
    anchor = tab.excel_ref('B5')
    obs = anchor.fill(RIGHT).fill(DOWN).is_not_blank().is_not_whitespace()     
    
    # Get the industry
    anchor.fill(DOWN).is_not_blank().is_not_whitespace().dimension('Industry', DIRECTLY, LEFT)

    # Extract topic dimmension 2
    # 3 Lines extracted for everything except tables 16 and 24
    if tab.name not in ['16','24']:
        tab.dimension(tab_names[tab.name], [
                                            tab.excel_ref('A4').fill(RIGHT).subdim(DIRECTLY, ABOVE),
                                            tab.excel_ref('A5').fill(RIGHT).subdim(DIRECTLY, ABOVE),
                                            tab.excel_ref('A6').fill(RIGHT).subdim(DIRECTLY, ABOVE)
                                            ])
    else:
        tab.dimension(tab_names[tab.name], [
                                            tab.excel_ref('A4').fill(RIGHT).subdim(DIRECTLY, ABOVE),
                                            tab.excel_ref('A5').fill(RIGHT).subdim(DIRECTLY, ABOVE),
                                            ])      

    # Add the time. It will be provided on the command line
    tab.dimension(TIME, PARAMS(0))

    # Clean some footer data out of obs
    obs = obs - tab.filter(contains_string('Source: Office for National Statistics')).expand(LEFT).expand(DOWN)
    
    # Get rid of addional obs captured as a result of 14 having three line headings
    if tab.name == '14':
        obs = obs - tab.excel_ref('B6').expand(RIGHT)

    yield obs
    
    