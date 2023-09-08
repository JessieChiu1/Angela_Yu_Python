import requests
from dotenv import load_dotenv
import os

# ===========
# load_dotenv
# ===========

load_dotenv()
Tequila_API = os.environ.get("TEQUILA_API")
Sheety_Bearer = os.environ.get("SHEETY_BEARER")

# ===============================================
# Fetching the name of all the cities with Sheety
# ===============================================

# fetch all the city from sheety into a list
sheety_get_endpoint = "https://api.sheety.co/4552723523d54bde250ecd98364af758/flightDeals/prices"
response = requests.get(url=sheety_get_endpoint)
response_list = response.json()["prices"]

# list comprehension to get only the city name
city_list = [row["city"] for row in response_list]

