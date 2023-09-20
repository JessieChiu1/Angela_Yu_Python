from selenium import webdriver
from selenium.webdriver.common.by import By

# ===========
# init driver
# ===========

url="http://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# =========
# Fill form
# =========

first_name_input = driver.find_element(By.NAME, value="fName")
last_name_input = driver.find_element(By.NAME, value="lName")
email_input = driver.find_element(By.NAME, value="email")
sign_up_button = driver.find_element(By.CLASS_NAME, value="btn")

first_name_input.send_keys("Jessie")
last_name_input.send_keys("Chiu")
email_input.send_keys("something@gmail.com")

sign_up_button.click()