from selenium import webdriver
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
    store_container = driver.find_elements(By.CSS_SELECTOR, value="#product unlocked enabled")
    store_container.reverse()
    for store in store_container:
        store.click()


def buy_upgrade():
    upgrade_container = driver.find_elements(By.CLASS_NAME, value="crate upgrade")
    for upgrade in upgrade_container:
        upgrade.click()


def save_game():
    # click option and save game button
    option_button = driver.find_element(By.CLASS_NAME, value="subButton")
    option_button.click()
    save_button = driver.find_element(By.XPATH, value='/div/div/div[4]/a[1]')
    save_button.click()

    # wait until the text area pop up
    wait.until(EC.element_to_be_clickable((By.ID, "textareaPrompt")))
    # copy and save the code to a txt
    save_code_tag = driver.find_element((By.ID, "textareaPrompt"))
    save_code = save_code_tag.text
    with open("save_code.txt", mode="w") as file:
        file.write(save_code)

    # click option button again to close option
    option_button.click()


def load_game():
    # wrapped everything in a try except clause in case we don't have a save code ready
    try:
        # get our save code
        with open("save_code.txt", mode="r") as file:
            content = file.read()

        # click option and load save
        option_button = driver.find_element(By.CLASS_NAME, value="subButton")
        option_button.click()
        load_save_button = driver.find_element(By.XPATH, value='/div/div/div[4]/a[2]')
        load_save_button.click()

        # wait until text are pop up and paste the save code to the text are
        wait.until(EC.element_to_be_clickable((By.ID, "textareaPrompt")))
        load_code_tag = driver.find_element((By.ID, "textareaPrompt"))
        load_code_tag.send_keys(content)

        # load the save code
        load_button = driver.find_element(By.ID, value="promptOption0")
        load_button.click()

        # close the option menu
        option_button.click()
    except:
        print("error")
