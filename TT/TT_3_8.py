# -*- coding: utf-8 -*-
"""
Created on Thursday July 17 10:47:26 2015
@author: Mike

"""

from databaker.constants import *

# Move_Right & Counter
My_count = [0]

MyList = [["Visit", "Count", "1000", "Visits (Thousands)"], \
        ["Spending", "Value", "1000000", "Spending (Millions)"]]
    
def per_file(tabs):
    return (PARAMS(0), PARAMS(0), PARAMS(1), PARAMS(1))
   
def per_tab(tab):
    
    Col_B = tab.excel_ref('B').is_not_blank()       # Get the output and anchor to the second value in B
    count = 0
    for each in Col_B:
        if count == 0:
            output = each
        if count == 1:
            anchor = each
        count += 1
        
    unwanted = tab.excel_ref('A').filter(contains_string ("verage annual")).expand(RIGHT).expand(DOWN).is_not_blank()
    
    if My_count[0] % 2 == 0:    
        obs = anchor.expand(DOWN).expand(RIGHT).filter(contains_string ("isits")).shift(DOWN).fill(DOWN).is_not_blank() - unwanted
        tab.dimension(STATUNIT, MyList[0][0])
        if My_count[0] == 2:
            tab.dimension(STATPOP, "UK Residents")
        else:
            tab.dimension(STATPOP, "Overseas Residents")
        tab.dimension(MEASURETYPE, MyList[0][1])
        tab.dimension(UNITMULTIPLIER, MyList[0][2])
        tab.dimension(UNITOFMEASURE, MyList[0][3]) 
    else:
        obs = obs = anchor.expand(DOWN).expand(RIGHT).filter(contains_string ("ending")).shift(DOWN).fill(DOWN).is_not_blank() - unwanted
        tab.dimension(STATUNIT, MyList[1][0])
        if My_count[0] == 3:
            tab.dimension(STATPOP, "UK Residents")
        else:
            tab.dimension(STATPOP, "Overseas Residents")
        tab.dimension(MEASURETYPE, MyList[1][1])
        tab.dimension(UNITMULTIPLIER, MyList[1][2])
        tab.dimension(UNITOFMEASURE, MyList[1][3]) 

    anchor.expand(RIGHT).is_not_blank().parent().dimension("Category", CLOSEST, LEFT)
    output.dimension("Output", CLOSEST, ABOVE)    
    Dates = anchor.shift(LEFT).fill(DOWN).is_not_blank() - unwanted
    Dates.dimension(TIME, DIRECTLY,LEFT)
    
    My_count[0] = My_count[0] + 1  
    
    yield obs