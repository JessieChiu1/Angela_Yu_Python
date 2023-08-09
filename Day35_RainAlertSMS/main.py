import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client
# You can use pythonanawhere to host and schedule a time for your python code to run, I will not do that because twillo will cost me money

# ===============
# fetch from .env
# ===============
load_dotenv()

lat = os.environ.get("LAT")
lon = os.environ.get("LON")
api_key = os.environ.get("API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
my_number = os.environ.get("MY_NUMBER")
twilio_number = os.environ.get("TWILIO_NUMBER")

# ======================
# fetching data from API
# ======================

api_parameters = {
    "lat": lat,
    "lon": lon,
    "appid": api_key
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


if check_rain(weather_data):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember your umbrella!",
        from_=f"+{twilio_number}",
        to=f"+{my_number}"
    )
    print(message.status)