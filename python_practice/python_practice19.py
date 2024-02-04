#The purpose of this program is to print out a multi-page article's text

from bs4 import BeautifulSoup
import requests

def print_article(request):
    soup = BeautifulSoup(request.text, "html.parser")
    res = soup.select(".entry-content > p")
    text = []

    for x in res:
        text.append(x.text)

    text = text[1:len(text)-2]

    # for x in text:
    #     print(x)
    print(text)

if __name__ == "__main__":
    r = requests.get("https://content.time.com/time/magazine/article/0,9171,2005869-1,00.html")
    r2 = requests.get("https://content.time.com/time/magazine/article/0,9171,2005869-2,00.html")
    print_article(r)
    print_article(r2)