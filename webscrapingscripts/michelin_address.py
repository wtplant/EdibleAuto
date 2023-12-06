# -*- coding: utf-8 -*-
"""
Created on Sat May 16 16:45:16 2020

@author: William
"""

import requests
from bs4 import BeautifulSoup 

r=requests.get("https://ny.eater.com/maps/michelin-starred-restaurants-nyc-2020")

r.content

'''double check below line'''

soup = BeautifulSoup(r.content)

f = open("Michelin.csv", "w")
#header = "Restaurants"
f.write("Address")
    
for m in soup.find_all("div", {"class":"c-mapstack__info"}):
     m.get("href")
     
     f.write(m.div.text)
     
f.close()
     