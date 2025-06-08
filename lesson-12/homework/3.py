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