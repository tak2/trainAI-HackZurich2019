# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 01:11:00 2019

@author: tkhal
"""

import os


from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS

import numpy
import pandas as pd 
import numpy as np
import re
#%% load dataframe with track site data to tsddf

# Read data from file 'csvfilename.csv'  for TSD 

csvfilename = 'track site data.CSV'

rawtsddata = pd.read_csv(csvfilename ,sep=';')

#df = rawdata[rawdata.type == ('distant signal' or 'balise' or 'main signal' )]
#df=df[~df['DATE'].isin(['2015-10-30.1', '2015-11-30.1', '2015-12-31.1'])]
tsddf=rawtsddata[rawtsddata['type'].isin(['distant signal' , 'balise' , 'main signal'])]
tsddf = tsddf.reset_index() 
tsddf = tsddf.drop(['index'], axis=1)


#%% load prediction data to 

