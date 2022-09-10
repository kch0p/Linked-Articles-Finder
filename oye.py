# https://medium.com/@adeoyewole/scraping-news-articles-in-python-53c567282e25

import requests
from bs4 import BeautifulSoup


url = requests.get('https://www.slowboring.com/p/racism-is-a-big-deal') 
soup = BeautifulSoup(url.content, 'html.parser')


page_weblinks = soup.find_all('article')
articles = []

for link in page_weblinks:
    url = link.find_all('a')[0]       
    print(url)
# print(page_weblinks)