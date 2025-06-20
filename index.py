import csv
import time
from selenium import webdriver  
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless") 
options.add_argument("--disable-gpu")

driver_path = "C:/Users/ASUS/OneDrive/Masaüstü/chromedriver-win64/chromedriver.exe"
driver = webdriver.Chrome(service=Service(driver_path), options=options)

base_url = "https://yox.la/baki/yasayis-kompleksleri"

all_data = []

for page_num in range(1, 28):
    if page_num == 1:
        url = base_url
    else:
        url = f"{base_url}?page={page_num}"
    print(f"Səhifə {page_num} yuklenir: {url}")

    driver.get(url)
    time.sleep(2)

    cards = driver.find_elements(By.CLASS_NAME, "y-list-item")
    if not cards:
        print("Bu səhifədə yaşayış kompleksi tapılmadı.")
        break

    for card in cards:
        name = card.find_element(By.CLASS_NAME, "title").text.strip()

        all_data.append((name,))

print(f"Ümumi {len(all_data)} yaşayış kompleksi tapıldı.")

driver.quit()

with open("yasayis_kompleksleri.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Ad"])
    writer.writerows(all_data)

print("Məlumat 'yasayis_kompleksleri.csv' faylına yazıldı.")
