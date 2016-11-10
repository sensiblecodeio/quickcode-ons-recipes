# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 13:32:40 2016

@author: Mike
"""

def correct(obs_file, dimension):
    """ An unordered list of corrections - if it comes up with a wierd combination,
    HERE is where you fix it. """
    
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('OTHER EUROPEAN', 'OTHER EUROPEAN COUNTRIES')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('NEAR & MIDDLE EAST', 'NEAR & MIDDLE EAST COUNTRIES')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('OTHER ASIAN', 'OTHER ASIAN COUNTRIES')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('AUSTRALASIA & ', 'AUSTRALASIA & OCEANIA')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('CENTRAL & EASTERN', 'CENTRAL & EASTERN EUROPE')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('WORLD TOTAL EUROPE', 'WORLD TOTAL CENTRAL & EASTERN EUROPE')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('COUNTRIES COUNTRIES', 'COUNTRIES')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('ASIA COUNTRIES', 'ASIA OTHER ASIAN COUNTRIES')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('EUROPE COUNTRIES', 'EUROPE OTHER EUROPEAN COUNTRIES')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('COUNTRIES COUNTRIES', 'COUNTRIES')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('ASIA NEAR & MIDDLE', 'ASIA NEAR & MIDDLE EAST')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('WORLD TOTAL CENTRAL &', 'WORLD TOTAL CENTRAL & EASTERN EUROPE')).astype(str)
             
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('2.3: Foreign direct investment flows into the United Kingdom analysed by area & main country and by industrial activity of UK affiliates', 'Direct investment flows analysed by area, main country and by industrial activity')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('2.3 Foreign direct investment flows into the United Kingdom analysed by area & main country and by industrial activity of UK affiliates', 'Direct investment flows analysed by area, main country and by industrial activity')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('3.3: FDI international investment position in the United Kingdom analysed by area & main country and by industrial activity of UK affiliates', 'Investment position analysed by area, main country and by industrial activity')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('3.3 FDI international investment position in the United Kingdom analysed by area & main country and by industrial activity of UK affiliates', 'Investment position analysed by area, main country and by industrial activity')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('4.3 Earnings from foreign direct investment in the United Kingdom analysed by area & main country and by industrial activity of UK affiliates', 'Earnings from direct investment analysed by area, main country and by industrial activity')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('4.3: Earnings from foreign direct investment in the United Kingdom analysed by area & main country and by industrial activity of UK affiliates', 'Earnings from direct investment analysed by area, main country and by industrial activity')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('2.3 Foreign direct investment flows abroad analysed by area & main country and by industrial activity of foreign affiliates', 'Direct investment flows analysed by area, main country and by industrial activity')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('2.3: Foreign direct investment flows abroad analysed by area & main country and by industrial activity of foreign affiliates', 'Direct investment flows analysed by area, main country and by industrial activity')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('3.3 FDI international investment position abroad analysed by area & main country and by industrial activity of foreign affiliates', 'Investment position analysed by area, main country and by industrial activity')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('3.3: FDI international investment position abroad analysed by area & main country and by industrial activity of foreign affiliates', 'Investment position analysed by area, main country and by industrial activity')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('4.3 Earnings from foreign direct investment abroad analysed by area & main country and by industrial activity of overseas affiliates', 'Earnings from direct investment analysed by area, main country and by industrial activity')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('4.3: Earnings from foreign direct investment abroad analysed by area & main country and by industrial activity of overseas affiliates', 'Earnings from direct investment analysed by area, main country and by industrial activity')).astype(str)        
            
    # Clean ups
    """Sometimes fixing one thing breaks another. these just clear out all the obviously wrong now"""
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('EASTERN EUROPE EASTERN EUROPE', 'EASTERN EUROPE')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('EAST EAST', 'EAST')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('WEST WEST', 'WEST')).astype(str)    
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('OCEANIAOCEANIA', 'OCEANIA')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('  ', ' ')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('   ', ' ')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('    ', ' ')).astype(str)
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.replace('     ', ' ')).astype(str)
    
    obs_file[dimension] = obs_file[dimension].map(lambda x: x.rstrip())
    
    return obs_file
    