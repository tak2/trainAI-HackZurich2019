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


#%% load dataframe with track site data

# Read data from file 'csvfilename.csv'  for TSD 

csvfilename = 'track site data.CSV'

rawtsddata = pd.read_csv(csvfilename ,sep=';')

#df = rawdata[rawdata.type == ('distant signal' or 'balise' or 'main signal' )]
#df=df[~df['DATE'].isin(['2015-10-30.1', '2015-11-30.1', '2015-12-31.1'])]
tsddf=rawtsddata[rawtsddata['type'].isin(['distant signal' , 'balise' , 'main signal'])]


tsddf = tsddf.reset_index() 

tsddf = tsddf.drop(['index'], axis=1)

tsddf['Altline'] = 0
#%%
locarr = ['LQ','MALA','GRUS','SCRS','FUWI','JAZ','FID','KUEB','CAPA','SAAS','SERN','KLOD','KLO']
trdf =pd.DataFrame() 
import numpy as np
temparry =[]
#localtdf =tsddf.loc[ tsddf['location abreviation']== 'SCRS']
#%%

for item in locarr:
    #print (item)
    
    localtdf = tsddf.loc[ tsddf['location abreviation']== item]
    #print(localtdf)
    #trdf[item] = np.nan
    #print(localtdf["additional information"].dropna().unique())
    temunqarr = localtdf["additional information"].dropna().unique()
    temparry.append(item)
    for altlocrt in temunqarr:
        print(altlocrt)
        temparry.append(altlocrt)
    print(temparry)
    
    trdf.append(temparry)
    print(trdf)
    temparry =[]
    #temunqarr = []
    #temunqarr = localtdf["additional information"].dropna().unique()
    localtdf = localtdf[0:0]

    


#%%
    '''
for i in range(len(tsddf)) : 
   # print(tsddf.loc[i, "additional information"])
   if tsddf.loc[i, "additional information"] == tsddf.loc[i, "additional information"] : 
            #print(tsddf.loc[i, "additional information"])
            tsddf.loc[i, "Altline"] = tsddf.loc[i, "additional information"] + tsddf.loc[i, "location abreviation"]
#%%'''
