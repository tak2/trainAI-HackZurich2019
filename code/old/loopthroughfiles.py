# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 13:46:28 2019

@author: tkhal
"""

import os
directory = 'samplepics'

for filename in os.listdir(directory):
    if filename.endswith(".JPG") :
        print(os.path.join(directory, filename))
    else:
        continue
    
    
