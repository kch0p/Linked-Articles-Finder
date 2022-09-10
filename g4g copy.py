# https://www.kindacode.com/article/extract-all-links-from-a-webpage-using-python-and-beautiful-soup-4/
import requests
from bs4 import BeautifulSoup
 
def has_numbers(inputString):
	return any(char.isdigit() for char in inputString)
 
url = 'https://www.slowboring.com/p/racism-is-a-big-deal'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
links = soup.select('a')
 
# Print out the result
for link in links:
  if link.get('href') != None:
    if 'https://' in link.get('href') and 'comment' not in link.get_text() and has_numbers(link.get_text()) == False and link.get_text() != ' ':
      print('\n',link.get_text(), ' ',link.get('href'))





# urls = []
# for link in soup.select('a'):
# 	if link.get_text() != None and 'https://' in link.get('href'): 
# 		print(link.get_text().title,' ',link.get('href'))
# 		print('----------------------------') # Just a line break

	# test = link.get('href')
	# # wrong_list = ['javascript','footnote','/tos'] #tried doing this but couldn't find a NOT LIKE equivilant in python
	# if test is not None and 'javascript' not in test and 'footnote' not in test and '/tos' not in test and 'subscribe' not in test: 
	# 	print('\n', link.get_text(),' ', link.get('href'))