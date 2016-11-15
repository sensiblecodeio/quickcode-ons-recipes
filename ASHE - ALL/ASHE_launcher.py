# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:02:25 2015

@author: Mike

"""

###########################################################################################

"""
Launcher
Provides a quickie interface if a number wasnt passed as an argument. If it was we use it and skip the
print to screen stuff
"""

import sys
if sys.argv[1] == 'prompt':

    # Capture user input to get the ASHE number
    print ''
    print '---------------------------------'
    print 'ASHE DATA TRANSFORMATION SCRIPTS'
    print '--------------------------------'
    print 'This script will generate both datasets for a single ASHE subject(i.e ASHE7 or ASHE12)'
    print ''
    print 'Before continuing make sure to have all source files for the chosen'
    print 'dataset unzipped in the same folder as this script.'
    print ''
    which_ASHE = raw_input('Enter the ASHE number then press return: .. ')
    print ''
else:
    which_ASHE = sys.argv[1]


import os

# Get the unique argument for each file from the filename
# i.e ' Get 'Working Pay - Gross' out of the filename 'Work Geography Table 7.1a   Weekly pay - Gross 2013.csv' 
def unique_me(filename):
    filenames = filename.split('.')
    del filenames[0]
    filenames = filenames[0]
    filenames = filenames[3:-5]
    filenames = filenames.strip()
    return filenames


###########################################################################################

"""

There are the parameters automatically being passed for each dataset

There's  a fair amount of repition but this lets you adapt to meet changes in a table
without rewriting the whole codebase.

@args:
"some text" - The text value for column A for the last value we want
            it's usuallt "Nor Classified" or "Northern Ireland" but
            doesn't have to be
            
BoldNobold etc - a switch for the various ways the spreadsheet are formatted
            Bold - hierarchy denoted by higher levels items in bold
            Nobold - standard
            BoldNWhite- hierarchy denoted by both bold and indentation
            NoBoldClipped - standard but slice away the first 13 rows of obervations
            (because they appear twice and would cause sparsity in the dataset)
            
Y/N - do we want to inlcude the row identified by arg 1 "some text" in our extraction
            
"""

dict_1 = {'ASHE1': '"absence" NoBold N',
          'ASHE2': '"Not Classified" Bold N',
          'ASHE3': '"Not Classified" Bold Y',
          'ASHE4': '"NOT CLASSIFIED" Bold Y',
          'ASHE5': '"affected by absence" Bold N',
          'ASHE6': '"Not Classified" NoBold N',
          'ASHE7': '"Not Classified" NoBold N',
          'ASHE8': '"Not Classified" NoBold N',
          'ASHE9': '"Northern Ireland" NoBold Y',
          'ASHE10': '"Northern Ireland" NoBold Y',
          'ASHE11': '"Not Classified" NoBoldClipped N',
          'ASHE12': '"Not Classified" NoBoldClipped N',
          'ASHE13': '"Not Classified" NoBold N',
          'ASHE14': '"Not Classified" Bold N',
          'ASHE15': '"Not Classified" Bold N',
          'ASHE16': '"Not Classified" NoBold N',
          'ASHE17': '"Not Classified" NoBold N',
          'ASHE18': '"Not Classified" NoBold N',
          'ASHE19': '"Not Classified" NoBold N',
          'ASHE20': '"Not Classified" BoldnWhite N',
          'ASHE21': '"Not Classified" BoldnWhite N',
          'ASHE22': '"Not Classified" NoBold N',
          'ASHE23': '"Not Classified" NoBold N',
          'ASHE24': '"Not Classified" NoBold N',
          'ASHE25': '"Not Classified" Bold N',
          'ASHE26': '"Not Classified" NoBold N',
          }

###########################################################################################

"""
THIS BUILDS THREE LISTS OF COMMANDS TO BE AUTOMATICALLY EXECUTED AT THE COMMAND LINE

* bakelista - list of datbaker recipes and arguments/parameters for extraction 'a' sheets
* bakelistb - list of datbaker recipes and arguments/parameters for extraction 'b' sheets 
* tranlist - script to merge and finalise each a & b combination, into merge_1 through merge_12
Note - the scripts are always executed in this 1-2-3 order.

These lists are both populated using 'which_ASHE', the information from the dictionaries and the 
information inherent in the filenames.

