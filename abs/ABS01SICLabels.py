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
    tablist.discard('Sections A-S')
    return tablist
    
def per_tab(tab):
    
    anchor = tab.filter('Year').assert_one()
    footer = tab.filter(contains_string('Annual Business Survey')).assert_one()
    
    obs = anchor.shift(-2,1).fill(DOWN).is_not_blank() - footer.expand(DOWN)
    
    obs.dimension("SICABS01", DIRECTLY, LEFT)
    first_label = obs.shift(RIGHT).dimension('SIC 1', DIRECTLY, RIGHT)
    first_label.shift(DOWN).dimension('SIC 2', CLOSEST, DOWN)
    first_label.shift(0,2).dimension('SIC 3', CLOSEST, DOWN)
    first_label.shift(0,3).dimension('SIC 4', CLOSEST, DOWN)
    
    yield obs