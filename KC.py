from ast import main
from operator import contains
import requests
from bs4 import BeautifulSoup
import numpy as np # for np.char
from datetime import datetime



# PART 0 - SETUP
startTime = datetime.now()
 
def has_numbers(inputString):
	return any(char.isdigit() for char in inputString)

def link_checker(link):
	s = link.get('href')
	
	if s != None and 'comment' not in s and 'javascript' not in s and 'footnote' not in s and '/tos' not in s and 'profile' not in s and 'author' not in s and 'subscribe' not in s:
		return s



# PART 1 - COLLECTING URLS
main_url = 'https://www.slowboring.com/p/racism-is-a-big-deal'
reqs = requests.get(main_url)
soup = BeautifulSoup(reqs.text, 'html.parser')
links = soup.article.select('a') # original example: https://www.kindacode.com/article/extract-all-links-from-a-webpage-using-python-and-beautiful-soup-4/#:~:text=text%2C%20'html.parser')-,links%20%3D%20soup.select('a'),-%23%20Print%20out%20the
 

url_list = []

for link in links: 
	link_value = link_checker(link)

	if link_value not in url_list:
		url_list.append(link_value)

url_list = [ ele for ele in url_list if ele is not None ]



# PART 2 - COLLECTING URL INFO 
f = open("test1.md", "w")

for url in url_list:
	try:
		reqs = requests.get(url)
		soup = BeautifulSoup(reqs.text, 'html.parser')

		# data = (soup.title.string,url) # more on the simple soup.title portion: https://stackoverflow.com/questions/67119560/python-beautiful-soup-get-only-body-content-without-header-or-footer-data
		# print(data)
		f.write(soup.title.string)
		f.write('\n')
		f.write('\n')
		f.write('[')
		f.write(url)
		f.write(']')
		f.write('(')
		f.write(url)
		f.write(')')
		f.write('\n')
		f.write('\n')
	except:
		continue
f.write('\n')
f.write('\n')
f.write('\n')
f.write('time to collect articles: ')
time_needed = str((datetime.now() - startTime).seconds)
f.write(time_needed)
f.write('seconds.')
f.write('\n')
f.write('\n')
f.write('original article: ')
f.write('[')
f.write(main_url)
f.write(']')
f.write('(')
f.write(main_url)
f.write(')')
f.close()	




# PART 3 - WRITING FILES & OPENING IN BROWSWER
import webbrowser
import os
import markdown

with open('test1.md', 'r') as f:
    text = f.read()
    html = markdown.markdown(text)

with open('test1.html', 'w') as f:
    f.write(html)


filename = 'file:///'+os.getcwd()+'/' + 'test1.html'
webbrowser.open_new_tab(filename)