import requests
from dotenv import load_dotenv
import os
import datetime as dt

# ===========
# load dotenv
# ===========

load_dotenv()

app_id = os.environ.get("APP_ID")
api_key = os.environ.get("API_KEY")
gender = os.environ.get("GENDER")
weight_kg = os.environ.get("WEIGHT_KG")
height_cm = os.environ.get("HEIGHT_CM")
age = os.environ.get("AGE")
auth_token = os.environ.get("AUTH_TOKEN")

# ===========
# prompt User
# ===========

query = input("Tell me which exercises you did: ")

# ======================
# Post exercise endpoint
# ======================

# https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#

headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
}

post_exercise_parameters = {
    "query": query,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age,
}

post_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=post_exercise_endpoint, json=post_exercise_parameters, headers=headers)
result = response.json()
data = result["exercises"]

# ==========================================
# Making requests to Google Sheet via Sheety
# ==========================================

# https://sheety.co/docs/requests
# https://sheety.co/docs/authentication.html

sheety_endpoint = "https://api.sheety.co/4552723523d54bde250ecd98364af758/myWorkoutsTracker/workouts"

today = dt.datetime.today().strftime("%m/%d/%Y")
time = dt.datetime.now().time().strftime('%H:%M:%S')

for exercise in data:
    post_workout_data = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["user_input"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    response = requests.post(url=sheety_endpoint, json=post_workout_data, headers=headers)
    print(response.text)


