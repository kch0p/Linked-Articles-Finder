import requests
from bs4 import BeautifulSoup
 
 
url = 'https://www.slowboring.com/p/racism-is-a-big-deal'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
	test = link.get('href')
	# wrong_list = ['javascript','footnote','/tos'] #tried doing this but couldn't find a NOT LIKE equivilant in python
	if test is not None and 'javascript' not in test and 'footnote' not in test and '/tos' not in test and 'subscribe' not in test: 
		print('\n', link.get_text(),' ', link.get('href'))