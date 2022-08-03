#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import json
import os
import datetime


# In[4]:


d = datetime.datetime.today()
dd=(d.year,d.month,d.day)
area='ha5' #areas can be find in here "https://www.data.jma.go.jp/mscweb/data/himawari/"

typ = 'tre' #tre,trm,irv,dnc,dms,dst,b08,b03,b13,cve

FILEJSON = (r'C:\Users\Tharusha\Documents\Himawari Imgs Downloader\him_img.json') 
with open(FILEJSON, 'r') as fson:  
        res = json.load(fson)
rest = res['list']        
for t in rest:
    time=t['time']
    url = (f'https://www.data.jma.go.jp/mscweb/data/himawari/img/{area}/{area}_{typ}_{time}.jpg')
    with open(time +'.jpg', 'wb') as f:
        im = requests.get(url)
        f.write(im.content)
        print(time, 'Done.')


# In[ ]:




