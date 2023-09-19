from selenium import webdriver
from selenium.webdriver.common.by import By

# This is to add options to not automatically close chrome when program finish running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://www.amazon.com/dp/B0788884DF?ref=nb_sb_ss_w_as-reorder-t1_k4_1_11&amp=&crid=3GWM5HP0EPN08&sprefix=dermashield&th=1"

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# how to locate elements: https://selenium-python.readthedocs.io/locating-elements.html
price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
price = float(f"{price_whole.text}.{price_fraction.text}")
print(price)

# .quit will close out the whole driver, .close will close a tab
driver.quit()
