# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:08:50 2019

@author: tkhal
"""



import os


from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS

import numpy

# Get GPS from exif functions

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

'''
exif = get_exif('samplepics\VIRB0022.0000.JPG')
geotags = get_geotagging(exif)
print(get_coordinates(geotags))
'''

 
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
import pandas as pd 
#pd.DataFrame(arr).to_csv("file1.csv",index=False)

df = pd.DataFrame(arr)

df['dist'] = 0.0

df.dtypes

#%%
import pyproj

geod = pyproj.Geod(ellps='WGS84')
'''
for city, coord in cities.items():
    lat0, lon0 = london_coord
    lat1, lon1 = coord
    
    azimuth1, azimuth2, distance = geod.inv(lon0, lat0, lon1, lat1)
    print(city, distance)
    print('    azimuth', azimuth1, azimuth2)
    '''
    
#%% load dataframe with track site data




#%%
lstlon = 0
lstlat = 0
disttot = 0
for index, row in df.iterrows():
    
        if index != 0: 
            #print( index , row[1])
            az12,az21,dist =  geod.inv(lstlon, lstlat, row[1], row[2])
            #print(type(dist))
            disttot = disttot + dist
            df.loc[index,'dist'] = round(disttot,2)
            #row.dist = 1
        lstlon = row[1]
        lstlat = row[2]
       
df.to_csv("file103.csv",index=False)

