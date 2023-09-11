import requests
from dotenv import load_dotenv
import os

# ===========
# load_dotenv
# ===========

load_dotenv()
TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
Sheety_Bearer = os.environ.get("SHEETY_BEARER")

# ===================
# Sheety Bearer Token
# ===================

sheety_headers = {
    "Authorization": f"Bearer {Sheety_Bearer}"
}

# ===============================================
# Fetching the name of all the cities with Sheety
# ===============================================

# fetch all the city from sheety into a list
sheety_get_endpoint = "https://api.sheety.co/4552723523d54bde250ecd98364af758/flightDeals/prices"
response = requests.get(url=sheety_get_endpoint, headers=sheety_headers)
city_data = response.json()["prices"]

# list comprehension to get only the city name
# city_list = [row["city"] for row in city_data]

# =================================================
# adding the IATA code for all the city with Sheety
# =================================================

for i in range(len(city_data)):
    # end with /[Object ID]
    sheety_edit_endpoint = "https://api.sheety.co/4552723523d54bde250ecd98364af758/flightDeals/prices"

    # Tequila request info
    IATA_query_endpoint = "https://api.tequila.kiwi.com/locations/query"

    tequila_location_query = {
        "term": city_data[i]["city"],
        "location_types": "city"
    }

    headers = {
        "apikey": TEQUILA_API_KEY,
    }

    # send request to fetch iata code information form Tequila
    response = requests.get(url=IATA_query_endpoint, headers=headers, params=tequila_location_query)
    tequila_output = response.json()
    city_iata_code = tequila_output["locations"][0]["code"]

    # sending requests to add the iata code to Sheety
    rowid = city_data[i]["id"]
    edited_data = {
        "price": {
            "city": city_data[i]["city"],
            "iataCode": city_iata_code,
            "lowestPrice": city_data[i]["lowestPrice"],
            "id": rowid,
        }
    }
    response = requests.put(url=f"{sheety_edit_endpoint}/{rowid}", json=edited_data, headers=sheety_headers)
    print(response.text)


