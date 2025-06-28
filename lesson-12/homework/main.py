## task 1
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

## task 2
from bs4 import BeautifulSoup
import sqlite3
import requests
import csv

jobs = []
url = "https://realpython.github.io/fake-jobs/"

con = sqlite3.connect("/media/asadbek/D/maab/new/python-homeworks/lesson-12/homework/jobs.db")
cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS jobs(title text unique, company text unique, location text unique, description text, link text)")
cnt = cursor.execute("select count(*) from jobs").fetchone()

def job_exists(title, company, location):
    job = cursor.execute("select * from jobs where title = ?and company = ? and location = ?", (title, company, location)).fetchone()
    return not job is None

def insert(job):
    query = "insert into jobs (title, company, location, description, link) values (?, ?, ?, ?, ?)"
    cursor.execute(query, (job['title'], job['company'], job['location'], job['description'], job['link']))
    con.commit()

def update(job):
    print(tuple(job.values()))
    cursor.execute("update jobs set title = ?, company = ?, location = ?, description = ?, link = ?", tuple(job.values()))
    con.commit()

def filter_by(key, val):
    jobs = cursor.execute('select * from jobs where ? = ?', (key, val)).fetchall()
    return jobs

def write_csv(jobs):
    with open("/media/asadbek/D/maab/new/python-homeworks/lesson-12/homework/jobs.db", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(['id', 'title', 'company', 'description', 'location', 'link'] + jobs)


soup = BeautifulSoup(requests.get(url).text, 'html.parser')
cards = soup.select('div.card-content')

for card in cards:
    link = card.footer.select('a')[1]['href']
    job = {
        'title' : card.select_one('div.media-content h2.title').text,
        'company' : card.select_one('div.media-content h3.subtitle').text,
        'location' : card.select_one('div.content p.location').text,
        'link' : link
    }
    job_soup = BeautifulSoup(requests.get(link).text)
    job['description'] = job_soup.select_one('div.content p').text
    if not job_exists(job['title'], job['company'], job['location']):
        insert(job)
        print(job['title'], "- insert")
    else:
        update(job)
        print(job['title'], "- update")


## task 3
import time
import json
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(), options=options)

driver.get("https://www.demoblaze.com")
time.sleep(3)

laptops_tab = driver.find_element(By.LINK_TEXT, "Laptops")
laptops_tab.click()
time.sleep(3)

laptops_data = []

while True:
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    items = soup.find_all("div", class_="card-block")

    for item in items:
        try:
            name = item.find("a").text.strip()
            price = item.find_next("h5").text.strip()
            description = item.find_next("p").text.strip()

            laptops_data.append({
                "name": name,
                "price": price,
                "description": description
            })
        except:
            continue

    try:
        next_btn = driver.find_element(By.ID, "next2")
        if 'disabled' in next_btn.get_attribute('class'):
            break
        next_btn.click()
        time.sleep(3)
    except:
        break

driver.quit()

with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptops_data, f, indent=2)

print(f"Scraped {len(laptops_data)} laptops. Saved to laptops.json")