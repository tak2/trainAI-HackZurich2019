# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 13:50:36 2019

@author: tkhal
"""

import os


from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS

#import numpy

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


directory = 'samplepics'
arr = []

for filename in os.listdir(directory):
    if filename.endswith(".JPG") :
#        print(os.path.join(directory, filename))
        print(filename)
        exif = get_exif(os.path.join(directory, filename))
        geotags = get_geotagging(exif)
        print(get_coordinates(geotags))
        lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])
        lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])
        arr.append([filename,lon,lat])

    else:
        continue

#array to CSV file 
import pandas as pd 
pd.DataFrame(arr).to_csv("file1.csv",index=False)

