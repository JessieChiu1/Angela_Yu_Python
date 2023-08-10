import requests
from dotenv import load_dotenv
import os

# ===============
# Fetch from .env
# ===============

load_dotenv()

user_token = os.environ.get("USER_TOKEN")
username = os.environ.get("PIXELA_USERNAME")


# ===========
# Create User
# ===========

# create user: https://docs.pixe.la/entry/post-user

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": user_token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

# ============
# Create Graph
# ============

# create graph: https://docs.pixe.la/entry/post-graph

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_parameters = {
    "id": "graph1",
    "name": "Coding Habit Graph",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": user_token
}

# response = requests.post(url=graph_endpoint, headers=headers, json=graph_parameters)
# print(response.text)