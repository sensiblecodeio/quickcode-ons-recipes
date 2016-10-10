# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 06:25:11 2015

@author: Rob
"""
from __future__ import unicode_literals
from databaker.constants import *

def per_file(tabs):
    tablist = tabs.names
    tablist.discard('Contents')
    tablist.discard('Section A-S')
    return tablist
    
def per_tab(tab):
    
    anchor = tab.filter('Year').assert_one()
    measure_type = anchor.shift(DOWN).fill(RIGHT).is_not_blank()
    
    year = anchor.shift(DOWN).fill(DOWN).is_not_blank().dimension(TIME, DIRECTLY, LEFT)
    
    this_bit = measure_type.filter('Number')
    
    obs = year.waffle(this_bit)
    
    anchor.shift(-2,1).fill(DOWN).is_not_blank().dimension('SIC07ABS01',CLOSEST, ABOVE)
    anchor.fill(RIGHT).dimension('Number of Enterprises', DIRECTLY, ABOVE)
    anchor.shift(-1,1).fill(DOWN).is_not_blank().dimension('SIC07ABS01 2',CLOSEST, ABOVE)
    
    tab.dimension(STATUNIT, 'Enterprises')
    tab.dimension(STATPOP, 'UK Businesses')
    tab.dimension(MEASURETYPE, 'Count')
    tab.dimension(UNITMULTIPLIER, '1')
    tab.dimension(UNITOFMEASURE, 'Enterprises')
    
    yield obs
    
    year = anchor.shift(DOWN).fill(DOWN).is_not_blank().dimension(TIME, DIRECTLY, LEFT)
    
    this_bit = measure_type.filter('Thousand')
    
    obs = year.waffle(this_bit)
    
    anchor.shift(-2,1).fill(DOWN).is_not_blank().dimension('SIC07ABS01',CLOSEST, ABOVE)
    anchor.fill(RIGHT).dimension('Employee Counts', DIRECTLY, ABOVE)
    anchor.shift(-1,1).fill(DOWN).is_not_blank().dimension('SIC07ABS01 2',CLOSEST, ABOVE)
    
    tab.dimension(STATUNIT, 'Employees')
    tab.dimension(STATPOP, 'UK Businesses')
    tab.dimension(MEASURETYPE, 'Count')
    tab.dimension(UNITMULTIPLIER, '1000')
    tab.dimension(UNITOFMEASURE, 'Employees (Thousands)')
    
    yield obs
    
    year = anchor.shift(DOWN).fill(DOWN).is_not_blank().dimension(TIME, DIRECTLY, LEFT)
    
    this_bit = measure_type.filter(contains_string("million"))
    
    obs = year.waffle(this_bit)
    
    anchor.shift(-2,1).fill(DOWN).is_not_blank().dimension('SIC07ABS01',CLOSEST, ABOVE)
    anchor.fill(RIGHT).dimension('UK Business Value', DIRECTLY, ABOVE)
    anchor.shift(-1,1).fill(DOWN).is_not_blank().dimension('SIC07ABS01 2',CLOSEST, ABOVE)
    
    tab.dimension(STATUNIT, '£')
    tab.dimension(STATPOP, 'UK Businesses')
    tab.dimension(MEASURETYPE, 'Value')
    tab.dimension(UNITMULTIPLIER, '1000000')
    tab.dimension(UNITOFMEASURE, 'GBP Million')
    
    yield obs