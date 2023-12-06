''' from https://www.youtube.com/watch?v=3xQTJi2tqgk '''

import requests
from bs4 import BeautifulSoup 

r=requests.get("https://ny.eater.com/maps/michelin-starred-restaurants-nyc-2020")

r.content

'''double check below line'''

soup = BeautifulSoup(r.content)

f = open("Michelin.csv", "w")
#header = "Restaurants"
f.write("Address")

for x in soup.find_all("div", {"class":"c-mapstack__card-hed"}):
    x.get("href")

#for x in soup.find_all("div"):
    #f.write(x.div.h1.text)
    
    
    '''top part works, not sure if the x.get has any bearing on output'''
    
for t in soup.find_all("div", {"class":"c-mapstack__phone desktop-only"}):
     t.get("href")
    
     #f.write(t.text+(","))
    
for m in soup.find_all("div", {"class":"c-mapstack__info"}):
     m.get("href")
     
     f.write(m.div.text)
     
f.close()
     
     
     
    












