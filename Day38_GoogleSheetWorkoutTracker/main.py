import requests
from dotenv import load_dotenv
import os

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

# ===========
# prompt User
# ===========

query = input("Tell me which exercises you did: ")

# ======================
# Post exercise endpoint
# ======================

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
print(response.text)