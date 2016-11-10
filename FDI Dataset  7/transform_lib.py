 # -*- coding: utf-8 -*-
"""
Spyder Editor

Developing basic reusable functions to help transforn data with Pandas.

Author: Mike
"""

import inspect, os
import pandas as pd
import glob


def validateheaders(myframe):
    standard_headings = ['dim_id_', 'dimension_label_eng_', 'dimension_label_cym_', 'dim_item_id_',
    'dimension_item_label_eng_', 'dimension_item_label_cym_', 'is_total_', 'is_sub_total']
    for count in range(35, len(myframe.columns.values), 8):
        for x in range(0, 8):
              myframe.rename(columns={myframe.columns[count+x]: standard_headings[x] + str((count-35) / 8 + 1)}, inplace=True)
    return myframe


"""
Clean trailing zeroes from Time
USAGE (Assuming imported as tf) ..... myframe = tf.clean_time(myframe)
"""

def clean_time(myframe):
    
    myframe['time_dim_item_id'] = myframe['time_dim_item_id'].astype(str)
    myframe['time_dim_item_label_eng'] = myframe['time_dim_item_label_eng'].astype(str)
    
    myframe['time_dim_item_id'] = myframe['time_dim_item_id'].map(lambda x: x.replace('.0', '')).astype(str)
    myframe['time_dim_item_label_eng'] = myframe['time_dim_item_label_eng'].map(lambda x: x.replace('.0', '')).astype(str)

    return myframe
    


"""
Autosorting all fields
USAGE (Assuming imported as tf) ..... myframe = tf.sort(myframe)
"""
def sort(myframe):
    
    headers = list(myframe.columns.values)

    check_list = []
    for each in headers:        
        if "dim_id" in each:
            if "time" not in each:
                check_list.append(each)            

    count_list = []
    for each in check_list:    
        if myframe[each].nunique() > 1:
            count_list.append([each, myframe[each].nunique()])            
    
    changes = 0
    for each in count_list:
        if each[1] > changes:
            changes = each[1]
     
    # To change to high > low, change to .... range(2, changes)       
    for each in range(changes, -1, -1):
            for header in count_list:
                if each == header[1]:
                    myframe = myframe.sort(header[0])
                    print "Auto sorting on: " + str(header)
    
    return myframe
    
        
"""
A remove command for removing a list of quoted text from a list of columns.
"""
def remove_from_columns(myframe, headers, items):
    
        for each in headers:
            myframe[each] = myframe[each].astype(str)
            for item in items:
                myframe[each] = myframe[each].map(lambda x: x.replace(item, ''))
                myframe[each] = myframe[each].map(str.strip)
        return myframe



"""
Dismiss command for unwanted items. Will remove all 8 relevant columns.
"""
def dismiss(myframe, headers):
    
    for each in headers:
        Column1 = myframe.columns.get_loc(each)
        for x in range(1, 9):
            myframe = myframe.drop(myframe.columns[Column1], axis=1)
        # print 'Dismissed ' + str(each) + ' and associated fields.'
    return myframe
    
        

"""
- Combine all CSVs in a director -' 
Take a boolean true/false and a list as args. This can either be CSV you want combined. Or the CSVs from the directory you DONT want combined.
Examples: ....  
myframe = load(True, ['file2.csv'])                    # loads only file2.csv from the current directory
myframe = load(False, ['file2,csv'])                   # loads and combines all files in the directory EXCEPT file2.csv
myframe = load(True, ['file2.csv', 'file4.csv'])       # loads and combines only files 2 and 4 from the current directory. 

"""


