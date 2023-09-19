from selenium import webdriver
from selenium.webdriver.common.by import By

# Selenium is great because beautifulsoup fails when it takes time for the website to load or the website is built with React/Angular and it is responsive to user's click or interaction. With Selenium, you can mimic the same steps that the user might.

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

# ========================================
# locate by CSS_SELECTOR are really useful
# ========================================

# url = "https://www.python.org/"
#
# document_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# link = document_link.text

# ========================================
# locate by XPath is best if all else fail
# ========================================

# Let's say you want to get the link for Submit Website Bug

# url = "https://www.python.org/"

# You can inspect element, right click, copy XPath
# https://www.w3schools.com/xml/xpath_intro.asp

# submit_bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit_bug_link)


# .quit will close out the whole driver, .close will close a tab
driver.quit()
