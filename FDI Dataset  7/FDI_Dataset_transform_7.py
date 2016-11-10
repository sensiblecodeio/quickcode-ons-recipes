# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:42:18 2015

@author: Mike
"""

import sys
import transform_lib as tf
import pandas as pd
import py_lookups as lookup
import geofix as gf

# Combine the files
obs_file1 = pd.read_csv(sys.argv[1])
obs_file2 = pd.read_csv(sys.argv[2])

obs_file = pd.concat([obs_file1, obs_file2])

obs_file = obs_file[obs_file['observation'] != '*********']    
obs_file = obs_file.reset_index()    

obs_file = gf.correct(obs_file, 'dim_item_id_3')
obs_file['dimension_item_label_eng_3'] = obs_file['dim_item_id_3'] 

# Add file footer
count = len(obs_file)
obs_file = obs_file.set_value(len(obs_file), 'observation', '*********')
obs_file = obs_file.set_value(len(obs_file) -1, 'data_marking', count)
obs_file['data_marking'] = obs_file['data_marking'].astype(str)
obs_file['data_marking'] = obs_file['data_marking'].map(lambda x: x.replace('.0', ''))

# Sort out the index
obs_file.fillna('', inplace = True)
obs_file = obs_file.drop('index', 1)

# Make Category Generic
obs_file = lookup.cat_lookup(obs_file, "dim_item_id_1")
obs_file['dimension_item_label_eng_1'] = obs_file['dim_item_id_1']

# Strip trialing 0 from time
obs_file['time_dim_item_id'] = obs_file['time_dim_item_id'].astype(str)
obs_file['time_dim_item_label_eng'] = obs_file['time_dim_item_label_eng'].astype(str)

obs_file['time_dim_item_id'] = obs_file['time_dim_item_id'].map(lambda x: x.replace('.0', '')).astype(str)
obs_file['time_dim_item_label_eng'] = obs_file['time_dim_item_label_eng'].map(lambda x: x.replace('.0', '')).astype(str)

# Remove the dimensions we dont need anymore: args = (dataframe, [dimensons to drop])
obs_file.fillna('', inplace = True)

obs_file.to_csv(sys.argv[3] + '.csv', index=False)
