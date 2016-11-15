 # -*- coding: utf-8 -*-
"""
Spyder Editor

Basic reusable functions to help post-process data with Pandas.

Author: Mike
"""

import pandas as pd

# Dismiss command for unwanted items. Will remove all 8 relevant columns.
def dismiss(myframe, headers):
    
    for each in headers:
        Column1 = myframe.columns.get_loc(each)
        for x in range(1, 9):
            myframe = myframe.drop(myframe.columns[Column1], axis=1)
    return myframe
    

# Write over the current topic dimension numbering with correct numbering
def validateheaders(myframe):
    standard_headings = ['dim_id_', 'dimension_label_eng_', 'dimension_label_cym_', 'dim_item_id_',
                         'dimension_item_label_eng_', 'dimension_item_label_cym_', 'is_total_', 'is_sub_total_']
    for count in range(35, len(myframe.columns.values), 8):
        for x in range(0, 8):
           myframe.rename(columns={myframe.columns[count+x]: standard_headings[x] + str((count-35) / 8 + 1)}, inplace=True)
    return myframe

 
# Converts everything to string and joins around a single space
def strip_and_join(obs_file, dimlist):
    for x in dimlist:
        obs_file[x] = obs_file[x].astype(str)
        obs_file[x] = obs_file[x].map(lambda x: x.strip())
        obs_file[x] = obs_file[x].map(lambda x: ' '.join(x.split()))        
    obs_file[dimlist[0]] = obs_file[dimlist[0]] + ' ' + obs_file[dimlist[1]] + ' ' + obs_file[dimlist[2]]
    obs_file[dimlist[0]] = obs_file[dimlist[0]].map(lambda x: x.strip())
    return obs_file[dimlist[0]]
    
