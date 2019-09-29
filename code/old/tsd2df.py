# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:23:24 2019

@author: tkhal
"""
# Load the Pandas libraries with alias 'pd' 
import pandas as pd 

import numpy as np
# Read data from file 'csvfilename.csv'  for TSD 

csvfilename = 'track site data.CSV'

rawdata = pd.read_csv(csvfilename ,sep=';')

#df = rawdata[rawdata.type == ('distant signal' or 'balise' or 'main signal' )]
#df=df[~df['DATE'].isin(['2015-10-30.1', '2015-11-30.1', '2015-12-31.1'])]
df=rawdata[rawdata['type'].isin(['distant signal' , 'balise' , 'main signal'])]

