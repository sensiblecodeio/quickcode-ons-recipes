# -*- coding: utf-8 -*-
"""
Created on Thu Oct 08 09:12:06 2015

@author: Mike
"""

import sys
import pandas as pd
import transform_lib as tf
import py_lookups as lookup

### COMMON TO EVERY TABLE

load_file = sys.argv[1]
numASHE = sys.argv[2]



obs_file = pd.read_csv(load_file, dtype=object)
obs_file.fillna('', inplace = True)

"""
Old Conditional. Left in place for now but i rly need to un-indent everything :)
"""
execute = True
if execute:
    
    # Sortout the mean/median thing, one for every other instance of mean or median
    flip  = 0
    for i, row in obs_file.iterrows():
        if row['dim_item_id_4'] == 'change':
            if flip == 0:
                obs_file.ix[i, 'dim_item_id_4'] = 'change in Median'
                flip = 1
            else:
                obs_file.ix[i, 'dim_item_id_4'] = 'change in Mean'
                flip = 0
        
    # Clean and concatenate the columns for Titles 1,2 & 3.
    obs_file['dim_item_id_2'] = tf.strip_and_join(obs_file, ['dim_item_id_2', 'dim_item_id_3', 'dim_item_id_4'])
    obs_file['dimension_item_label_eng_2'] = obs_file['dim_item_id_2']
    obs_file = tf.dismiss(obs_file, ['dim_id_3', 'dim_id_4'])
    
    # Get rid of the number after number of jobs. i.e 'Number of Jobs 1' becomes 'Number of Jobs'
    obs_file['dim_id_2'] = obs_file['dim_id_2'].str[:-2]
    obs_file['dimension_label_eng_2'] = obs_file['dim_id_2']

    
    """
    CONDITIONALS
    This is the code that will change depending on the ASHE table number being transformed.
    """

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------------------------------------

    if numASHE in ['1', '26']:
        obs_file = tf.dismiss(obs_file, ['dim_id_7', 'dim_id_8'])

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------------------------------------


    #  IF ITS ASHE tables 7-13    
    if numASHE in ['7', '8', '9', '10', '11', '12']:
        ### Sort out geography
        # Populate missing codes with a LOOKUP    
        obs_file = lookup.locatiionTOgeocode(obs_file, "dim_item_id_7")
        obs_file['dim_item_id_8'][obs_file['dim_item_id_8'] == ''] = obs_file['dim_item_id_7']    
        
        # Move codes across    
        obs_file['geographic_area'] = obs_file['dim_item_id_8']
    
        # Dismiss dimensions 7 and 8 as we dont need them for the final document
        obs_file = tf.dismiss(obs_file, ['dim_id_8', 'dim_id_7'])
        obs_file = tf.validateheaders(obs_file)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------------------------------------


    if numASHE in ['3', '5']:
            # Sort data types and put in the Classification
            obs_file['dim_item_id_7'] = obs_file['dim_item_id_7'].astype(str)
            obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].astype(str)
            obs_file['dim_item_id_9'] = obs_file['dim_item_id_9'].astype(str)
            obs_file['dim_id_7'] = 'Area'
            obs_file['dimension_label_eng_7'] = obs_file['dim_id_7']
            
            obs_file['dim_item_id_7'] = obs_file['dim_item_id_7'].map(str.strip)
            obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(str.strip)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------------------------------------
            
            if numASHE == '5':
                
                obs_file['dim_item_id_7'] = obs_file['dim_item_id_7'].astype(str)
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].astype(str)
                obs_file['dim_item_id_9'] = obs_file['dim_item_id_9'].astype(str)
                obs_file['dim_item_id_7'] = obs_file['dim_item_id_7'].map(str.strip)
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(str.strip)
                obs_file['dim_item_id_9'] = obs_file['dim_item_id_9'].map(str.strip)
                obs_file['temp'] = '' 
                obs_file['temp'][(obs_file['dim_item_id_9'] != '') & (obs_file['dim_item_id_8'] != '')] = ' (' + obs_file['dim_item_id_9'].map(str.strip) + ')'
                obs_file['dim_item_id_9'] = ''
            
                # Use itterator. If the CAPS area is in 8, split it into seven and same number from spaces from 8
                
                # lists required for conditionals
                remove_list = ['EAST', 'WEST', 'East', 'West', 'NORTH EAST', 'NORTH WEST', 'YORKSHIRE AND THE HUMBER', 'EAST MIDLANDS', 'WEST MINDLANDS', 
                'LONDON', 'SOUTH EAST', 'SOUTH WEST', 'WALES', 'SCOTLAND', 'NORTHERN IRELAND', 'United Kingdom', 'North East', 'North West', 'LONDON', 'WEST MIDLANDS', 'EAST MIDLANDS',
                'Yorkshire and The Humber', 'East Midlands', 'West Midlands', 'London', 'South East', 'South West', 'Wales', 'Scotland', 'Northern Ireland']         
                
                for i, row in obs_file.iterrows():
                    for each in remove_list[4:]:
                        if each in row['dim_item_id_8']:
                            row['dim_item_id_8'] = row['dim_item_id_8'][len(each):]
                            row['dim_item_id_8'] = row['dim_item_id_8'].lstrip(', ')
                            row['dim_item_id_9'] = each
                            
                
                    # Do east and west last as theyre partially contained in other answers
                    for each in remove_list[:4]:
                        if each in row['dim_item_id_8']:
                            row['dim_item_id_8'] = row['dim_item_id_8'][len(each):]
                            row['dim_item_id_8'] = row['dim_item_id_8'].lstrip(', ')
                            row['dim_item_id_9'] = each     

                for i, row in obs_file.iterrows():
                    for each in remove_list[4:]:
                        if each in row['dim_item_id_7']:
                            row['dim_item_id_7'] = row['dim_item_id_7'][len(each):]
                            row['dim_item_id_7'] = row['dim_item_id_7'].lstrip(', ')          
                
                    # Do east and west last as theyre partially contained in other answers
                    for each in remove_list[:4]:
                        if each in row['dim_item_id_7']:
                            row['dim_item_id_7'] = row['dim_item_id_7'][len(each):]
                            row['dim_item_id_7'] = row['dim_item_id_7'].lstrip(', ') 
                
                # Clean any rogue whitespace
                obs_file['dim_item_id_7'] = obs_file['dim_item_id_7'].map(str.strip)
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(str.strip)
                obs_file['dim_item_id_9'] = obs_file['dim_item_id_9'].map(str.strip)
                
                obs_file['dim_item_id_8'][obs_file['dim_item_id_8'] == obs_file['dim_item_id_7']] = '' 
                
                # Concatenate etc
                #obs_file['dim_item_id_7'][obs_file['dim_item_id_8'] == obs_file['dim_item_id_7']] = 'Total'
                obs_file['dim_item_id_7'][obs_file['dim_item_id_8'] != ''] = obs_file['dim_item_id_7'] + ' - ' + obs_file['dim_item_id_8']
                obs_file['dim_item_id_7'][obs_file['dim_item_id_7'] == ' - '] = 'Total'
    
                # Get rid of any blank codes/curly brackets only
                obs_file['dim_item_id_7'] = obs_file['dim_item_id_7'].map(lambda x: x.replace('()', ''))
                
                # Add UK where we dont have a region
                obs_file['dim_item_id_9'][obs_file['dim_item_id_9'] == ''] = 'United Kingdom'
                
                # Add the code and fill the blanks now everything else is sorted
                obs_file['dim_item_id_7'][obs_file['dim_item_id_7'] == ''] = 'Total'
                obs_file['dim_item_id_7'] = obs_file['dim_item_id_7'] + obs_file['temp']
                obs_file = obs_file.drop('temp', axis=1)
    
                # Clean up the labels, get rid of unwanted columns
                obs_file['dimension_item_label_eng_7'] = obs_file['dim_item_id_7']
                obs_file['dimension_item_label_eng_9'] = obs_file['dim_item_id_9']
                obs_file = tf.dismiss(obs_file, ['dim_id_8'])
                obs_file['dim_id_7'] = 'Occupation'  
                obs_file['dimension_label_eng_7'] = obs_file['dim_id_7']
                obs_file['dim_id_9'] = 'Region'  
                obs_file['dimension_label_eng_9'] = obs_file['dim_id_9']

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------------------------------------
                
            
            if numASHE == '3':
                # get rid of all the extra label UK from 'UK, Some row title' etc
                obs_file['dim_item_id_8'][obs_file['dim_item_id_8'] == obs_file['dim_item_id_7']] = 'All'
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].astype(str)
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(lambda x: x.replace('United Kingdom, ',''))
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(lambda x: x.replace('North East, ',''))
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(lambda x: x.replace('North West, ',''))
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(lambda x: x.replace('Yorkshire and The Humber, ',''))
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(lambda x: x.replace('East Midlands, ',''))
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(lambda x: x.replace('West Midlands, ',''))
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(lambda x: x.replace('South East, ',''))
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(lambda x: x.replace('South West, ',''))
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(lambda x: x.replace('Wales, ',''))    
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(lambda x: x.replace('Scotland, ',''))  
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(lambda x: x.replace('Northern Ireland, ',''))  
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(lambda x: x.replace('East, ',''))  
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(lambda x: x.replace('London, ',''))  
                obs_file['dim_id_8'] = 'Occupation'
                obs_file['dimension_label_eng_8'] = obs_file['dim_id_8']
            
                obs_file['dim_item_id_8'][obs_file['dim_item_id_8'].str[:2] == ' ,'] = obs_file['dim_item_id_8'].str[2:]
                obs_file['dimension_label_eng_8'] = obs_file['dim_id_8']
                
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(str.strip) + ' (' + obs_file['dim_item_id_9'].map(str.strip) + ')'
                # Get rid of any blank codes/curly brackets only
                obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(lambda x: x.replace('()', ''))
                obs_file['dimension_item_label_eng_8'] = obs_file['dim_item_id_8']
                obs_file = tf.dismiss(obs_file, ['dim_id_9'])
            obs_file = tf.validateheaders(obs_file)
        

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------------------------------------


    # IF ITS ASHE TABLES 2, 4, 25
    if numASHE in ['2', '4', '25']: 
        # Sort out the Description
        obs_file['dim_item_id_7'] = obs_file['dim_item_id_7'].astype(str)
        obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].astype(str)
        obs_file['dim_item_id_9'] = obs_file['dim_item_id_9'].astype(str)        
        obs_file['dim_item_id_7'][obs_file['dim_item_id_7'] != obs_file['dim_item_id_8']] = obs_file['dim_item_id_7'].map(str.strip) + ' - ' + obs_file['dim_item_id_8'].map(str.strip)
        obs_file['dim_item_id_7'] = obs_file['dim_item_id_7'].map(str.strip) + ' (' + obs_file['dim_item_id_9'].map(str.strip) + ')'
        # Get rid of any blank codes/curly brackets only
        obs_file['dim_item_id_7'] = obs_file['dim_item_id_7'].map(lambda x: x.replace('()', ''))
        obs_file['dimension_item_label_eng_7'] = obs_file['dim_item_id_7']        
        obs_file = tf.dismiss(obs_file, ['dim_id_8', 'dim_id_9'])
        obs_file = tf.validateheaders(obs_file) 

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------------------------------------

        
    if numASHE in ['6', '13']:
        obs_file['dim_item_id_7'] = obs_file['dim_item_id_7'].astype(str)
        obs_file['dim_item_id_7'] = obs_file['dim_item_id_7'].map(lambda x: x.replace('16-17b', '16-17'))
        obs_file['dimension_item_label_eng_7'] = obs_file['dim_item_id_7']
        obs_file = tf.dismiss(obs_file, ['dim_id_8'])
        obs_file = tf.validateheaders(obs_file)        

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------------------------------------
   
    if numASHE in ['20', '21']:        
        unwanted = ['All Industries and Services', 'All employees', '18-21', '22-29', '30-39', '40-49', '50-59', '60+']

        # Strip back to just total/age in dimension 7 and atore in a temp column
        for i, row in obs_file.iterrows():
            for each in unwanted:
                if each in row['dim_item_id_7']:
                    row['empty5'] = each
                    
        # Keep the unwanted in dim item 8 - IF THATS ALL thats in there, otherwise replacewith ''
        for each in unwanted:
            obs_file['dim_item_id_7'][obs_file['dim_item_id_7'].map(lambda x: x not in unwanted)] = obs_file['dim_item_id_7'].map(lambda x: x.replace(each,''))
            obs_file['dim_item_id_8'][obs_file['dim_item_id_8'].map(lambda x: x not in unwanted)] = obs_file['dim_item_id_8'].map(lambda x: x.replace(each,''))
            obs_file['dim_item_id_9'][obs_file['dim_item_id_9'].map(lambda x: x not in unwanted)] = obs_file['dim_item_id_9'].map(lambda x: x.replace(each,''))                    
            
        obs_file['dim_item_id_7'] = obs_file['dim_item_id_7'].astype(str)
        obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].astype(str)
        obs_file['dim_item_id_9'] = obs_file['dim_item_id_9'].astype(str)
        
        # Get rid of any unwanted commas at the beginning of lines
        obs_file['dim_item_id_7'] = obs_file['dim_item_id_7'].map(lambda x: x.lstrip(', '))
        obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(lambda x: x.lstrip(', '))
        obs_file['dim_item_id_9'] = obs_file['dim_item_id_9'].map(lambda x: x.lstrip(', '))
        
        # Get rid of any NoLookupErrors (expected)            
        obs_file['dim_item_id_9'][obs_file['dim_item_id_9'] == 'NoLookupError'] = ''
        obs_file['dim_item_id_10'][obs_file['dim_item_id_10'] == 'NoLookupError'] = ''
                
        # Use lookup to populate 8
        #obs_file['dim_item_id_8'] = obs_file['dim_item_id_10'][:]   #otherwise itll mutate later
        
        # Use a lookup depending on the source
        if numASHE == 20:        
            obs_file = lookup.ASHE20(obs_file, "dim_item_id_8")
        else:
            pass
            obs_file = lookup.ASHE21(obs_file, "dim_item_id_10")    
            obs_file['dim_item_id_8'][obs_file['dim_item_id_8'] == ''] = 'All Industries and Services'
            obs_file['dim_item_id_10'][obs_file['dim_item_id_10'] == ''] = obs_file['dim_item_id_8']
            obs_file['dim_item_id_8'] = obs_file['dim_item_id_10']
        
        # TODO - wtf does this do?
        obs_file['dim_item_id_7'] = obs_file['empty5'].map(str.strip)
        obs_file['empty5'] = ''
        obs_file = tf.dismiss(obs_file, ['dim_id_9', 'dim_id_10'])        
        
        # Make sure any 
        for i, row in obs_file.iterrows():
            if row['dim_item_id_7'] == 'All employees':
                row['dim_item_id_7'] = row['dim_item_id_8']

        # Put Some properly named Dimensions in
        obs_file['dim_id_7'] = obs_file['dim_id_7'].astype(str)
        obs_file['dim_id_8'] = obs_file['dim_id_8'].astype(str)
        obs_file['dim_id_7'] = 'Age Group'
        obs_file['dim_id_8'] = 'Occupation'
        obs_file['dimension_label_eng_7'] = obs_file['dim_id_7']        
        obs_file['dimension_label_eng_8'] = obs_file['dim_id_8']
        
        # Tidy up
        obs_file['dimension_item_label_eng_7'] = obs_file['dim_item_id_7']
        obs_file['dimension_item_label_eng_8'] = obs_file['dim_item_id_8']       

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------------------------------------
        
        
    if numASHE in ['15', 'holdingvalue']:
        obs_file['dim_item_id_7'] = obs_file['dim_item_id_7'].astype(str)
        obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].astype(str)
        obs_file['dim_item_id_9'] = obs_file['dim_item_id_9'].astype(str)
        
        # We need to genericise all the roles. Getting rid of the nationality frome ach line
        thatlist = ['Northern Ireland', 'Scotland', 'United Kingdom', 'Wales', 'South West', 'South East', 'London', 
                    'East', 'West Midlands', 'East Midlands', 'Yorkshire and The Humber', 'North West', 'North East']
        
        obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(str.strip)
        obs_file['dim_item_id_7'] = obs_file['dim_item_id_7'].map(str.strip)
        
        for i, row in obs_file.iterrows():
            for each in thatlist:
                if each in row['dim_item_id_8']:
                    row['dim_item_id_8'] = row['dim_item_id_8'][len(each):]
        
        obs_file = obs_file[(obs_file['observation'] != '') | (obs_file['data_marking'] != '')]        
        
        obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].str.lstrip(', ')
        obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].str.lstrip('st, ')
        obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'] + ' (' + obs_file['dim_item_id_9'].map(str.strip) + ')'
        obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].map(lambda x: x.replace(' ()', 'Total'))
        obs_file['dimension_item_label_eng_8'] = obs_file['dim_item_id_8']
        obs_file = tf.dismiss(obs_file, ['dim_id_9'])
        
        obs_file = obs_file.sort(['measure_type_eng'])  
        
        # Get rid of the silly quote marks
        obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].str.lstrip('"')
        obs_file['dim_item_id_8'] = obs_file['dim_item_id_8'].str.rstrip('"')
        obs_file['dimension_item_label_eng_8'] = obs_file['dim_item_id_8']
        
        # Sort out the labels
        obs_file['dim_id_8'][:-1] = 'Occupation'
        obs_file['dimension_label_eng_8'] = obs_file['dim_id_8']
        
        obs_file['dim_id_7'][:-1] = 'Area'
        obs_file['dimension_label_eng_7'] = obs_file['dim_id_7']
     
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------------------------------------
     
     
    # Adding the Appropriate names for the last dimension/s
    if numASHE in ['2', '3']:
        obs_file['dim_id_5'][:-1] = 'Occupation'
        obs_file['dimension_label_eng_5'] = obs_file['dim_id_5']
    if numASHE in ['5', '4', '21']:
        obs_file['dim_id_5'][:-1] = 'Industry'
        obs_file['dimension_label_eng_5'] = obs_file['dim_id_5']
    if numASHE in ['25', '13']:
        obs_file['dim_id_5'][:-1] = 'Sector'
        obs_file['dimension_label_eng_5'] = obs_file['dim_id_5']
    


    
    
    """
    END OF CONDITIONALS
    """

    # Modify the filename to get the name of the CV file, then load it
    new_file = load_file.replace('-ASHE_', ' CV-ASHE_')
    new_file = new_file.replace('a ', 'b ')
    new_file = new_file.replace('recipe', 'recipe2')    
    
    # TODO - tidy this up
    new_file = new_file.replace('Areb', 'Area')
    CV_file = pd.read_csv(new_file, dtype=object)
    CV_file.fillna('', inplace=True)
    
    # Load in the CV values
    obs_file['observation_type'] = 'CV'
    obs_file['obs_type_value'] = CV_file['observation']
    # Make sure to clear out and nan values as we're about to search for blanks
    CV_file.fillna('', inplace=True)
    obs_file['obs_type_value'][obs_file['obs_type_value'] == ''] = CV_file['data_marking']
    
    
    """
    SORTING OUT THE SEGMENTATION    
    """
    # its value for the main segment    
    obs_file['dim_id_2'] = 'Earnings Statistics'
    obs_file['measure_type_eng'] = 'Value'
    
    # Number of jobs segment
    obs_file['dim_id_2'][obs_file['dim_item_id_2'] == 'Number of jobs (thousand)'] = 'Indicative number of jobs'
    obs_file['dim_item_id_2'][obs_file['dim_item_id_2'] == 'Number of jobs (thousand)'] = 'Indicative number of jobs'
    obs_file['measure_type_eng'][obs_file['dim_item_id_2'] == 'Indicative number of jobs'] = 'Count'

    # 
    obs_file['measure_type_eng'][obs_file['dim_item_id_2'] == 'Annual percentage change in Mean'] = 'Percentage Change'
    obs_file['measure_type_eng'][obs_file['dim_item_id_2'] == 'Annual percentage change in Median'] = 'Percentage Change'
    obs_file['dim_id_2'][obs_file['measure_type_eng'] == 'Percentage Change'] = 'Annual Percentage Change'

    #
    obs_file['dim_item_id_2'][obs_file['dim_item_id_2'] == 'Earnings'] = 'Earnings Statistics'

    # Fill out the labels for the
    obs_file['dimension_item_label_eng_2'] = obs_file['dim_item_id_2']
    obs_file['dimension_label_eng_2'] = obs_file['dim_id_2']

    """
    -end of segmentation bit
    """

    # Clean any transform spill over onto the last line
    headers = list(obs_file.columns.values)
    for header in headers[2:]:
        obs_file[header][-1:] = ''   
    
    # Get the table value from the filename
    chunks = load_file.split('a ')
    if 'Area' in load_file:
        wanted = chunks[1]
    else:
        wanted = chunks[0]
    chunks = wanted.split('.')
    wanted = chunks[1]
    print 'Transform for Tables ' + str(wanted)    
    
    
obs_file.to_csv('merge_file_' + str(wanted) + '.csv', index=False)

