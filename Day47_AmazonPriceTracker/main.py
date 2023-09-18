import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import os
import smtplib

# =============
# load_env
# =============
load_dotenv()

email_address = os.environ.get("EMAIL_ADDRESS")
password = os.environ.get("PASSWORD")

# ==================
# Fetching html page
# ==================

url = "https://www.amazon.com/Hartz-Delectables-Squeeze-Interactive-Lickable/dp/B0BGT84G2R/ref=sr_1_1_sspa?crid=1T7CRSWCAAKPR&keywords=delectables%2Blickable%2Bcat%2Btreats&qid=1694741755&sprefix=delecta%2Caps%2C215&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

headers = {
    "Accept-Language": "en-US,en;q=0.9,zh-HK;q=0.8,zh;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
}

response = requests.get(url=url, headers=headers)

html = response.text

soup = BeautifulSoup(html, "html.parser")

# just open the index.html in browser to see if it is the page you want
# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(soup.prettify())

# ================================
# Web scraping with beautiful soup
# ================================

# the amazon html page will change depending on if the item is prime eligible or not

# example of web scraping prime eligible item is in the "try" block
# url = "https://www.amazon.com/Hartz-Delectables-Squeeze-Interactive-Lickable/dp/B0BGT84G2R/ref=sr_1_1_sspa?crid=1T7CRSWCAAKPR&keywords=delectables%2Blickable%2Bcat%2Btreats&qid=1694741755&sprefix=delecta%2Caps%2C215&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
try:
    product_info = soup.find(name="div", id="centerCol")
    div_price_container = product_info.find(name="div", id="corePrice_desktop")

    price_container = div_price_container.find(name="span", class_="apexPriceToPay")
    price = float(price_container.text.split("$")[1])
    print(price)
# example of web scraping prime ineligible item
# url = "https://www.amazon.com/dp/B0788884DF?ref=nb_sb_ss_w_as-reorder-t1_k4_1_11&amp=&crid=3GWM5HP0EPN08&sprefix=dermashield&th=1"
except AttributeError:
    price_whole = soup.find(name="span", class_="a-price-whole")
    price_fraction = soup.find(name="span", class_="a-price-fraction")
    price = float(f"{price_whole.text}{price_fraction.text}")
    print(price)


product_name = soup.find(name="span", id="productTitle").text.strip()

print(product_name)

# ===================================================
# Sending email when price drop below a certain price
# ===================================================

target_price = 31

if price < target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_address, password=password)
        connection.sendmail(
            from_addr=email_address,
            to_addrs=email_address,
            msg=f"Subject: Amazon Price Alert \n\n {product_name} currently below ${target_price}"
        )