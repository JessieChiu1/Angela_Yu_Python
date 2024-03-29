import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import smtplib

# ===============
# fetch from .env
# ===============
load_dotenv()

btc_api_key = os.environ.get("BTC_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")
email_address = os.environ.get("EMAIL_ADDRESS")
password = os.environ.get("PASSWORD")

# ===============
# datetime module
# ===============

now = datetime.now()
today = datetime.today().date()
yesterday = today - timedelta(1)

# ==========
# fetch data
# ==========

btc_api_parameters = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": "BTC",
    "market": "USD",
    "apikey": btc_api_key,
}


def fetch_btc_data():
    response = requests.get(url="https://www.alphavantage.co/query", params=btc_api_parameters)
    response.raise_for_status()
    raw_data = response.json()
    return raw_data['Time Series (Digital Currency Daily)']


def today_btc_change(today_closing, yesterday_closing):
    price_change = today_closing - yesterday_closing
    percentage_change = price_change/yesterday_closing * 100
    rounded_value = round(percentage_change,2)
    return rounded_value


# ==========
# fetch news
# ==========

news_api_parameters = {
    "q": "Bitcoin",
    "from": f"{yesterday}",
    "to": f"{today}",
    "sortBy": "popularity",
    "apiKey": news_api_key,
}


def fetch_news():
    response = requests.get(url="https://newsapi.org/v2/everything", params=news_api_parameters)
    response.raise_for_status()
    data = response.json()
    return data["articles"]


# ==========
# send email
# ==========

if now.hour > 18:
    # btc data
    BTC_data = fetch_btc_data()
    today_closing = float(BTC_data[f"{today}"]["4a. close (USD)"])
    yesterday_closing = float(BTC_data[f"{yesterday}"]["4a. close (USD)"])
    # news data
    news_data = fetch_news()
    # calculate price change
    price_change = today_btc_change(today_closing, yesterday_closing)
    # send email with smtplib
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_address, password=password)

        # Create the email message with proper UTF-8 encoding
        subject = "Bitcoin Daily Alert"
        message_body = f"""
        Today's Price change: {price_change}%
        Top 3 News:
        {news_data[0]['title']} by {news_data[0]['author']}
        {news_data[0]['url']}
        {news_data[1]['title']} by {news_data[1]['author']}
        {news_data[1]['url']}
        {news_data[2]['title']} by {news_data[2]['author']}
        {news_data[2]['url']}
        """
        msg = f"Subject: {subject}\n\n{message_body}"
        msg = msg.encode('utf-8')

        connection.sendmail(
            from_addr=email_address,
            to_addrs=email_address,
            msg=msg
        )

