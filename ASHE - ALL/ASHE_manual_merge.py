# -*- coding: utf-8 -*-
"""
Created on Wed May 04 15:18:17 2016

@author: Mike
 
Manual running code
Re-creates the automatic inputs and lets someone skip straight to merging the final files

"""

import sys
from ASHE_merger import *

# Which table
which_ASHE = sys.argv[1]

# Adds a load of filler to year and puts it in a list, so the script can execute wihout conditionals
fdone = []
fdone.append(sys.argv[2] + '####')

# runs merge scripts
merge_earnings(which_ASHE, fdone)
merge_hours(which_ASHE, fdone)