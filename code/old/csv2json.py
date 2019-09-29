# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 20:30:29 2019

@author: tkhal
"""

import csv
import json

csvfile = open('sample1.csv', 'r')
jsonfile = open('file3.json', 'w')
'''
fieldnames = ("IdLocnumTypOrder","lon","lat")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    #print(row)
    json.dump(row, jsonfile)
    jsonfile.write('\n')
    '''
    #%%

import pandas as pd
csv_file = pd.DataFrame(pd.read_csv(csvfile, sep = ",", header = 0, index_col = False))
csv_file.to_json(jsonfile, orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)

