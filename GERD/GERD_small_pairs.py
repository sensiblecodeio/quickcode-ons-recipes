# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 13:49:10 2016

@author: Mike
"""

from __future__ import unicode_literals
from databaker.constants import *


def per_file(tabs):
    return [PARAMS(1), PARAMS(2)]
    

# All of the code for getting random unwanted bits out of obs. Applies to all three runs (1st sheet, and 2 runs on 2nd sheet)
def clean_obs(obs, anchor, tab):

    # Issues with cross shaped data markers again, slice out anything in obs with a blank data header (i.e any data marker fields)
    obs = obs - anchor.expand(RIGHT).is_blank().fill(DOWN)
        
    # Now get rid of everything from one line above the footer
    obs = obs - tab.filter(contains_string('Source: Office for National Statistics')).shift(UP).expand(RIGHT).expand(LEFT).expand(DOWN)
    
    # Cut out any dates we swept up by accident
    obs = obs - anchor.fill(DOWN).is_blank().expand(RIGHT)
    
    return obs    
    
    
    
def per_tab(tab):
    
    # Dictionary holding the varying terminology used by the differet combinations. Also, 3rd variable is dimension name
    terminology =   {
                    '6': 'Funding',
                    '3': 'Funding',    # Unnecessary repition here, but its honestly easier to cut and paste  
                    
                    '5': 'Expenditure',
                    '8': 'Expenditure', 
                    
                    '4': 'Employment',
                    '15': 'Employment',  
                    
                    '9': 'Expenditure',
                    '17': 'Expenditure',   
                    
                    '18': 'Expenditure',
                    '19': 'Expenditure', 
                    }


    # ========================================================================================
    # Code for extracting the 1st of the two sheets

    if tab.name == PARAMS(1):

        #set anchor        
        anchor = tab.excel_ref('B4')
        
        # Capture the time
        anchor.expand(RIGHT).is_not_blank().is_not_whitespace().dimension(TIME, DIRECTLY, ABOVE)

        # Capture the left hand row
        anchor.fill(DOWN).is_not_blank().is_not_whitespace().dimension(terminology[tab.name], DIRECTLY, LEFT)
    
        obs = anchor.fill(RIGHT).is_not_blank().is_not_whitespace().fill(DOWN).is_not_blank().is_not_whitespace()
        tab.dimension("Source", 'Total')
        
        obs = clean_obs(obs, anchor, tab)
        
        if PARAMS(1) in ["3", "6", "4", "15"]:
            # Get the measure type
            # Waffle blanks in C with non blanks in B3
            my_types = anchor.fill(DOWN).is_bold().is_not_blank().is_not_whitespace()
            my_types = my_types - anchor.fill(DOWN).filter(contains_string('TOTAL'))   
            my_types.dimension(STATUNIT, CLOSEST, ABOVE)

        # Get the current/constant price info for tabs 5 and 8
        if PARAMS(1) in ["8", "5"]:
            tab.excel_ref('B').is_bold().filter(contains_string("PRICES")).dimension('Pricing', CLOSEST, ABOVE)            
            
        
        yield obs
        
      
    else:

        # ===================================
        # IF its the 2nd tab
        # extract twice, once for each side
        # ===================================
    
        anchor = tab.excel_ref('B6')
        
        # Loops twice. Once for Civil, Once for each source of funding (e.g once for Civil, once for Defence)
        # Records start ot 2003 so use the 2nd instance of it to divide into two runs    
        date_cells = anchor.expand(RIGHT).is_not_blank().is_not_whitespace()
        for each in date_cells:
            if each.value == 2003:
                key_cell = each
                
        # Capture the time
        anchor.expand(RIGHT).is_not_blank().is_not_whitespace().dimension(TIME, DIRECTLY, ABOVE)

        # Capture the left hand row
        anchor.fill(DOWN).is_not_blank().is_not_whitespace().dimension(terminology[tab.name], DIRECTLY, LEFT)
    
        # Select all the obs then get rid of the obs on the right
        obs = anchor.shift(RIGHT).fill(DOWN).fill(RIGHT).is_not_blank().is_not_whitespace()
        obs = obs - key_cell.shift(LEFT).fill(DOWN).fill(RIGHT)
                
        # Select the Correct terminology
        tab.dimension("Source", "Civil")

        if PARAMS(1) in ["3", "6", "4", "15"]:
            # Measure typeis always value. Need to inlcude here as first segments will have this info
            tab.dimension(STATUNIT, "£ Million")            
            
        obs = clean_obs(obs, anchor, tab)
        
        # Get the current/constant price info for tabs 5 and 8
        if PARAMS(1) in ["8", "5"]:
            tab.excel_ref('B').is_bold().filter(contains_string("PRICES")).dimension('Pricing', CLOSEST, ABOVE) 
                
        yield obs
                

        # ========================================================================================
        # Code for extracting the RIGHT side of the second sheet
                
        anchor = tab.excel_ref('B6')
        
        # Loops twice. Once for Civil, Once for each source of funding (e.g once for Civil, once for Defence)
        # Records start ot 2003 so use the 2nd instance of it to divide into two runs    
        date_cells = anchor.expand(RIGHT).is_not_blank().is_not_whitespace()
        for each in date_cells:
            if each.value == 2003:
                key_cell = each
                
        # Capture the time
        anchor.expand(RIGHT).is_not_blank().is_not_whitespace().dimension(TIME, DIRECTLY, ABOVE)

        # Capture the left hand row
        anchor.fill(DOWN).is_not_blank().is_not_whitespace().dimension(terminology[tab.name], DIRECTLY, LEFT)
    
        # Select all the obs on the LEFT
        obs = key_cell.fill(DOWN).expand(RIGHT).is_not_blank().is_not_whitespace()
                
        # Select the Correct terminology
        tab.dimension("Source", "Defence")

        if PARAMS(1) in ["3", "6", "4", "15"]:
            # Measure typeis always value. Need to inlcude here as first segments will have this info
            tab.dimension(STATUNIT, "£ Million")
                
        obs = clean_obs(obs, anchor, tab)
        
        # Get the current/constant price info for tabs 5 and 8
        if PARAMS(1) in ["8", "5"]:
            tab.excel_ref('B').is_bold().filter(contains_string("PRICES")).dimension('Pricing', CLOSEST, ABOVE) 

        yield obs
 