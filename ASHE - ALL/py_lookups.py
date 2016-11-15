# -*- coding: UTF-8 -*-
# Some quick lookups required to render the various ASHE tables user friendly
 
def locatiionTOgeocode(myframe, header):
    this_lookup = [
          ["United Kingdom","K02000001"],
          ["Great Britain","K03000001"],
          ["England and Wales","K04000001"],
          ["England","E92000001"],
          ["Wales / Cymru","W92000004"],
          ["Northern Ireland","N92000002"],
          ["Scotland","S92000003"],
          ["North East","E12000001"],
          ["North West","E12000002"],
          ["Yorkshire and The Humber","E12000003"],
          ["East Midlands","E12000004"],
          ["West Midlands","E12000005"],
          ["East","E12000006"],
          ["London","E12000007"],
          ["South East","E12000008"],
          ["South West","E12000009"],
    ]
    myframe[header] = myframe[header].astype(str)
    for each in this_lookup:
        myframe[header] = myframe[header].replace(each[0], each[1])
    myframe[header] = myframe[header]
    myframe[header] = myframe[header].map(str.strip)
    return myframe

 
# -*- coding: UTF-8 -*-
 
def ASHE20(myframe, header):
    this_lookup = [
          ["","All Occupations"],
          ["1","Managers, directors and senior officials (1)"],
          ["11","Managers, directors and senior officials - Corporate managers and directors (11)"],
          ["12","Managers, directors and senior officials - Other managers and proprietors (12)"],
          ["2","Professional occupations (2)"],
          ["21","Professional occupations - Science, research, engineering and technology professionals (21)"],
          ["22","Professional occupations - Health professionals (22)"],
          ["23","Professional occupations - Teaching and educational professionals (23)"],
          ["24","Professional occupations - Business, media and public service professionals (24)"],
          ["3","Associate professional and technical occupations (3)"],
          ["31","Associate professional and technical occupations - Science, engineering and technology associate professionals (31)"],
          ["32","Associate professional and technical occupations - Health and social care associate professionals (32)"],
          ["33","Associate professional and technical occupations - Protective service occupations (33)"],
          ["34","Associate professional and technical occupations - Culture, media and sports occupations (34)"],
          ["35","Associate professional and technical occupations - Business and public service associate professionals (35)"],
          ["4","Administrative and secretarial occupations (4)"],
          ["41","Administrative and secretarial occupations - Administrative occupations (41)"],
          ["42","Administrative and secretarial occupations - Secretarial and related occupations (42)"],
          ["5","Skilled trades occupations (5)"],
          ["51","Skilled trades occupations - Skilled agricultural and related trades (51)"],
          ["52","Skilled trades occupations - Skilled metal, electrical and electronic trades (52)"],
          ["53","Skilled trades occupations - Skilled construction and building trades (53)"],
          ["54","Skilled trades occupations - Textiles, printing and other skilled trades (54)"],
          ["6","Caring, leisure and other service occupations (6)"],
          ["61","Caring, leisure and other service occupations - Caring personal service occupations (61)"],
          ["62","Caring, leisure and other service occupations - Leisure, travel and related personal service occupations (62)"],
          ["7","Sales and customer service occupations (7)"],
          ["71","Sales and customer service occupations - Sales occupations (71)"],
          ["72","Sales and customer service occupations - Customer service occupations (72)"],
          ["8","Process, plant and machine operatives - Process, plant and machine operatives (8)"],
          ["81","Process, plant and machine operatives -  plant and machine operatives (81)"],
          ["82","Process, plant and machine operatives - Transport and mobile machine drivers and operatives (82)"],
          ["9","Elementary occupations (9)"],
          ["91","Elementary occupations - Elementary trades and related occupations (91)"],
          ["92","Elementary occupations - Elementary administration and service occupations (92)"],
    ]
    myframe[header] = myframe[header].astype(str)
    for each in this_lookup:
        myframe[header] = myframe[header].replace(each[0], each[1])
    myframe[header] = myframe[header]
    myframe[header] = myframe[header].map(str.strip)
    return myframe
 

# -*- coding: UTF-8 -*-
 
