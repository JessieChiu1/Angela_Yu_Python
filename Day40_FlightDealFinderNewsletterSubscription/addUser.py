import requests
from dotenv import load_dotenv
import os

# ===========
# load_dotenv
# ===========

load_dotenv()
Sheety_Bearer = os.environ.get("SHEETY_BEARER")

# ===================
# Sheety Bearer Token
# ===================

sheety_headers = {
    "Authorization": f"Bearer {Sheety_Bearer}"
}

sheety_user_post_endpoint = "https://api.sheety.co/4552723523d54bde250ecd98364af758/flightDeals/users"

# =======================
# Prompting for user info
# =======================

first_name = input("What is your first name?")
last_name = input("What is your last name?")
email = input("What is my email?")

new_user = {
    "users": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
    }
}


response = requests.post(url=sheety_user_post_endpoint, headers=sheety_headers, json=new_user)
response.raise_for_status()