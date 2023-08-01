import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# This will return the status code
print(response)

# status code
# 100s Hold on
# 200s Success
# 300s You don't have permission
# 400s You made some mistake
# 500s server not available right now

# if it is not a success, it will raise the exception
response.raise_for_status()

# This is how you tap into the actual data
data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)