"""

bakelista = []
bakelistb = []
tranlist = []

# Create a list of all files
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Cut it downt so it's just the excels
ff = [] # ff  = final file(s)

for f in files:
    if 'Table ' + str(which_ASHE) in f:
        if 'data'not in f:
            if 'transform' not in f:
                if 'preview' not in f:
                    if 'b ' not in f:
                        ff.append(f)

fdone = [] # the files from ff we're gonna start processing on
for each in ff:
    if 'a ' in each:
        fdone.append(each)

# Build key for dictionary
x = 'ASHE' + str(which_ASHE)

# Build commands for bakelist a and b
for i in fdone:  
    # First the 'a' version
    line = 'bake --preview ASHE_recipe.py "' + str(i) + '" "' + str(unique_me(i)) + '" D1 D2 ' + dict_1[x]
    bakelista.append(line)
                     
    # Then make a 'b' version
    line = line.replace('a ', 'b ')
    line = line.replace('.xls', ' CV.xls')
    line = line.replace('ASHE_recipe.py', 'ASHE_recipe2.py')

    # TODO - messy swap back. Better ways to do this
    line = line.replace('Areb', 'Area')

    bakelistb.append(line)


# Build tranlist
# You can extrapolate the databaked version of the files from the intial name but the formatting
# changes. This section makes those changes then creates the transform commands.
# note - D1 and D2 are holding values for dimension name 1 and 2. Theyre overwritten later but we have to use something.
for i in fdone:

    # if its not a b table
    if 'b ' not in i: 

        # Clean up dict_2 item to match the post-processing change in format
        cleantext2 = '" D1 D2 ' + dict_1[x]
        
        # Get rid of quotes and replace spaces with commas'
        cleansplit = cleantext2.split('"')
        for each in range(0, len(cleansplit) - 1):
            if each != 2:
                cleansplit[each] = cleansplit[each].replace('"', '')
                cleansplit[each] = cleansplit[each].replace(' ', ',')
        cleantext2 = ''.join(cleansplit)
        
        # Assorted other changes
        cleantext2 = cleantext2 + '.csv'
        cleantext2 = cleantext2.replace('Classified ','Classified,')
        cleantext2 = cleantext2.replace(' Bold',',Bold')
        cleantext2 = cleantext2.replace(' NoBold',',NoBold')
        cleantext2 = cleantext2.replace(' Mixed',',Mixed')
        cleantext2 = cleantext2.replace(' N.csv',',N.csv')
        cleantext2 = cleantext2.replace(' Y.csv',',Y.csv')
     
        # create the final transform command
        # NOTE - theres a varaible for which_ASHE attached to the end here
        # this lets the transform script know which table it is (and what conditional changes to apply)
        tranlist.append('python transform_ASHE.py "data-' + str(i)[:-4] + '-ASHE_recipe-' + str(unique_me(i))
        + cleantext2 + '" ' + str(which_ASHE))

  
###########################################################################################

"""
EXECUTING THE COMMANDS
executes 1st command in bakelista
executes 1st command in bakelistb
executes 1st command in tranlist

repeats sequence for 2nd, third etc

Also generates a txt file called 'execute.txt'. This file will hold the full sequence of commands
so a user can execute individual pieces (or make a correction) without re-running the whole thing.
"""

# Create an execute.txt of all commands to be run
f = open('execute.txt','w')
for count in range(0, len(tranlist)):
    
    f.write(bakelista[count])
    f.write('\n')
    f.write(bakelistb[count])  
    f.write('\n')
    f.write(tranlist[count])
    f.write('\n')

f.close()  


# executing the databaker recipes
import subprocess as sp  

for count in range(0, len(tranlist)):

    # extract table a
    p = sp.Popen(bakelista[count], shell=True)          # run each command 
    p.communicate()  

    # extract table b
    p = sp.Popen(bakelistb[count], shell=True)          # run each command 
    p.communicate()  
    
    # merge / transform
    p = sp.Popen(tranlist[count], shell=True)            # run each command     
    p.communicate()  
    
    
######################################################################
# Merge the files to finish

from ASHE_merger import merge_hours, merge_earnings

merge_earnings(which_ASHE, fdone)
merge_hours(which_ASHE, fdone)

