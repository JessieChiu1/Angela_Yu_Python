import requests
from dotenv import load_dotenv
import os
import datetime as dt

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
graphID = "graph1"

graph_parameters = {
    "id": graphID,
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

# ==============
# adding a pixel
# ==============

# POST pixel request: https://docs.pixe.la/entry/post-pixel

post_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graphID}"

today = dt.datetime.today().strftime("%Y%m%d")

post_pixel_parameters = {
    "date": today,
    "quantity": "5",
}

# response = requests.post(url=post_pixel_endpoint, headers=headers, json=post_pixel_parameters)
# print(response.text)

# =============================
# PUT request: updating a pixel
# =============================

# PUT pixel request: https://docs.pixe.la/entry/put-pixel

put_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graphID}/{today}"

put_pixel_parameters = {
    "quantity": "6",
}

response = requests.put(url=put_pixel_endpoint, headers=headers, json=put_pixel_parameters)
print(response.text)