from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ===========
# init driver
# ===========
url = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# making the screen bigger since smaller window size affects the webpage layout
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# ============
# find element
# ============

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)

# =======================
# find searchbar and type
# =======================
# for some reason the ENTER is not registering and teh searchbutton wasn't clickable
# turnout if I wait for element to be clickable, I can click it.....

searchbar = driver.find_element(By.CLASS_NAME, "cdx-text-input__input")
searchbar.send_keys("Python")
# searchbar.send_keys(Keys.ENTER)

search_button = driver.find_element(By.CSS_SELECTOR, "#searchform button")

# Explicitly wait for the search button to be clickable
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#searchform button")))

search_button.click()