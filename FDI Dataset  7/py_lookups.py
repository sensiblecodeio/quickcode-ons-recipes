# -*- coding: UTF-8 -*-
 
def cat_lookup(myframe, header):
    this_lookup = [
          ["Acquisition of foreign companies' share & loan capital","Acquisition of share & loan capital"],
          ["Acquisition of UK companies' share & loan capital","Acquisition of share & loan capital"],
          ["Amount due to foreign parent companies on branch-head office account at end period","Amount due to companies on branch-head office account at end period"],
          ["Amount due to foreign parent companies on inter-company account at end period","Amount due to parent companies on inter-company account at end period"],
          ["Amount due to UK parent companies on branch head-office account at end period","Amount due to companies on branch-head office account at end period"],
          ["Amount due to UK parent companies on inter-company account at end period","Amount due to parent companies on inter-company account at end period"],
          ["Disposal of foreign companies' share & loan capital","Disposal of companies' share & loan capital"],
          ["Disposal of UK companies' share & loan capital","Disposal of companies' share & loan capital"],
          ["Less dividends paid to foreign parent companies","Less dividends paid to parent companies"],
          ["Less dividends received by UK companies","Less dividends paid to parent companies"],
          ["Net interest accrued by UK companies","Net interest accrued"],
          ["Net interest accrued to foreign parent companies","Net interest accrued"],
          ["Net profits","Net Profits"],
          ["Total net FDI earnings abroad","Total net FDI earnings"],
          ["Total net FDI earnings in the UK","Total net FDI earnings"],
          ["Total net FDI international investment position abroad at end period","Total net FDI international investment position at end period"],
          ["Total net FDI international investment position in the UK at end period","Total net FDI international investment position at end period"],
          ["Total net foreign direct investment in the UK","Total net investment"],
          ["UK companies' share of foreign companies' net profits","UK companies' share of foreign companies' net profits"],
          ["Unremitted profits (reinvested earnings)","Unremitted profits (reinvested earnings)"],
          ["Increase in amounts due to foreign parents on inter-company account","Increase in amounts due on inter-company account"],
          ["Increase in amounts due to UK parents on branch head-office account","Increase in amounts due on inter-company account"],
          ["Investment Abroad","Investment Abroad"],
          ["Foreign companies' share of UK companies' net profits","Foreign companies' share of UK companies' net profits"],
          ["UK companies' share of foreign companies' net profits","UK companies' share of foreign companies' net profits"],
          ["Foreign companies' share of UK companies' share capital and reserves at end period","Foreign companies' share of UK companies' share capital and reserves at end period"],
          ["UK companies' share of foreign companies' share capital and reserves at end period","UK companies' share of foreign companies' share capital and reserves at end period"],
          ["Increase in amounts due to foreign parents on branch head-office account","Increase in amounts due to foreign parents on branch head-office account"],
          ["Increase in amounts due to UK parents on inter-company account","Increase in amounts due to UK parents on inter-company account"],
    ]
    myframe[header] = myframe[header].astype(str)
    for each in this_lookup:
        myframe[header] = myframe[header].replace(each[0], each[1])
    myframe[header] = myframe[header]
    myframe[header] = myframe[header].map(str.strip)
    return myframe
 
# -*- coding: UTF-8 -*-
 
def type_lookup(myframe, header):
    this_lookup = [
          ["Foreign branches","Branches"],
          ["Foreign subsidiaries and associates","Subsidiaries and associates"],
          ["Total net FDI earnings abroad","Total net FDI earnings"],
          ["Total net FDI earnings in the UK","Total net FDI earnings"],
          ["Total net FDI international investment position abroad at end period","Total net FDI international investment position at end period"],
          ["Total net FDI international investment position in the UK at end period","Total net FDI international investment position at end period"],
          ["investment abroad","Total net investment"],
          ["Total net foreign direct investment in the UK","Total net investment"],
          ["UK branches","Branches"],
          ["UK subsidiaries and associates","Subsidiaries and associates"],
    ]
    myframe[header] = myframe[header].astype(str)
    for each in this_lookup:
        myframe[header] = myframe[header].replace(each[0], each[1])
    myframe[header] = myframe[header]
    myframe[header] = myframe[header].map(str.strip)
    return myframe
 
# -*- coding: UTF-8 -*-
 
def correct_text(myframe, header):
    this_lookup = [
          ["Foreign companies' share of UK companies' net profits1,2","UK subsidiaries and associates - Foreign companies' share of UK companies' net profits1,2"],
          ["Net interest accrued to foreign parent companies","UK subsidiaries and associates - Net interest accrued to foreign parent companies"],
          ["Amount due to foreign parent companies on inter-company account at end period","UK subsidiaries and associates - Amount due to foreign parent companies on inter-company account at end period"],
          ["Foreign companies' share of UK companies' share capital and reserves at end period","UK subsidiaries and associates - Foreign companies' share of UK companies' share capital and reserves at end period"],
          ["Amount due to foreign parent companies on branch-head office account at end period","UK branches - Amount due to foreign parent companies on branch-head office account at end period"],
          ["Foreign parent companies' share of UK companies' net profits1,2","UK subsidiaries and associates - Foreign parent companies' share of UK companies' net profits1,2"],
          ["Less dividends paid to foreign parent companies3","UK subsidiaries and associates - Less dividends paid to foreign parent companies3"],
          ["Unremitted profits (reinvested earnings)","UK subsidiaries and associates - Unremitted profits (reinvested earnings)"],
          ["Acquisition of UK companies' share & loan capital","UK subsidiaries and associates - Acquisition of UK companies' share & loan capital"],
          ["Disposal of UK companies' share & loan capital","UK subsidiaries and associates - Disposal of UK companies' share & loan capital"],
          ["Increase in amounts due to foreign parents on inter-company account","UK subsidiaries and associates - Increase in amounts due to foreign parents on inter-company account"],
          ["Increase in amounts due to foreign parents on branch head-office account","UK branches - Increase in amounts due to foreign parents on branch head-office account"],
    ]
    myframe[header] = myframe[header].astype(str)
    for each in this_lookup:
        myframe[header] = myframe[header].replace(each[0], each[1])
    myframe[header] = myframe[header]
    myframe[header] = myframe[header].map(str.strip)
    return myframe
 
