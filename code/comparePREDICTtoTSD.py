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
import pyproj
import gc

#%% load dataframe with track site data to tsddf

# Read data from file 'csvfilename.csv'  for TSD 

tsdfilename = 'track site data.CSV'

rawtsddata = pd.read_csv(tsdfilename ,sep=';')


tsddf=rawtsddata[rawtsddata['type'].isin(['distant signal' , 'balise' , 'main signal'])]
tsddf = tsddf.reset_index() 
tsddf = tsddf.drop(['index'], axis=1)

del rawtsddata

#%% get the dist col to the dataset dfdist

# functions to  Get GPS from exif functions

def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()

def get_labeled_exif(exif):
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val

    return labeled

def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    return geotagging

def get_decimal_from_dms(dms, ref):

    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1] / 60.0
    seconds = dms[2][0] / dms[2][1] / 3600.0

    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return round(degrees + minutes + seconds, 5)

def get_coordinates(geotags):
    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

    return (lat,lon)
 
# loop through files and put file name and gps in array

directory = "Trackpictures_LoRes/001_-_Landquart_-_Klosters_Platz"
arr = []

for filename in os.listdir(directory):
    if filename.endswith(".JPG") :
#        print(os.path.join(directory, filename))
        #print(filename)
        exif = get_exif(os.path.join(directory, filename))
        geotags = get_geotagging(exif)
        #print(get_coordinates(geotags))
        lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])
        lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])
        arr.append([filename,lon,lat])

    else:
        continue

#array to CSV file 

#pd.DataFrame(arr).to_csv("file1.csv",index=False)

dfdist = pd.DataFrame(arr)

dfdist['dist'] = 0.0

dfdist.dtypes


geod = pyproj.Geod(ellps='WGS84')

  
lstlon = 0
lstlat = 0
disttot = 0
for index, row in dfdist.iterrows():
    
        if index != 0: 
            #print( index , row[1])
            az12,az21,dist =  geod.inv(lstlon, lstlat, row[1], row[2])
            #print(type(dist))
            disttot = disttot + dist
            dfdist.loc[index,'dist'] = round(disttot,2)
            #row.dist = 1
        lstlon = row[1]
        lstlat = row[2]
del   lstlon ,lstlat,disttot  ,dist ,lat ,lon 
del filename ,exif, geotags, index ,row, arr ,az12 ,az21 ,tsdfilename ,directory 
#df.to_csv("file103.csv",index=False)
gc.collect()
#%% load prediction data to PRDdf

prdfilename = 'prediction.csv'

prddf = pd.read_csv(prdfilename ,sep=';')


#%% compare the prediction to the tsd if not the same check for the dist 

cmprarr = ['filename','type','path','lon','lat']
cmprarrin = []
 = pd.DataFrame(cmprarr)
index2 = 0
truepath = "t"

for index, row in prddf.iterrows():
     cmprarrin.append( prddf.loc[index,1])#filename
     cmprarrin.append( prddf.loc[index,2])#typ
     if prddf.loc[index,2] == tsddf.loc[index,2]:
         #cmprarrin.append( tsddf.loc[index,2])
         cmprarrin.append( 0 )
         
         index2 = index2 + 1
     else:
         
         if tsddf.loc[index,3] == tsddf.loc[index,3] :
             print("error with prediction")
             break
         else:
             
             if truepath == "t":
                 while prddf.loc[index,2] != tsddf.loc[index,2]:
                     truepath = tsddf.loc[index,3]
                     index2 = index2 + 1
             else:
                 while tsddf.loc[index,3] != truepath:
                     index2 = index2 + 1
                 
                    
                 cmprarrin.append( truepath )#path
                 # get location from data base
                 cmprarrin.append( dfdist[dfdist['1'] == prddf.loc[index,1]] )#lon
                 cmprarrin.append( dfdist[dfdist['1'] == prddf.loc[index,2]]  )#lat
                      
     
     cmpdf.append(cmprarrin)
     cmprarrin = []

cmpdf.to_csv("finaldatabase.csv",index=False)
    



        

