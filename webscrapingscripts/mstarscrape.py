''' from https://www.youtube.com/watch?v=3xQTJi2tqgk '''

import requests
from bs4 import BeautifulSoup 

r=requests.get("https://guide.michelin.com/us/en/new-york-state/new-york/restaurants/3-stars-michelin")

r.content

'''double check below line'''

soup = BeautifulSoup(r.content)

for x in soup.find_all("div"):
    x.get("href")

#for x in soup.find_all("div"):
    print (x.text)











