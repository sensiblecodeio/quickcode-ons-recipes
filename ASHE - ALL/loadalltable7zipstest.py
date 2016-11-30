# Simply do everything all at once
import zipfile, io, re, os
from tempfile import NamedTemporaryFile
import pandas as pd

alltabs = [ ]

dirname = "table7zips"
dfiles = os.listdir(dirname)
dfiles.sort(reverse=True)
for dfile in dfiles:
    zfile = os.path.join(dirname, dfile)
    print("opening", zfile)
    zdir = zipfile.ZipFile(zfile)
    xlsfilenames = zdir.namelist()
    for xlsfilename in xlsfilenames:
        z = zdir.read(xlsfilename)
        print(" zfile", xlsfilename, len(z))
        tf = NamedTemporaryFile("w+b", suffix=".xls")
        tf.write(z)
        k = pd.read_excel(tf.name, sheetname=None)
        print(k.keys())
        len(k["All"].columns)

print("There are this many tables: ", len(tabs))
print("Square sizes are", [len(tab)*len(tab.columns)  for tab in tabs])
