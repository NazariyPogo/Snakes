#The purpose of this program is to print out all article titles on the New York Times homepage
#WARNING - Crashes during runtime have occasionally occurred

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/sitemap/today/'      #URL for the NYT sitemap for all articles posted TODAY
title_list = []                                         #MAY NOT WORK AFTER 01/28/2024

def get_website_data(url):
    r = requests.get(url)
    return r.text

url_html = get_website_data(url)

soup = BeautifulSoup(url_html, 'html.parser')       #Retrieves incoming data from NYT site map and organizes into HTML tree

find_correct_parent = soup.select('.css-cmbicj')    #Locates all u1 tags where the correct one is at index 0 (hardcoded option)
                                                        #This is done because other indexes added include NYT collections, videos,
                                                        #and 'other' daily pieces
                                                            #Also, NYT has changing css-xxxxxx tags making this harder to maintain

tag = find_correct_parent[0].find_all('li')         #Identifies all tags containing article titles

for x in tag:                                       #Takes string form of article titles and places it into a new list
    title_list.append(x.string)

for x in title_list:                                #Print out the list in an orderly fashion
    print(x)







#ALTERNATE VERSION USING THE NYT HOMEPAGE - RESULTS WILL BE DIFFERENT FROM SITE MAP



url = 'https://www.nytimes.com'      #URL for the NYT sitemap for all articles posted TODAY
title_list = []

def get_website_data(url):
    r = requests.get(url)
    return r.text

url_html = get_website_data(url)

soup = BeautifulSoup(url_html, 'html.parser')       #Retrieves incoming data from NYT site map and organizes into HTML tree

find_correct_parent = soup.select('.story-wrapper') #Finds all sections that are involved with stories (has other stuff too that
tag = []                                            #is parsed out later)

for x in find_correct_parent:                       #Finds specific tag in subsection that contains text
    tag += x.find_all('p', class_ = 'indicate-hover')

for x in tag:                                       #Takes string form of article titles and places it into a new list
    title_list.append(x.string)

title_list = title_list[0:len(title_list)-12]       #Remove unneeded links to Wordle, Crossword, and other apps
title_list = list(set(title_list))                  #Removes copies of articles which DOES happen

for x in title_list:                                #Print out the list in an orderly fashion
    print(x)