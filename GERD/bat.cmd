SET Excel_Sheet="rftberd2014datasets_tcm77-424594.xls"
SET Year="2014"

bake --preview GERD_recipe_main.py %Excel_Sheet% %Year%
bake --preview GERD_small_pairs.py %Excel_Sheet% %Year% "3" "6"
bake --preview GERD_small_pairs.py %Excel_Sheet% %Year% "8" "5"
bake --preview GERD_small_pairs.py %Excel_Sheet% %Year% "4" "15"
bake --preview GERD_small_pairs.py %Excel_Sheet% %Year% "9" "17"
bake --preview GERD_18_19_21_22.py %Excel_Sheet% %Year% "18" "19"
bake --preview GERD_18_19_21_22.py %Excel_Sheet% %Year% "21" "22"
