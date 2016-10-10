# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:05:13 2015

@author: Rob
"""
from __future__ import unicode_literals
from databaker.constants import *

def per_file(tabs):
    return "*"
    
def per_tab(tab):
    
    tab_title = tab.excel_ref("A1")

    if not tab_title.filter(contains_string(PARAMS()[0])):
        return
    
    anchor = tab.filter("Period").assert_one()
    
    datarows = anchor.fill(DOWN).is_not_blank()
    datacols = anchor.shift(DOWN).fill(RIGHT).is_not_blank()
    
    obs = datarows.waffle(datacols).is_not_blank()
    
    datarows.dimension(TIME, DIRECTLY, LEFT)
    datacols.parent().dimension("Costs", DIRECTLY, ABOVE)
    anchor.fill(RIGHT).parent().dimension("SIC", CLOSEST, LEFT)
    
    if tab_title.filter(contains_string("year on year")):
        tab.dimension("Growth Period","Annual")
        tab.dimension(MEASURETYPE,"Percent")
    elif tab_title.filter(contains_string("quarter on quarter")):
        tab.dimension("Growth Period","Quarterly")
        tab.dimension(MEASURETYPE,"Percent")
    elif tab_title.filter(contains_string("growth rates")):
        tab.dimension("Growth Period","Annual")
        tab.dimension(MEASURETYPE,"Percent")
    else:
        tab.dimension(MEASURETYPE,"Index")
    
    if tab_title.filter(contains_string("Non-Seasonally")):
        tab.dimension("SA / NSA","Not seasonally adjusted")
    else:
        tab.dimension("SA / NSA","Seasonally adjusted")
        
    yield obs