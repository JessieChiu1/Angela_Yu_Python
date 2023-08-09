import requests
from dotenv import load_dotenv
import os
import datetime as dt

# ===============
# fetch from .env
# ===============
load_dotenv()

btc_api_key = os.environ.get("BTC_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")

# ==========
# fetch data
# ==========

api_parameters= {
    "function": "DIGITAL_CURRENCY_WEEKLY",
    "symbol": "BTC",
    "market": "USD",
    "apikey": btc_api_key,
}

response = requests.get(url="https://www.alphavantage.co/query", params=api_parameters)
response.raise_for_status()
raw_data = response.json()
BTC_data = raw_data['Time Series (Digital Currency Weekly)']

# ==========
# fetch news
# ==========


