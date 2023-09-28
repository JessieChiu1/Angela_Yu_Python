import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException

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

# ====================================================
# Navigating Apartment.com with selenium and filtering
# ====================================================

# searchbar
# =========
wait = WebDriverWait(driver, timeout=30)

searchbar = driver.find_element(By.ID, value="quickSearchLookup")
searchbar.send_keys("Brooklyn, NY")
search_button = driver.find_element(By.CLASS_NAME, value="go")
search_button.click()

# input bed parameter
# ==================

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
max_rent.send_keys("2200")
max_rent.send_keys(Keys.ENTER)

# ============================
# web scrapping apartment page
# ============================
apartment_list = []


# functions
# =========
def get_apartments_info():
    """
    This function grabs all the apartment info on the current page
    :return: nothing, but the apartment_list will update with the new apartments we web scraped
    """
    # wait for the url to update with the new search research and refresh the page so we are querying the updated search result
    time.sleep(5)
    driver.refresh()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#placardContainer")))
    apartments = driver.find_elements(By.CSS_SELECTOR, "#placardContainer .mortar-wrapper:not(.carouselSpinner)")
    # for each of the apartment, identified the relevant information and create a dictionary of the apartment and push it to a list
    for apartment in apartments:
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
                    apartment_price = "PriceNotFound"
        # if the price is something like "$XXXX - $XXXX" I want to add the same unit with lower and upper bound price
        apartment_price = apartment_price.replace('$', '').replace(' ', '').replace('/mo', '').replace(',', '').split('-')

        # create object and appending to list, accounted for the price range!
        for price in apartment_price:
            apartment_data = {
                "address": apartment_address,
                "price": price,
                "url": apartment_url,
            }
            print(apartment_data)
            apartment_list.append(apartment_data)


def next_page():
    """
    This function will navigate to the next page if there is a next page
    :return: boolean
    """
    page_container = driver.find_element(By.ID, "paging")
    try:
        next_page_button = page_container.find_element(By.CLASS_NAME, "next")
        next_page_button.click()
        return True
    except NoSuchElementException:
        print("no more pages")
        return False


# web scrapping all apartments loop
# =================================

# get first page info
get_apartments_info()
# if there is a next page, get those apartment info also
while next_page():
    get_apartments_info()

# ============
# Fill in form
# ============

driver.get(google_form_url)
# loop through each apartment
for apartment in apartment_list:
    if "CallforRent" not in apartment['price'] and "PriceNotFound" not in apartment['price']:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_input.send_keys(apartment['address'])
        price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input.send_keys(apartment['price'])
        url_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        url_input.send_keys(apartment['url'])
        submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit_button.click()

        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
        submit_another = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        submit_another.click()

driver.quit()
