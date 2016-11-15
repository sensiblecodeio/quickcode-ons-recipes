# -*- coding: utf-8 -*-
"""
Created on Wed May 04 13:16:19 2016

@author: Mike
"""

# GENERIC final combination code
# both hours and earnings will call this plus the more specific code shown below

def generic_merge(obs_file, which_ASHE):
    
    obs_file.fillna('', inplace = True)

    # Get ridof any blank obs and data markings rows
    # WE WILL HAVE SOME. I cant take these out earlier as the main and CV files wont join in the proper sequence.
    obs_file = obs_file[obs_file['observation'] + obs_file['data_marking'] != '']

    # Strip and replace the mangled vetical indexes
    obs_file = obs_file.reset_index() 
    obs_file = obs_file.drop('index', axis=1)

    # Correct the obs count
    obs_file['data_marking'][-1:] = len(obs_file) -1

    if which_ASHE >1 and which_ASHE < 7:
        # Sort for segments
        obs_file = obs_file.sort(['measure_type_eng', 'dim_id_1', 'dim_item_id_7'], ascending=False)        
    else:
        # Sort for segments
        obs_file = obs_file.sort(['measure_type_eng', 'dim_item_id_1'], ascending=False)
        
    return obs_file
    
###########################################################################################
# TABLES - 1 THROUGH 8 BECOME ASHEearnings

def merge_earnings(which_ASHE, fdone):
    
    import pandas as pd
    
    # load all sheets. Strip the footer row of all except the last one
    a1 = pd.read_csv('merge_file_1.csv', dtype=object)
    a1 = a1[a1['observation'] != '*********']
    
    a2 = pd.read_csv('merge_file_2.csv', dtype=object)
    a2 = a2[a2['observation'] != '*********']
    
    a3 = pd.read_csv('merge_file_3.csv', dtype=object)
    a3 = a3[a3['observation'] != '*********']
    
    a4 = pd.read_csv('merge_file_4.csv', dtype=object)
    a4 = a4[a4['observation'] != '*********']
    
    a5 = pd.read_csv('merge_file_5.csv', dtype=object)
    a5 = a5[a5['observation'] != '*********']
    
    a6 = pd.read_csv('merge_file_6.csv', dtype=object)
    a6 = a6[a6['observation'] != '*********']
    
    a7 = pd.read_csv('merge_file_7.csv', dtype=object)
    a7 = a7[a7['observation'] != '*********']
    
    a8 = pd.read_csv('merge_file_8.csv', dtype=object)
    obs_file = pd.concat([a1, a2, a3, a4, a5, a6, a7, a8])
    obs_file = generic_merge(obs_file, which_ASHE)
    
    # Output final product
    obs_file.to_csv('transform-ASHE' + str(which_ASHE)+ 'earnings' + fdone[0][-8:-4] + '.csv', index=False)

###########################################################################################
# TABLES - 9 THROUGH 11 BECOME ASHEhours

def merge_hours(which_ASHE, fdone):
    
    import pandas as pd
    
    # load all sheets. Strip the footer row of all except the last one
    a1 = pd.read_csv('merge_file_9.csv', dtype=object)
    a1 = a1[a1['observation'] != '*********']
    
    a2 = pd.read_csv('merge_file_10.csv', dtype=object)
    a2 = a2[a2['observation'] != '*********']
    
    a3 = pd.read_csv('merge_file_11.csv', dtype=object)
    
    obs_file = pd.concat([a1, a2, a3])
    obs_file = generic_merge(obs_file, which_ASHE)
    
    # Switich "Earnings" Dim id to "Hours" - THIS CODE IS NOT REQUIRED FOR EARNINGS
    obs_file['dim_id_1'][:-1] = 'Hours'
    obs_file['dimension_label_eng_1'] = obs_file['dim_id_1']
    # Switch "Earnings Statistics" to "Hours Statistics"
    obs_file['dim_id_2'][obs_file['dim_id_2'] == 'Earnings Statistics'] = 'Hours Statistics'
    obs_file['dimension_label_eng_2'] = obs_file['dim_id_2']
    
    # Output final product
    obs_file.to_csv('transform-ASHE' + str(which_ASHE)+ 'hours' + fdone[0][-8:-4] + '.csv', index=False)
    
