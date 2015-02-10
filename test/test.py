from databaker.constants import *

def per_file(tabs):
    return "*"

def per_tab(tab):
    tab.set_header("kitten", "kitten")
    tab.excel_ref("A1").fill(RIGHT).is_header('top', UP, strict=True)
    return tab.excel_ref("B2").fill(RIGHT).fill(DOWN)

