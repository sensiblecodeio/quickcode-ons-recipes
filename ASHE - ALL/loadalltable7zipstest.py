# Simply do everything all at once
import zipfile, io, re, os, time
from tempfile import NamedTemporaryFile
import pandas as pd
import resource

filesizes = [ ]
zipxlssizes = [ ]
alltabs = [ ]

print("resource before", resource.getrusage(resource.RUSAGE_SELF))

t0 = time.time()
dirname = "table7zips"
dfiles = os.listdir(dirname)
dfiles.sort(reverse=True)
for dfile in dfiles:
    zfile = os.path.join(dirname, dfile)
    filesizes.append(os.path.getsize(zfile))
    print("opening", zfile)
    zdir = zipfile.ZipFile(zfile)
    xlsfilenames = zdir.namelist()
    for xlsfilename in xlsfilenames:
        z = zdir.read(xlsfilename)
        print(" zfile", xlsfilename, len(z))
        zipxlssizes.append(len(z))
        tf = NamedTemporaryFile("w+b", suffix=".xls")
        tf.write(z)
        k = pd.read_excel(tf.name, sheetname=None)
        alltabs.extend(list(k.values()))

print("Total files", len(filesizes), "combined bytes", sum(filesizes))
print("Total zippedxlsfiles", len(zipxlssizes), "combined bytes", sum(zipxlssizes))
cellcounts = [len(tab)*len(tab.columns)  for tab in alltabs]   # to prove they are simultaneously loaded 
print("Total tabs", len(alltabs), "combined cells", sum(cellcounts))
print("processing time", time.time() - t0)

print("resource after", resource.getrusage(resource.RUSAGE_SELF))
