# eot-recipes

QuickCode for ONS recipes and sample files for DataBaker.

Run with `bake <recipe> <spreadsheets>`

## Fixtures

Files in `csv_out` have been generated with Python 2.7:

```
chardet==2.3.0
databaker==1.1.1
docopt==0.6.2
html5lib==0.999999999
json-table-schema==0.2.1
lxml==3.6.4
messytables==0.15.1
PyHamcrest==1.9.0
python-dateutil==2.5.3
python-magic==0.4.12
requests==2.11.1
six==1.10.0
webencodings==0.5
xlrd==1.0.0
xlutils==2.0.0
xlwt==1.1.2
xypath==1.1.0
```

These can be used for comparing the behaviour of a "known good" and
development versions of databaker.

The 1.1.1 version is the version the ONS have been using as of the time
of writing.

## `compare.py`

This is a Python script to compare the output of a git diff of CSVs. It
was used to check that modified values only differed in precision
between Python 2 and 3.

See comments in the script for more information.
