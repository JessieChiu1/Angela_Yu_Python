from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# ===========
# init driver
# ===========

# https://stackoverflow.com/questions/49921128/selenium-cant-click-element-because-other-element-obscures-it
url = "https://www.apartments.com/"
google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSflgA-TY8ajr5t8_0pdLtMzT5K_Mtpkxz0WlScOlkrlaSzl7g/viewform?usp=sf_link"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# ===============================
# Navigating Zillow with selenium
# ===============================

# searchbar
# =========
wait = WebDriverWait(driver, 10)

searchbar = driver.find_element(By.ID, value="quickSearchLookup")
searchbar.send_keys("Brooklyn, NY")
search_button = driver.find_element(By.CLASS_NAME, value="go")
search_button.click()

# input bed parameter
# ==================
# IDK why selecting the bed parameter has to first, if we set the price parameter first, the input bed parameter section will nto work
wait.until(EC.element_to_be_clickable((By.ID, "bedRangeLink")))
bed_option_button = driver.find_element(By.ID, value="bedRangeLink")
bed_option_button.click()

wait.until((EC.element_to_be_clickable((By.XPATH, '//*[@id="bedsMinMaxRangeControl"]/div/div/div/div/div[3]/div/button'))))
max_bed_container = driver.find_element(By.XPATH, value='//*[@id="bedsMinMaxRangeControl"]/div/div/div/div/div[3]/div/button')
max_bed_container.click()

one_bed_option = driver.find_element(By.XPATH, value='//*[@id="bedsMinMaxRangeControl"]/div/div/ul[2]/li[3]')
one_bed_option.click()

# input price parameter
# =====================
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "rentRangeSelector")))
price_option_button = driver.find_element(By.CLASS_NAME, value="rentRangeSelector")
price_option_button.click()

max_rent = driver.find_element(By.CLASS_NAME, value="maxRentInput")
max_rent.send_keys("2000")
max_rent.send_keys(Keys.ENTER)