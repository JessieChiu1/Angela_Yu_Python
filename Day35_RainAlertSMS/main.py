import requests
from dotenv import load_dotenv
import os

# ===============
# fetch from .env
# ===============
load_dotenv()

lat = os.environ.get("LAT")
lon = os.environ.get("LON")
api_ley = os.environ.get("API_KEY")

# ======================
# fetching data from API
# ======================

api_parameters = {
    "lat": lat,
    "lon": lon,
    "appid": api_ley
}

url = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(url=url, params=api_parameters)
response.raise_for_status()
# only need the list of forcast and only the first 4 since they are 3 hours interval
data = response.json()["list"][:4]
# list comprehension to just grab the description of the weather conditions
weather_data = [forcast["weather"][0]["main"] for forcast in data]


# ==============================
# check if it will rain function
# ==============================

def check_rain(weather_data):
    for forcast in weather_data:
        if "rain" in forcast.lower():
            return True
    return False

