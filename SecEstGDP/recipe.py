# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 10:26:02 2015

@author: Mike
"""

from __future__ import unicode_literals
from databaker.constants import *


def per_file(tabs):
    return [PARAMS(0), PARAMS(1)]
    # , 'B1 CVM OUTPUT', 'B2 CVM OUTPUT', 'C1 EXPENDITURE', 'C2 EXPENDITURE', 'D INCOME', 'L GVAbp', 'M Alignment adjustments']
    #return ['N Financial Year Variables']
    
def per_tab(tab):
    
    # If we only have 1 tab to scrape, we pass the Content tab as the second PARAM - so its returned straight away
    if tab == 'None':
        return

    if tab.name == 'Content':
        return
    
    # Make Dictionary showing byindex number to use for different tabs    
    skipcount = {
                'A1 AGGREGATES':1, 'A2 AGGREGATES':1, 'B1 CVM OUTPUT':2, 'B2 CVM OUTPUT':2, 'C1 EXPENDITURE':1, 'C2 EXPENDITURE':1,  
                'D INCOME':1, 'L GVAbp':1, 'M Alignment adjustments':1, 'N Financial Year Variables':1, 'O Selected imp def':1, 
                'P GDP per head':1, 'H1 TRADE':1 ,'H2 TRADE':1}
    
    # Use a dictionary to specifiy the non-percentage measuretype.
    mtype = {
                'A1 AGGREGATES':'Number', 'A2 AGGREGATES':'Value', 'B1 CVM OUTPUT':'Number', 'B2 CVM OUTPUT':'Number', 'C1 EXPENDITURE':'Value', 'C2 EXPENDITURE':'Value',  
                'D INCOME':'Value', 'L GVAbp':'Number', 'M Alignment adjustments':'Value', 'N Financial Year Variables':'Value', 'O Selected imp def':'Number', 
                'P GDP per head':'Number', 'H1 TRADE':'Value' ,'H2 TRADE':'Value'}    
    
    # Skip if we're looking at the Index or Content sections    
    if tab.name == 'Index' or tab.name == ' Contents':
        return
    else:
        # Anchor and Obs 
        anchor = tab.excel_ref('A2').expand(DOWN).is_not_blank().is_not_whitespace().by_index(skipcount[tab.name])
        obs = anchor.fill(RIGHT).expand(DOWN).is_not_blank().is_not_whitespace()
    
        for x in range(0, 2):
            
            # The itteration will determine which columns we're extracting and whether we look LEFT or RIGHT for the dimension
            if x == 0:
                direction = LEFT
            elif x == 1:
                direction = RIGHT
               
            
            # MEAURETYPE IS ALWAYS FIXED. TAKEN FROM mtype dictionary            
            tab.dimension(MEASURETYPE, mtype[tab.name])            
            
            
            """
            HEADING DIMENSIONS - 
            """
            if tab.name == 'A1 AGGREGATES' or tab.name == 'A2 AGGREGATES':
                    tab.dimension('Category', [
                        tab.excel_ref('A2').expand(RIGHT).is_not_blank().is_not_whitespace().parent().subdim(CLOSEST, direction),
                        tab.subdim(' - '),
                        tab.excel_ref('A3').expand(RIGHT).is_not_blank().is_not_whitespace().subdim(DIRECTLY, ABOVE)
                        ])
                    if tab.name == 'A1 AGGREGATES':
                        if x == 0:
                            obs = obs - (tab.excel_ref('F1').fill(DOWN) | tab.excel_ref('J1').fill(DOWN))
                        else:
                            obs = tab.excel_ref('F1') | tab.excel_ref('J1')
                            obs = obs.waffle(anchor.fill(DOWN).is_not_bold().is_not_blank().is_not_whitespace())
                    if tab.name == 'A2 AGGREGATES':
                        if x == 0:
                            obs = obs - (tab.excel_ref('C1').fill(DOWN) | tab.excel_ref('G1').fill(DOWN))
                            obs = obs.is_not_blank().is_not_whitespace()
                        else:
                            obs = tab.excel_ref('C1') | tab.excel_ref('G1')
                            obs = obs.waffle(anchor.fill(DOWN).is_not_bold().is_not_blank().is_not_whitespace())
                            obs = obs.is_not_blank().is_not_whitespace()
                     
                     
            if tab.name == 'B1 CVM OUTPUT' or tab.name == 'B2 CVM OUTPUT':
                    # Deliberatly add some blank cells to the bag where we'd get a NoLookupError.
                    top = tab.excel_ref('A2').expand(RIGHT).is_not_blank().is_not_whitespace().parent()
                    top = top | tab.excel_ref('C2') | tab.excel_ref('O2') | tab.excel_ref('AA2') | tab.excel_ref('AC2')
                    tab.dimension('Category', [
                        top.subdim(CLOSEST, direction),
                        tab.subdim(' - '),
                        tab.excel_ref('A3').expand(RIGHT).is_not_blank().is_not_whitespace().subdim(DIRECTLY, ABOVE)
                        ])                                           
                    if tab.name == 'B1 CVM OUTPUT':
                        if x == 0:
                            obs = obs - (tab.excel_ref('E1').fill(DOWN) | tab.excel_ref('Q1').fill(DOWN) | tab.excel_ref('S1').fill(DOWN))
                        else:
                            obs = tab.excel_ref('E1') | tab.excel_ref('Q1') | tab.excel_ref('S1')
                            obs = obs.waffle(anchor.fill(DOWN).is_not_bold().is_not_blank().is_not_whitespace())
                    if tab.name == 'B2 CVM OUTPUT':
                        if x == 0:
                            obs = obs.is_not_blank().is_not_whitespace()
                        else:
                            return # Only one pass needed
                    
                    
            if tab.name == 'C1 EXPENDITURE' or tab.name == 'C2 EXPENDITURE':
                    # Add some blanks to headert lines 1 and 2 so we dont get lookuperrors
                    h1 = tab.excel_ref('A2').expand(RIGHT).is_not_blank().is_not_whitespace().parent() | tab.excel_ref('L2') | tab.excel_ref('C2')
                    h2 = tab.excel_ref('A3').expand(RIGHT).is_not_blank().is_not_whitespace() | tab.excel_ref('K3')                    
                    tab.dimension('Category', [
                        h1.subdim(CLOSEST, direction),
                        tab.subdim(' - '),
                        h2.subdim(CLOSEST, direction),
                        tab.subdim(' - '),
                        tab.excel_ref('A4').expand(RIGHT).is_not_blank().is_not_whitespace().subdim(DIRECTLY, ABOVE)
                        ])
                    if x == 0:
                        obs = obs - (tab.excel_ref('C1').fill(DOWN) | tab.excel_ref('G1').fill(DOWN))
                    else:
                        obs = tab.excel_ref('C1') | tab.excel_ref('G1')
                        obs = obs.waffle(anchor.fill(DOWN).is_not_bold().is_not_blank().is_not_whitespace())


            if tab.name == 'D INCOME':
                    h1 = tab.excel_ref('A2').expand(RIGHT).is_not_blank().is_not_whitespace().parent() | tab.excel_ref('C2') | tab.excel_ref('F2')                  
                    tab.dimension('Category', [
                        h1.subdim(CLOSEST, direction),
                        tab.subdim(' - '),
                        tab.excel_ref('A3').expand(RIGHT).is_not_blank().is_not_whitespace().subdim(DIRECTLY, ABOVE)
                        ])
                    if x == 0:
                        obs = obs - tab.excel_ref('D1').fill(DOWN)
                    else:
                        obs = tab.excel_ref('D1')
                        obs = obs.waffle(anchor.fill(DOWN).is_not_bold().is_not_blank().is_not_whitespace())               


            if tab.name == 'H1 TRADE' or tab.name == 'H2 TRADE':
                    if tab.name == 'H1 TRADE':
                        tab.dimension('Category', [
                            tab.excel_ref('A2').expand(RIGHT).is_not_blank().is_not_whitespace().parent().subdim(CLOSEST, direction),
                            tab.subdim(' - '),
                            tab.excel_ref('A3').expand(RIGHT).is_not_blank().is_not_whitespace().subdim(DIRECTLY, ABOVE)
                            ])
                        if x == 0:
                            obs = obs - (tab.excel_ref('C1').fill(DOWN) | tab.excel_ref('G1').fill(DOWN) | tab.excel_ref('K1').fill(DOWN))
                        else:
                            obs = tab.excel_ref('C1') | tab.excel_ref('G1') | tab.excel_ref('K1')
                            obs = obs.waffle(anchor.fill(DOWN).is_not_bold().is_not_blank().is_not_whitespace())
                    if tab.name == 'H2 TRADE':
                        tab.dimension('Category', [
                            tab.excel_ref('A3').expand(RIGHT).is_not_blank().is_not_whitespace().parent().subdim(CLOSEST, direction),
                            tab.subdim(' - '),
                            tab.excel_ref('A4').expand(RIGHT).is_not_blank().is_not_whitespace().subdim(DIRECTLY, ABOVE)
                            ])
                        if x == 0:
                            obs = obs - (tab.excel_ref('C1').fill(DOWN) | tab.excel_ref('G1').fill(DOWN))
                            obs = obs.is_not_blank().is_not_whitespace()
                        else:
                            obs = tab.excel_ref('C1') | tab.excel_ref('G1')
                            obs = obs.waffle(anchor.fill(DOWN).is_not_bold().is_not_blank().is_not_whitespace())
                            obs = obs.is_not_blank().is_not_whitespace()        
             
             
            if tab.name == 'L GVAbp':
                    # Add some blanks to headert lines 1 and 2 so we dont get lookuperrors
                    h1 = tab.excel_ref('A2').expand(RIGHT).is_not_blank().is_not_whitespace().parent()
                    h2 = tab.excel_ref('A3').expand(RIGHT).is_not_blank().is_not_whitespace() | tab.excel_ref('F3') | tab.excel_ref('C3')                    
                    tab.dimension('Category', [
                        h1.subdim(CLOSEST, direction),
                        tab.subdim(' - '),
                        h2.subdim(CLOSEST, direction),
                        tab.subdim(' - '),
                        tab.excel_ref('A4').expand(RIGHT).is_not_blank().is_not_whitespace().subdim(DIRECTLY, ABOVE)
                        ])
                    if x == 0:
                        obs = obs - (tab.excel_ref('C1').fill(DOWN) | tab.excel_ref('H1').fill(DOWN) | tab.excel_ref('I1').fill(DOWN))
                    else:
                        obs = tab.excel_ref('C1') | tab.excel_ref('H1') | tab.excel_ref('I1')
                        obs = obs.waffle(anchor.fill(DOWN).is_not_bold().is_not_blank().is_not_whitespace())  


            # Just in case but we'll probably never use
            if tab.name == 'N Financial Year Variables':          
                    h1 = tab.excel_ref('A3').expand(RIGHT).is_not_blank().is_not_whitespace().parent() | tab.excel_ref('L3')                     
                    tab.dimension('Category', [
                        h1.subdim(CLOSEST, direction),
                        tab.subdim(' - '),
                        tab.excel_ref('A4').expand(RIGHT).is_not_blank().is_not_whitespace().subdim(DIRECTLY, ABOVE)
                        ])
                    if x == 0:
                        obs = obs
                    else:
                        return # Only one yield required            


            # Time Dimension                                
            anchor.expand(DOWN).is_not_blank().is_not_whitespace().is_not_bold().dimension(TIME, DIRECTLY, LEFT)
                
            # Getting the type of Output
            anchor.expand(DOWN).is_not_blank().is_not_whitespace().is_bold().dimension('Output', CLOSEST, ABOVE)
                
            # Getting the CDIDs
            cdid_horizontal = anchor.shift(UP).fill(RIGHT).is_not_blank().is_not_whitespace()       
            cdid_vertical = anchor.expand(DOWN).is_blank()
            cdid = cdid_horizontal.waffle(cdid_vertical).is_not_blank().is_not_whitespace() | cdid_horizontal        
            cdid.dimension('CDID', DIRECTLY, ABOVE)
              
              
            # Get the differentiating dimension for Table(s) C
            if tab.name == 'C1 EXPENDITURE':
                tab.dimension(UNITOFMEASURE,'£ million')
            if tab.name == 'C2 EXPENDITURE':
                tab.dimension(UNITOFMEASURE,'Reference year 2012, £ million')            
                    
                  
                  
            # -- Cleaning the crap out of obs --
            # Footer information
            obs = obs - tab.excel_ref('B2').expand(DOWN).is_not_blank().is_not_whitespace().expand(RIGHT).expand(LEFT).expand(DOWN)        
            # CDIDs        
            obs = obs - cdid
            
            if PARAMS(2) == 'Y':
                obs = obs - anchor.fill(DOWN).filter(contains_string('Q')).fill(RIGHT)
            elif PARAMS(2) == 'Q':
                # obs = anchor.fill(DOWN).is_not_blank().is_not_whitespace() - anchor.fill(DOWN).filter(contains_string('Q')).is_not_blank().is_not_whitespace()
                unwanted = anchor.fill(DOWN).is_not_blank().is_not_whitespace() - anchor.fill(DOWN).filter(contains_string('Q')).is_not_blank().is_not_whitespace()               
                obs = obs - unwanted.fill(RIGHT)
            
            # goalkeeper
            obs = obs.is_not_blank().is_not_whitespace()
            
            yield obs
            
        
            
            
            