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

