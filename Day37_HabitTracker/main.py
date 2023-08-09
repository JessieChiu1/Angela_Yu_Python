import requests
from dotenv import load_dotenv
import os

# ===============
# Fetch from .env
# ===============

load_dotenv()

user_token = os.environ.get("USER_TOKEN")
username = os.environ.get("USERNAME")


# ===========
# Create User
# ===========

# create user: https://docs.pixe.la/entry/post-user
user_parameters = {
    "token": user_token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url="https://pixe.la/v1/users", json=user_parameters)
print(response.text)