def ASHE21(myframe, header):
    this_lookup = [
          ["A","Agriculture, forestry and fishing (A)"],
          ["1","Crop and animal production, hunting and related service activities (1)"],
          ["2","Forestry and logging (2)"],
          ["3","Fishing and aquaculture (3)"],
          ["B","Mining and quarrying (B)"],
          ["5","Mining of coal and lignite  (5)"],
          ["6","Extraction of crude petroleum and natural gas (6)"],
          ["7","Mining of metal ores (7)"],
          ["8","Other mining and quarrying (8)"],
          ["9","Mining support service activities (9)"],
          ["C","Manufacturing (C)"],
          ["10","Manufacture of food products (10)"],
          ["11","Manufacture of beverages (11)"],
          ["12","Manufacture of tobacco products (12)"],
          ["13","Manufacture of textiles (13)"],
          ["14","Manufacture of wearing apparel (14)"],
          ["15","Manufacture of leather and related products (15)"],
          ["16","Manufacture of wood and of products of wood and cork, except furniture; manufacture of articles of straw and plaiting materials (16)"],
          ["17","Manufacture of paper and paper products (17)"],
          ["18","Printing and reproduction of recorded media (18)"],
          ["19","Manufacture of coke and refined petroleum products (19)"],
          ["20","Manufacture of chemicals and chemical products (20)"],
          ["21","Manufacture of basic pharmaceutical products and pharmaceutical preparations (21)"],
          ["22","Manufacture of rubber and plastic products (22)"],
          ["23","Manufacture of other non-metallic mineral products (23)"],
          ["24","Manufacture of basic metals (24)"],
          ["25","Manufacture of fabricated metal products, except machinery and equipment (25)"],
          ["26","Manufacture of computer, electronic and optical products (26)"],
          ["27","Manufacture of electrical equipment (27)"],
          ["28","Manufacture of machinery and equipment n.e.c. (28)"],
          ["29","Manufacture of motor vehicles, trailers and semi-trailers (29)"],
          ["30","Manufacture of other transport equipment (30)"],
          ["31","Manufacture of furniture (31)"],
          ["32","Other manufacturing (32)"],
          ["33","Repair and installation of machinery and equipment (33)"],
          ["D","Electricity, gas, steam and air conditioning supply (D)"],
          ["35","Electricity, gas, steam and air conditioning supply (35)"],
          ["E","Water supply; sewerage, waste management and remediation activities (E)"],
          ["36","Water collection, treatment and supply (36)"],
          ["37","Sewerage (37)"],
          ["38","Waste collection, treatment and disposal activities; materials recovery (38)"],
          ["39","Remediation activities and other waste management services (39)"],
          ["F","Construction (F)"],
          ["41","Construction of buildings (41)"],
          ["42","Civil engineering (42)"],
          ["43","Specialised construction activities (43)"],
          ["G","Wholesale and retail trade; repair of motor vehicles and motorcycles (G)"],
          ["45","Wholesale and retail trade and repair of motor vehicles and motorcycles (45)"],
          ["46","Wholesale trade, except of motor vehicles and motorcycles (46)"],
          ["47","Retail trade, except of motor vehicles and motorcycles (47)"],
          ["H","Transportation and storage (H)"],
          ["49","Land transport and transport via pipelines (49)"],
          ["50","Water transport (50)"],
          ["51","Air transport (51)"],
          ["52","Warehousing and support activities for transportation (52)"],
          ["53","Postal and courier activities (53)"],
          ["I","Accommodation and food service activities (I)"],
          ["55","Accommodation (55)"],
          ["56","Food and beverage service activities (56)"],
          ["J","Information and communication (J)"],
          ["58","Publishing activities (58)"],
          ["59","Motion picture, video and television programme production, sound recording and music publishing activities (59)"],
          ["60","Programming and broadcasting activities (60)"],
          ["61","Telecommunications (61)"],
          ["62","Computer programming, consultancy and related activities (62)"],
          ["63","Information service activities (63)"],
          ["K","Financial and insurance activities (K)"],
          ["64","Financial service activities, except insurance and pension funding (64)"],
          ["65","Insurance, reinsurance and pension funding, except compulsory social security (65)"],
          ["66","Activities auxiliary to financial services and insurance activities (66)"],
          ["L","Real estate activities (L)"],
          ["68","Real estate activities (68)"],
          ["M","Professional, scientific and technical activities (M)"],
          ["69","Legal and accounting activities (69)"],
          ["70","Activities of head offices; management consultancy activities (70)"],
          ["71","Architectural and engineering activities; technical testing and analysis (71)"],
          ["72","Scientific research and development (72)"],
          ["73","Advertising and market research (73)"],
          ["74","Other professional, scientific and technical activities (74)"],
          ["75","Veterinary activities (75)"],
          ["N","Administrative and support service activities (N)"],
          ["77","Rental and leasing activities (77)"],
          ["78","Employment activities (78)"],
          ["79","Travel agency, tour operator and other reservation service and related activities (79)"],
          ["80","Security and investigation activities (80)"],
          ["81","Services to buildings and landscape activities (81)"],
          ["82","Office administrative, office support and other business support activities (82)"],
          ["O","Public administration and defence; compulsory social security (O)"],
          ["84","Public administration and defence; compulsory social security (84)"],
          ["P","Education (P)"],
          ["85","Education (85)"],
          ["Q","Human health and social work activities (Q)"],
          ["86","Human health activities (86)"],
          ["87","Residential care activities (87)"],
          ["88","Social work activities without accommodation (88)"],
          ["R","Arts, entertainment and recreation (R)"],
          ["90","Creative, arts and entertainment activities (90)"],
          ["91","Libraries, archives, museums and other cultural activities (91)"],
          ["92","Gambling and betting activities (92)"],
          ["93","Sports activities and amusement and recreation activities (93)"],
          ["S","Other service activities (S)"],
          ["94","Activities of membership organisations (94)"],
          ["95","Repair of computers and personal and household goods (95)"],
          ["96","Other personal service activities (96)"],
          ["T","Activities of households as employers; undifferentiated goods-and services-producing activities of households for own use (T)"],
          ["97","Activities of households as employers of domestic personnel (97)"],
          ["98","Undifferentiated goods- and services-producing activities of private households for own use (98)"],
          ["U","Activities of extraterritorial organisations and bodies (U)"],
          ["99","Activities of extraterritorial organisations and bodies (99)"],
    ]
    myframe[header] = myframe[header].astype(str)
    for each in this_lookup:
        myframe[header] = myframe[header].replace(each[0], each[1])
    myframe[header] = myframe[header]
    myframe[header] = myframe[header].map(str.strip)
    return myframe
 
