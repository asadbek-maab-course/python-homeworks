from bs4 import BeautifulSoup
from pprint import pprint

with open("/media/asadbek/D/maab/new/python-homeworks/lesson-12/homework/weather.html", "r") as f:
    html = f.read()
soup = BeautifulSoup(html)
header = soup.thead.select('th')
table = {'head' : [], 'data' : []}
for item in header:
    table['head'].append(item.text)
rows = soup.tbody.select('tr')
for row in rows:
    lst = row.select('td')
    table['data'].append({
        "day" : lst[0].text, 
        "temp" : lst[1].text, 
        "con" : lst[2].text
    })

def get_high_temp(data):
    days = []
    max_temp = 0
    for day in data['data']:
        if int(day['temp'][0:-3]) > max_temp:
            max_temp = int(day['temp'][0:-3])
            days = [day]
        elif int(day['temp'][0:-3]) == max_temp:
            days.append(day)
    return days
def get_sunny(data):
    return [day for day in data['data'] if day['con'] == "Sunny"]

print(get_high_temp(table))
print(get_sunny(table))
