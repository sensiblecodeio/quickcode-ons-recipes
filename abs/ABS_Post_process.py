# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 10:07:40 2015

@author: Rob / Mike


NOTE - Added a py_lookup file to catch all the labels whcih have altered names.
If it happens again its probably easiest to just add to that that rework the whole recipe.

"""

import pandas as pd
import csv
import py_lookups as lookup
import sys

load_file = sys.argv[1]
                                                                                                   
obs_file = pd.read_csv(load_file, dtype=object)
obs_file.fillna('', inplace = True)
#obs_file[1:] = obs_file[1:].astype('str')

#Clean Superscript elements
obs_file['dim_item_id_2'] = obs_file['dim_item_id_2'].str.rstrip(' (1)')
obs_file['dim_item_id_2'] = obs_file['dim_item_id_2'].str.strip()
obs_file['dimension_item_label_eng_2'] = obs_file['dim_item_id_2']

# 95 and 96 not working with the below lookup, do them by direct reference
# TODO - why?
obs_file['dim_item_id_1'] = obs_file['dim_item_id_1'].astype(str)
obs_file['dim_item_id_1'].map(str.strip)
obs_file['dim_item_id_1'][obs_file['dim_item_id_1'].str[:2] == '96'] = 'Other personal service activities '
obs_file['dim_item_id_1'][obs_file['dim_item_id_1'].str[:2] == '95'] = 'Repair of computers and personal house'

# Sort the names out via a lookup.
# Get rid of any numbers starting with an excel generated 0
obs_file = lookup.name_changer(obs_file, "dim_item_id_1")

# Concat the pre and post lookup values into one cell, then copy to label
obs_file['dimension_item_label_eng_1'] = obs_file['dimension_item_label_eng_1'].astype(str)
obs_file['dimension_item_label_eng_1'] = obs_file['dimension_item_label_eng_1'].map(lambda x: x.rstrip('.0'))
obs_file['dim_item_id_1'] = obs_file['dimension_item_label_eng_1'] + ' ' + obs_file['dim_item_id_1'] 
obs_file['dimension_item_label_eng_1'] = obs_file['dim_item_id_1']

#remove unwanted Dimension fields
obs_file.drop(['dim_id_3', 'dimension_label_eng_3', 'dimension_label_cym_3', 'dim_item_id_3', 'dimension_item_label_eng_3', 'dimension_item_label_cym_3', 'is_total_3', 'is_sub_total_3'],inplace=True,axis=1)

# At this poiny dim_item_id_1 doesnt match prevous months (its truncated) so use another lookup t0 correct
obs_file = lookup.repair(obs_file, "dim_item_id_1")
obs_file['dimension_item_label_eng_1'] = obs_file['dim_item_id_1']


"""
UN-CORRECT
We have to uncorrect a title as per discussion with Paul, to make it match the previous dataset uploaded 
"""
obs_file['dim_item_id_2'][obs_file['dim_item_id_2'] == 'National non-domestic (business) rates'] = 'National non-domestic (business rates'

#sort the file for segments
obs_file = obs_file.sort(['dim_id_2', 'unit_of_measure_eng', 'measure_type_eng'], ascending = False)

#strip trailing '.0' from fields read by databaker as float
obs_file['observation'] = obs_file['observation'].map(str).map(lambda x: x.replace('.0', ''))
obs_file['time_dim_item_id'] = obs_file['time_dim_item_id'].map(str).map(lambda x: x.replace('.0', ''))
obs_file['time_dim_item_label_eng'] = obs_file['time_dim_item_label_eng'].map(str).map(lambda x: x.replace('.0', ''))

#Save the transformed file
obs_file.to_csv('transform-Annual Business Survey Standard Extracts 2013R-ABS01-.csv', index = False, quoting = csv.QUOTE_MINIMAL)
#obs_merge.to_csv('merge-Annual Business Survey Standard Extracts 2013R-ABS01-.csv')