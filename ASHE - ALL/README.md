# ONSdatabaker scripts - Annual summary of Hours and Earnings.


# SOURCE - https://github.com/ONS-OpenData/bau_ASHE

Please note. We use github for versioning purposes only. If anyone wants the actual data involved it will always be easily accessible via the ONS website (www.ons.gov.uk) and API service.

The ASHE data tables consist of a twice yearly release of 300+ large excel spreadsheets of data.

This repo is a generic "one size fits all" ONSdatabaker based sequence of scripts that can convert each table (22 spreadsheets each) into two datasets:

Earnings: tables 1-8

Hours: tables 9-11

This should work against all previous years but it's not fully tested (there is a lot) and there certainly will be issues regarding geographical hierarchy lookups (as these change with time).

The geography based tables are tables (7-12).


## Usage

1.) "Download as zip" from the above options and extract

2.) Download and extract the zip file for your chosen ASHE table 

3.) Double click the "CLICK TO RUN ON WINDOWS" batch file

4.) Enter the table number you're converting (7 for ASHE table 7 etc)


## Warnings

Unless you have a particuarly powerful computer processing some of the larger tables (ASHE 15 in particular) can lead to the processing freezing after the successful extraction of a spreadheet.

To get around this, when you run these scripts they will generate an execute.txt document, which contains the full sequence of commands being run. 

You can run these manually one at a time from the command line (just navigate to the directory and copy paste them in). They may freeze up after extraction (give it a minute or two after completion) but you can just shut it down or ctrl+break and move on to the next one.

If you run the commands manually this way, you'll need to finsh with the following command to merge the successfully extracted files:

```python ASHE_manual_merge.py <TABLE NUMBER> <YEAR> ```

for example:

```python ASHE_manual_merge.py 7 2013 ```


## Structure

This recipe is intended for use with a very specific legacy output structure. If you're a visitor and running (I wouldnt advise it - use the demo), you'll need to use the WDA structure_csv_user.py file stored elsewherer on our github.
