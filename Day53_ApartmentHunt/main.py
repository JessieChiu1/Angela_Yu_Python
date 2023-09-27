import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

time.sleep(5)
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
from bs4 import BeautifulSoup

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

# ======================================
# Navigating Apartment.com with selenium
# ======================================

# searchbar
# =========
wait = WebDriverWait(driver, timeout=30)

searchbar = driver.find_element(By.ID, value="quickSearchLookup")
searchbar.send_keys("Brooklyn, NY")
search_button = driver.find_element(By.CLASS_NAME, value="go")
search_button.click()

# input bed parameter
# ==================

# IDK why selecting the bed parameter has to first, if we set the price parameter first, the input bed parameter section will nto work
wait.until(EC.element_to_be_clickable((By.ID, "bedRangeLink")))
bed_option_button = driver.find_element(By.ID, value="bedRangeLink")
print("found bed option button")
bed_option_button.click()

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".minBedOptions li:nth-child(2)")))
one_bed_option = driver.find_element(By.CSS_SELECTOR, ".minBedOptions li:nth-child(2)")
print("found 1bedroom option")
one_bed_option.click()

# input price parameter
# =====================

wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "rentRangeSelector")))
price_option_button = driver.find_element(By.CLASS_NAME, value="rentRangeSelector")
price_option_button.click()

wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "maxRentInput")))
max_rent = driver.find_element(By.CLASS_NAME, value="maxRentInput")
max_rent.send_keys("2700")
max_rent.send_keys(Keys.ENTER)

# function for web scrapping the apartment information
# ====================================================
apartment_list = []


def get_apartments_info():
    time.sleep(5)
    driver.refresh()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#placardContainer")))
    apartments = driver.find_elements(By.CSS_SELECTOR, "#placardContainer .mortar-wrapper:not(.carouselSpinner)")
    print(len(apartments))
    for apartment in apartments:
        try:
            # find address
            if " Brooklyn, NY" not in apartment.find_element(By.CLASS_NAME, "property-address").text:
                apartment_address = apartment.find_element(By.CLASS_NAME, "property-title").get_attribute("title")
            else:
                apartment_address = apartment.find_element(By.CLASS_NAME, "property-address").text

            # find url
            apartment_url = apartment.find_element(By.CLASS_NAME, "property-link").get_attribute("href")

            # find price
            try:
                apartment_price_element = apartment.find_element(By.CLASS_NAME, "property-pricing")
                apartment_price = apartment_price_element.text
            except NoSuchElementException:
                try:
                    apartment_price_element = apartment.find_element(By.CLASS_NAME, "price-range")
                    apartment_price = apartment_price_element.text
                except NoSuchElementException:
                    try:
                        apartment_price_element = apartment.find_element(By.CLASS_NAME, "property-rents")
                        apartment_price = apartment_price_element.text
                    except NoSuchElementException:
                        apartment_price = "Price not found"
            # create object and appending to list
            apartment_data = {
                "address": apartment_address,
                "url": apartment_url,
                "price": apartment_price
            }
            print(apartment_data)
            apartment_list.append(apartment_data)
        except NoSuchElementException or InvalidSelectorException as e:
            print(apartment.get_attribute("outerHTML"))
            print(e)
            raise SystemExit



get_apartments_info()