import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup


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

product_info = soup.find(name="div", id="centerCol")
div_price_container = product_info.find(name="div", id="corePrice_desktop")

price_container = div_price_container.find(name="span", class_="apexPriceToPay")
price = float(price_container.text.split("$")[1])
print(price)