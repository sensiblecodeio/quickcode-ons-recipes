# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 06:25:11 2015

@author: Rob
"""

from databaker.constants import *
from hamcrest import *

def per_file(tabs):
    return ['Section A', 'Section B', 'Section C', 'Section D', 'Section E', 'Section F'
           'Section I', 'Section J', 'Section K', 'Section L', 'Section M', 'Section N', 'Section O', 'Section P',
           'Section Q', 'Section R', 'Section S', 'Division 45', 'Division 46', 'Division 47']
            
    
    
    #, 'Section G'  values all elsewhere in excel workbook
    
def per_tab(tab):
    
    anchor = tab.filter('Year').assert_one()
    measure_type = anchor.shift(DOWN).fill(RIGHT).is_not_blank()
    
    year = anchor.shift(DOWN).fill(DOWN).is_not_blank()
    
    sic = anchor.shift(-2,1).fill(DOWN).same_row(year).is_not_blank()
    
    this_bit = measure_type.filter('Number')
    
    obs = year.waffle(this_bit)
    
    year.dimension(TIME, DIRECTLY, LEFT)
    sic = anchor.shift(-2,1).fill(DOWN).same_row(year).is_not_blank().dimension('ABSSIC07',CLOSEST, ABOVE)
    anchor.fill(RIGHT).dimension('Number of Enterprises', DIRECTLY, ABOVE)
    
    tab.dimension(STATUNIT, 'Enterprises')
    tab.dimension(STATPOP, 'UK Businesses')
    tab.dimension(MEASURETYPE, 'Count')
    tab.dimension(UNITMULTIPLIER, '1')
    tab.dimension(UNITOFMEASURE, 'Enterprises')

    
    yield obs
    
    this_bit = measure_type.filter('Thousand')
    
    obs = year.waffle(this_bit)
    
    year.dimension(TIME, DIRECTLY, LEFT)
    anchor.shift(-2,1).fill(DOWN).is_not_blank().dimension('ABSSIC07',CLOSEST, ABOVE)
    anchor.fill(RIGHT).dimension('Employee Counts', DIRECTLY, ABOVE)
    
    tab.dimension(STATUNIT, 'Employees')
    tab.dimension(STATPOP, 'UK Businesses')
    tab.dimension(MEASURETYPE, 'Count')
    tab.dimension(UNITMULTIPLIER, '1000')
    tab.dimension(UNITOFMEASURE, 'Employees (Thousands)')

    
    yield obs
    
    all_obs = anchor.fill(RIGHT).is_not_blank().waffle(year)
    ignore_obs = measure_type.filter(any_of('Number', 'Thousand')).waffle(year)
    
    obs = all_obs - ignore_obs
    
    year.dimension(TIME, DIRECTLY, LEFT)
    anchor.shift(-2,1).fill(DOWN).is_not_blank().dimension('ABSSIC07',CLOSEST, ABOVE)
    anchor.fill(RIGHT).dimension('UK Business Value', DIRECTLY, ABOVE)
    
    tab.dimension(STATUNIT, 'GBP')
    tab.dimension(STATPOP, 'UK Businesses')
    tab.dimension(MEASURETYPE, 'Value')
    tab.dimension(UNITMULTIPLIER, '1000000')
    tab.dimension(UNITOFMEASURE, 'GBP Million')

    yield obs