from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ===========
# init driver
# ===========

url = "https://orteil.dashnet.org/cookieclicker/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# ===============
# Choose Language
# ===============

# init wait
wait = WebDriverWait(driver, 10)
# wait for the english language button to pop up
wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))

# click the English button language
en_button = driver.find_element(By.ID, "langSelect-EN")
en_button.click()

# ==================
# Selecting elements
# ==================

wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))


# =========
# functions
# =========


def click_cookie(count):
    big_cookie = driver.find_element(By.ID, value="bigCookie")
    for _ in range(count):
        big_cookie.click()


def buy_store():
    store_container = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
    store_container.reverse()
    # buy all possible upgrade from most expensive to least
    for store in store_container:
        store.click()


def buy_upgrade():
    upgrade_container = driver.find_elements(By.CSS_SELECTOR, value=".crate.upgrade")
    # this just buy the first upgrade since when you buy an upgrade, it disappears, and it will run into the StaleElementReferenceException error
    if upgrade_container:
        upgrade_container[0].click()


# =============
# gameplay loop
# =============

while True:
    click_cookie(50)
    buy_upgrade()
    buy_store()
