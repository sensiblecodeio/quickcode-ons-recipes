#!/bin/sh
bake a02/a02.py a02/table-a02.xls
# Commented out because recipe doesn't work for this file.
# Results in xypath.xypath.NoCellsAssertionError.
# bake ashe/ashe13.py ashe/ashe_prov_2014.xls
bake ashe/ashe13.py ashe/ashe_rev_cv_2013.xls
bake census-2011-ccg/census-2011-ccg.py census-2011-ccg/Mid-2011-ccg-syoa-file.xls
# Commented out because recipe not available.
# bake earn01/earn01.py earn01/table-earn01.xls
bake earn03/earn03.py earn03/table-earn03.xls
mkdir -p csv_out && find . -name "data*.csv" -exec mv {} ./csv_out/ \; 
