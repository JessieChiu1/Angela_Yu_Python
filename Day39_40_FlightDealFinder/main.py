import requests
from dotenv import load_dotenv
import os

# ===========
# load_dotenv
# ===========

load_dotenv()
Tequila_API = os.environ.get("TEQUILA_API")
Sheety_Bearer = os.environ.get("SHEETY_BEARER")

# ===================
# Sheety Bearer Token
# ===================

headers = {
    "Authorization": f"Bearer {Sheety_Bearer}"
}

# ===============================================
# Fetching the name of all the cities with Sheety
# ===============================================

# fetch all the city from sheety into a list
sheety_get_endpoint = "https://api.sheety.co/4552723523d54bde250ecd98364af758/flightDeals/prices"
response = requests.get(url=sheety_get_endpoint, headers=headers)
city_data = response.json()["prices"]

# list comprehension to get only the city name
city_list = [row["city"] for row in city_data]

# =================================================
# adding the IATA code for all the city with Sheety
# =================================================

# end with /[Object ID]
sheety_edit_endpoint = "https://api.sheety.co/4552723523d54bde250ecd98364af758/flightDeals/prices"

# Tequila endpoint
IATA_query_endpoint = "https://api.tequila.kiwi.com/locations/query"

for i in range(len(city_data)):
    row_data = city_data[i]
    print(row_data)
    rowid = city_data[i]["id"]
    edited_data = {
        "price": {
            "city": city_data[i]["city"],
            "iataCode": "TESTING",
            "lowestPrice": city_data[i]["lowestPrice"],
            "id": rowid,
        }
    }
    response = requests.put(url=f"{sheety_edit_endpoint}/{rowid}", json=edited_data, headers=headers)
    print(response.text)