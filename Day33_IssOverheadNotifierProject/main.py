import math
import requests
import datetime as dt
import os
from dotenv import load_dotenv
import smtplib
import time

# If the ISS is close to my current location
# and it is currently dark
# then send me an email to tell me to look up
# BONUS: run the code every 60 seconds.

MY_LAT = 40.628826
MY_LNG = -73.961694
margin = 5
smtp_email = "smtp.gmail.com"

# status code
# 100s Hold on
# 200s Success
# 300s You don't have permission
# 400s You made some mistake
# 500s server not available right now

# ======================
# Sunset and Sunrise API
# ======================
# This api requires you to input some parameter (your location

sun_parameter = {
    "lat": MY_LAT,
    "LNG": MY_LNG,
    "formatted": 0,
}

# fetching data
response = requests.get(url="https://api.sunrise-sunset.org/json", params=sun_parameter)


# helper function that convert the sun_api sunrise and sunset time to the same format as datetime module
def get_hour(time):
    output = time.split('T')[1]
    output = output.split(':')[0]
    return output


# if it is not a success, it will raise the exception
response.raise_for_status()

sun_data = response.json()
sunrise = get_hour(sun_data["results"]["sunrise"])
sunset = get_hour(sun_data["results"]["sunset"])
time_now = dt.datetime.now().hour

# ============
# ISS location
# ============

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# if it is not a success, it will raise the exception
response.raise_for_status()

iss_data = response.json()

iss_lat = float(iss_data["iss_position"]["latitude"])
iss_lng = float(iss_data["iss_position"]["longitude"])


# =================
# Conditional checks
# ==================
# calculating distance
def find_distance(my_lat, my_lng, iss_lat, iss_lng):
    a = abs(my_lat - iss_lat)
    b = abs(my_lng - iss_lng)
    c = math.sqrt((a ** 2 + b ** 2))
    return c


distance = find_distance(my_lat=MY_LAT, my_lng=MY_LNG, iss_lat=iss_lat, iss_lng=iss_lng)


# checking if it is dark
def is_dark(sunrise, sunset, time_now):
    sunrise_int = int(sunrise)
    sunset_int = int(sunset)
    if sunrise_int < time_now < sunset_int:
        return True
    return False


sky_is_dark = is_dark(sunrise=sunrise, sunset=sunset, time_now=time_now)

# =============
# Sending email
# =============
# loading the .env to local environment
load_dotenv()

email_address = os.environ.get("EMAIL_ADDRESS")
password = os.environ.get("PASSWORD")

while True:
    time.sleep(60)
    if distance < margin and sky_is_dark:
        with smtplib.SMTP(smtp_email) as connection:
            connection.starttls()
            connection.login(user=email_address, password=password)
            connection.sendmail(
                from_addr=email_address,
                to_addrs=email_address,
                msg="Subject:ISS Overhead!\n\nThe international Space Station is overhead now! Look up"
            )
    else:
        print("distance away from ISS:", distance)