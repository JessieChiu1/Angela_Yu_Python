from selenium import webdriver
from selenium.webdriver.common.by import By

# ===========
# init driver
# ===========

url = "https://www.python.org/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# =============
# find elements
# =============

event_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu time")
event_link = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu a")

# =================
# create dictionary
# =================

event_dict = []

for i in range(0, len(event_time)):
    event = {
        "name": event_link[i].text,
        "link": event_link[i].get_attribute("href"),
        "date": event_time[i].text
    }
    event_dict.append(event)

print(event_dict)