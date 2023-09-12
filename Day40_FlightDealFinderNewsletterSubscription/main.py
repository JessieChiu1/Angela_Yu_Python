# This is an extension on the Day39 projects, I wanted to refactor and make it more readable

import requests
from dotenv import load_dotenv
import os
import datetime as dt
import smtplib

# ===========
# load_dotenv
# ===========

load_dotenv()
TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
sheety_bearer = os.environ.get("SHEETY_BEARER")
email_address = os.environ.get("EMAIL_ADDRESS")
email_password = os.environ.get("EMAIL_PASSWORD")

# ===================
# Sheety Bearer Token
# ===================

sheety_headers = {
    "Authorization": f"Bearer {sheety_bearer}"
}

# ===============================================
# Fetching the name of all the cities with Sheety
# ===============================================

sheety_get_endpoint = "https://api.sheety.co/4552723523d54bde250ecd98364af758/flightDeals/prices"
response = requests.get(url=sheety_get_endpoint, headers=sheety_headers)
response.raise_for_status()
city_data = response.json()["prices"]

for i in range(len(city_data)):
    # search for flights and sort by prices
    # =====================================
    tequila_search_endpoint = "https://tequila-api.kiwi.com/v2/search"

    header = {
        "apikey": TEQUILA_API_KEY
    }

    query = {
        "fly_from": "NYC",
        "fly_to": city_data[i]["iataCode"],
        "date_from": dt.datetime.today().strftime("%d/%m/%Y"),
        "date_to": (dt.datetime.today() + dt.timedelta(days=180)).strftime("%d/%m/%Y"),
        "curr": "USD",
        "sort": "price"
    }

    response = requests.get(url=tequila_search_endpoint, headers=header, params=query)
    response.raise_for_status()
    search_result = response.json()

    cheapest_flight = search_result["data"][0]

    # get the lowest price of the current city
    sheety_price = city_data[i]["lowestPrice"]

    # update sheety price and send email
    # ==================================
    if cheapest_flight["price"] < sheety_price:
        # update sheety price
        # ===================
        sheety_edit_endpoint = "https://api.sheety.co/4552723523d54bde250ecd98364af758/flightDeals/prices"

        rowid = city_data[i]["id"]
        edited_data = {
            "price": {
                "city": city_data[i]["city"],
                "iataCode": city_data[i]["iataCode"],
                "lowestPrice": cheapest_flight["price"],
                "id": rowid,
            }
        }

        response = requests.put(url=f"{sheety_edit_endpoint}/{rowid}", json=edited_data, headers=sheety_headers)
        response.raise_for_status()
        print(response.text)

        # sending an email alert
        # ======================

        # fetch all user in google sheet
        user_sheety_get_endpoint = "https://api.sheety.co/4552723523d54bde250ecd98364af758/flightDeals/users"
        response = requests.get(url=user_sheety_get_endpoint, headers=sheety_headers)
        user_data = response.json()

        # send email to everyone to alert price update
        for user in user_data["users"]:
            smtp_email = "smtp.gmail.com"
            with smtplib.SMTP(smtp_email) as connection:
                connection.starttls()
                connection.login(user=email_address, password=email_password)
                connection.sendmail(
                    from_addr=email_address,
                    to_addrs=user.email,
                    msg=f"Subject: {search_result.flyFrom} price alert\n\nOnly ${search_result.price} to fly from {search_result.cityFrom}-{search_result.cityCodeFrom} at {search_result.flyFrom} airport to {search_result.cityTo}-{search_result.cityCodeTo} at {search_result.flyTo}, from {search_result.local_arrival} to {search_result.local_departure}",
                )