def load(mode, filenames):
       
    import glob
    import inspect, os
   
    # use inspect and os to get the current filepath        
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
       
    # Use glob to get a list of of all CSVs in current directory. Create an empty dataframe.
    allFiles = glob.glob(path + "/*.csv")
    myframe = pd.DataFrame()
    list = []
        
    # Read in each file from from that list, skip the footer
    print "Combining files:"
    for file in allFiles:
        if mode == True:
            do_combine = False
            for myfile in filenames: 
                if file[len(path)+1:] == myfile:
                        do_combine = True
        if mode == False:
            do_combine = True
            for myfile in filenames:
                if file[len(path)+1:] in filenames:
                        do_combine = False
        if do_combine == True:                        
                        print file[len(path):]    
                        df = pd.read_csv(file)
                        list.append(df)
                        myframe = pd.concat(list)
    
    myframe = myframe[myframe['observation'] != '*********']    
    myframe = myframe.reset_index()    
        
    # Add file footer
    count = len(myframe)
    myframe = myframe.set_value(len(myframe), 'observation', '*********')
    myframe = myframe.set_value(len(myframe) -1, 'data_marking', count)

    myframe['data_marking'] = myframe['data_marking'].astype(str)
    myframe['data_marking'] = myframe['data_marking'].map(lambda x: x.replace('.0', ''))

    myframe.fillna('', inplace = True)
    myframe = myframe.drop('index', 1)

    return myframe         
       
       
       
"""
Combine all CSVs in a directory - with exceptions!
A lists of strings is also passed as 'exclusions'. If the filename contains any string in this list it is NOT conbined with the others.
"""

def combine_without(exclusions):

    # use inspect and os to get the current filepath        
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 

    # Combine all the CVs
    allFiles = glob.glob(path + "/*.csv")
    myframe = pd.DataFrame()
    list = []
    
    # Output to screen stuff
    print "---------------------------"
    print "Creating Combine (WITHOUT) File using path:" + path
    print "-- file list --"
    
    # for each file - decide whether to combine it based on exclusions list
    for file in allFiles:
        filename = file[len(path):]
        processYN = True                
        for each in exclusions:
            if filename.find(each) > 0:
                processYN = False
          
        # if we are processing, creating a list of datafrane and concatentate them.
        if processYN == True:
            print filename
            df = pd.read_csv(file,index_col=None, engine='python', skipfooter=True, header=0, dtype=object)
            list.append(df)
            myframe = pd.concat(list)
    
    print "---------------------------"
    print " "
  
    # Get ALL headers from the datafrane. Iterate through them, making them all strings
    allheaders = list(myframe.columns.values)    
    for each in allheaders:
        myframe[each] = myframe[each].astype(str)
      
    # Add file footer
    count = len(myframe)
    myframe = myframe.set_value(len(myframe), 'observation', '*********')
    myframe = myframe.set_value(len(myframe) -1, 'data_marking', count)
    
    myframe['data_marking'] = myframe['data_marking'].astype(str)
    myframe['data_marking'] = myframe['data_marking'].map(lambda x: x.replace('.0', '')).astype(str)
    
    return myframe

"""
Combine all CSVs in a directory - with exceptions!
A lists of strings is also passed as 'exclusions'. If the filename contains any string in this list it is NOT conbined with the others.
"""

def combine_with(inclusions):

    # use inspect and os to get the current filepath        
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 

    # Combine all the CVs
    allFiles = glob.glob(path + "/*.csv")
    myframe = pd.DataFrame()
    list = []
    
    # Output to screen stuff
    print "---------------------------"
    print "Creating Combine (WITHOUT) File using path:" + path
    print "-- file list --"
    
    # for each file - decide whether to combine it based on inclusions list
    for file in allFiles:
        filename = file[len(path):]
        processYN = False                
        for each in inclusions:
            if filename.find(each) > 0:
                processYN = True
          
        # if we are processing, creating a list of datafrane and concatentate them.
        if processYN == True:
            print filename
            df = pd.read_csv(file,index_col=None, engine='python', skipfooter=True, header=0, dtype=object)
            list.append(df)
            myframe = pd.concat(list)
    
    print "---------------------------"
    print " "
  
    # Get ALL headers from the datafrane. Iterate through them, making them all strings
    allheaders = list(myframe.columns.values)    
    for each in allheaders:
        myframe[each] = myframe[each].astype(str)
      
    # Add file footer
    count = len(myframe)
    myframe = myframe.set_value(len(myframe), 'observation', '*********')
    myframe = myframe.set_value(len(myframe) -1, 'data_marking', count)
    
    myframe['data_marking'] = myframe['data_marking'].astype(str)
    myframe['data_marking'] = myframe['data_marking'].map(lambda x: x.replace('.0', '')).astype(str)
    
    return myframe
