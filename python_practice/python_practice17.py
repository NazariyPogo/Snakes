#The purpose of this program is to print out all article titles on the New York Times homepage

import requests
from bs4 import BeautifulSoup

# url = 'https://www.nytimes.com/sitemap/today/'      #URL for the NYT sitemap for all articles posted 01/28/2024
# title_list = []

# def get_website_data(url):
#     r = requests.get(url)
#     return r.text

# url_html = get_website_data(url)

# soup = BeautifulSoup(url_html, 'html.parser')       #Retrieves incoming data from NYT site map and organizes into HTML tree

# find_correct_parent = soup.select('.css-cmbicj')    #Locates all u1 tags where the correct one is at index 0 (hardcoded option)
#                                                         #This is done because other indexes added include NYT collections, videos,
#                                                         #and 'other' daily pieces
#                                                             #Also, NYT has changing css-xxxxxx tags making this harder to maintain

# tag = find_correct_parent[0].find_all('li')         #Identifies all tags containing article titles

# for x in tag:                                       #Takes string form of article titles and places it into a new list
#     title_list.append(x.string)

# for x in title_list:                                #Print out the list in an orderly fashion
#     print(x)











# url = 'https://www.nytimes.com/sitemap/today/'      #URL for the NYT sitemap for all articles posted 01/28/2024
# title_list = []

# def get_website_data(url):
#     r = requests.get(url)
#     return r.text

# url_html = get_website_data(url)

# soup = BeautifulSoup(url_html, 'html.parser')       #Retrieves incoming data from NYT site map and organizes into HTML tree

# find_correct_parent = soup.select('.css-cmbicj')    #Locates all u1 tags where the correct one is at index 0 (hardcoded option)
#                                                         #This is done because other indexes added include NYT collections, videos,
#                                                         #and 'other' daily pieces
#                                                             #Also, NYT has changing css-xxxxxx tags making this harder to maintain

# tag = find_correct_parent[0].find_all('li')         #Identifies all tags containing article titles

# for x in tag:                                       #Takes string form of article titles and places it into a new list
#     title_list.append(x.string)

# for x in title_list:                                #Print out the list in an orderly fashion
#     print(x)