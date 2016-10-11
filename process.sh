#!/bin/sh -e
bake a02/a02.py a02/table-a02.xls

# Commented out because they generate very large files.
# bake abs/ABS01.py "abs/Annual Business Survey Standard Extracts 2014P (2).xlsx"
# bake abs/ABS01Extras.py "abs/Annual Business Survey Standard Extracts 2014P (2).xlsx"
bake abs/ABS01SICLabels.py "abs/Annual Business Survey Standard Extracts 2014P (2).xlsx"

# Commented out because recipe doesn't work for this file.
# Results in xypath.xypath.NoCellsAssertionError.
# bake ashe/ashe13.py ashe/ashe_prov_2014.xls
bake ashe/ashe13.py ashe/ashe_rev_cv_2013.xls

bake ASHE7/ASHE_recipe.py "ASHE7/PROV - Work Geography Table 7.10a   Paid hours worked - Basic 2015.xls" "Paid hours worked - Basic" D1 D2 "Not Classified" NoBold N
bake ASHE7/ASHE_recipe2.py "ASHE7/PROV - Work Geography Table 7.10b   Paid hours worked - Basic 2015 CV.xls" "Paid hours worked - Basic" D1 D2 "Not Classified" NoBold N

bake census-2011-ccg/census-2011-ccg.py census-2011-ccg/Mid-2011-ccg-syoa-file.xls

# Commented out because recipe not available.
# bake earn01/earn01.py earn01/table-earn01.xls

bake earn03/earn03.py earn03/table-earn03.xls

bake GERD/GERD_recipe_main.py GERD/rftberd2014datasets_tcm77-424594.xls 2014
bake GERD/GERD_small_pairs.py GERD/rftberd2014datasets_tcm77-424594.xls 2014 "3" "6"
bake GERD/GERD_small_pairs.py GERD/rftberd2014datasets_tcm77-424594.xls 2014 "8" "5"
bake GERD/GERD_small_pairs.py GERD/rftberd2014datasets_tcm77-424594.xls 2014 "4" "15"
bake GERD/GERD_small_pairs.py GERD/rftberd2014datasets_tcm77-424594.xls 2014 "9" "17"
bake GERD/GERD_18_19_21_22.py GERD/rftberd2014datasets_tcm77-424594.xls 2014 "18" "19"
bake GERD/GERD_18_19_21_22.py GERD/rftberd2014datasets_tcm77-424594.xls 2014 "21" "22"

bake ILCH/ILCH.py ILCH/ilchtablestemplatensa.xls growth
bake ILCH/ILCH.py ILCH/ilchtablestemplatensa.xls level
bake ILCH/ILCH.py ILCH/ilchtablestemplatesa.xls growth
bake ILCH/ILCH.py ILCH/ilchtablestemplatesa.xls level

bake MandA/Mergers_1_recipe.py MandA/rftmatables_tcm77-415727.xls
bake MandA/Mergers_2_5_recipe.py MandA/rftmatables_tcm77-415727.xls
bake MandA/Mergers_6_7_recipe.py MandA/rftmatables_tcm77-415727.xls "Table 6" "6A_Top"
bake MandA/Mergers_6_7_recipe.py MandA/rftmatables_tcm77-415727.xls "Table 6" "6A_Bottom"
bake MandA/Mergers_6_7_recipe.py MandA/rftmatables_tcm77-415727.xls "Table 6" "6D_Top"
bake MandA/Mergers_6_7_recipe.py MandA/rftmatables_tcm77-415727.xls "Table 6" "6D_Bottom"
bake MandA/Mergers_6_7_recipe.py MandA/rftmatables_tcm77-415727.xls "Table 7" "7A_Top"
bake MandA/Mergers_6_7_recipe.py MandA/rftmatables_tcm77-415727.xls "Table 7" "7A_Bottom"
bake MandA/Mergers_6_7_recipe.py MandA/rftmatables_tcm77-415727.xls "Table 7" "7D_Top"
bake MandA/Mergers_6_7_recipe.py MandA/rftmatables_tcm77-415727.xls "Table 7" "7D_Bottom"
bake MandA/Mergers_8or10_recipe.py MandA/rftmatables_tcm77-415727.xls "Table 8"
bake MandA/Mergers_8or10_recipe.py MandA/rftmatables_tcm77-415727.xls "Table 10"
bake MandA/Mergers_9_recipe.py MandA/rftmatables_tcm77-415727.xls

bake MFP/MFP_exp.py MFP/referencetablesunlinkedcorrection_tcm77-392175.xls

bake OTT/OTTArea.py OTT/referencetablesjune210815_tcm77-413962.xls
bake OTT/OTTPurpose.py OTT/referencetablesjune210815_tcm77-413962.xls
bake OTT/OTTEarnings.py OTT/referencetablesjune210815_tcm77-413962.xls

bake SecEstGDP/recipe.py SecEstGDP/gdpq3m2reftables_tcm77-425649.xls "A1 AGGREGATES" None Y
bake SecEstGDP/recipe.py SecEstGDP/gdpq3m2reftables_tcm77-425649.xls "A1 AGGREGATES" None Q
bake SecEstGDP/recipe.py SecEstGDP/gdpq3m2reftables_tcm77-425649.xls "A2 AGGREGATES" None Y
bake SecEstGDP/recipe.py SecEstGDP/gdpq3m2reftables_tcm77-425649.xls "A2 AGGREGATES" None Q
bake SecEstGDP/recipe.py SecEstGDP/gdpq3m2reftables_tcm77-425649.xls "B1 CVM OUTPUT" "B2 CVM OUTPUT" Y
bake SecEstGDP/recipe.py SecEstGDP/gdpq3m2reftables_tcm77-425649.xls "B1 CVM OUTPUT" "B2 CVM OUTPUT" Q
bake SecEstGDP/recipe.py SecEstGDP/gdpq3m2reftables_tcm77-425649.xls "C1 EXPENDITURE" "C2 EXPENDITURE" Y
bake SecEstGDP/recipe.py SecEstGDP/gdpq3m2reftables_tcm77-425649.xls "C1 EXPENDITURE" "C2 EXPENDITURE" Q
bake SecEstGDP/recipe.py SecEstGDP/gdpq3m2reftables_tcm77-425649.xls "D INCOME" None Y
bake SecEstGDP/recipe.py SecEstGDP/gdpq3m2reftables_tcm77-425649.xls "D INCOME" None Q
bake SecEstGDP/recipe.py SecEstGDP/gdpq3m2reftables_tcm77-425649.xls "H1 TRADE" "H2 TRADE" Y
bake SecEstGDP/recipe.py SecEstGDP/gdpq3m2reftables_tcm77-425649.xls "H1 TRADE" "H2 TRADE" Q
bake SecEstGDP/recipe.py SecEstGDP/gdpq3m2reftables_tcm77-425649.xls "L GVAbp" None Y
bake SecEstGDP/recipe.py SecEstGDP/gdpq3m2reftables_tcm77-425649.xls "L GVAbp" None Q

bake TT/TT_1or2_Table.py TT/section1travelandtourism1980to2014_tcm77-403561.xls
bake TT/TT_3_8.py TT/section1travelandtourism1980to2014_tcm77-403561.xls 1.03 1.04
bake TT/TT_3_8.py TT/section1travelandtourism1980to2014_tcm77-403561.xls 1.05 1.06
bake TT/TT_3_8.py TT/section1travelandtourism1980to2014_tcm77-403561.xls 1.07 1.08

mkdir -p csv_out && find . -path ./csv_out -prune -o -name "data*.csv" -exec mv {} ./csv_out/ \;
