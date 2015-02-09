from databaker.constants import *

def per_file(tabs):
    return "*"

def per_tab(tab):
    print tab.excel_ref("B2").value
    print tab.excel_ref("B2").fill(RIGHT)
    print tab.excel_ref("B2").fill(DOWN)
    return []

