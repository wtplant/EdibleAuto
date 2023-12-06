
"""


@author: William

working off of this really good YouTube tutorial:
    https://www.youtube.com/watch?v=XQgXKtPSzUI
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

new_url = 'https://ny.eater.com/maps/michelin-starred-restaurants-nyc-2020'

'''Open up connection and grab the webpage and download it'''
uClient = uReq(new_url)
'''Then we read the html, but put it into BeautifulSoup first due to file size
Offloads the content into a variable'''
page_html = uClient.read()
'''then we close it'''
uClient.close()
'''now  we call the soup function to parse the html text'''
page_soup = soup(page_html, "html.parser")

'''using the get_text function'''
cards = page_soup.find_all("div", {"class":"c-mapstack__card-hed"})

for card in cards:
    menu=card.find_all("div", {"class":"c-mapstack__card-hed"})