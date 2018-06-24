# Mengyao Liu
# mengyliu
# these should be the only imports you need
import requests
from bs4 import BeautifulSoup

# write your code here
# usage should be python3 part3.py

path = "https://www.michigandaily.com/"
response = requests.get(path)
soup = BeautifulSoup(response.text, "html.parser")

print("Michigan Daily -- MOST READ")
titles = soup.find("aside", {"class": "asidebar"}).find("div", {"class": "panel-pane pane-mostread"}).findAll("li")
for t in titles:
    next_url = path + t.a.get('href')
    title = t.a.get_text()
    print(title)
    next_response = requests.get(next_url)
    next_soup = BeautifulSoup(next_response.text, "html.parser")
    if next_soup.find("div", {"class": "view-content"}):
    	authors = next_soup.find("div", {"class": "view-content"}).findAll("div", {"class": "link"})
    	print('  by',end=' ')
    	for au in authors:
    		print(au.contents[0].string,end=' ');
    	print('')
    else:
    	author = next_soup.find("div", {"id": "article"}).find("p", {"class": "info"})
    	print("  {}".format(author.contents[0].string))