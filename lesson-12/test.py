from bs4 import BeautifulSoup
import requests
from pprint import pprint

url = "https://azimjon.com"

html = requests.get(url + "/blog").text
soup = BeautifulSoup(html)
tags = soup.select("div#archive a.list-item")
blog = [
    {
        "title" : item.find('div', class_ = 'title').text, 
        "date" : item.find('div', class_ = 'date').text,
        "link" : url + item['href'],
    } 
     for item in tags
]
pprint(blog)