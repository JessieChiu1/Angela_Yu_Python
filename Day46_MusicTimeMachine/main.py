import requests
from bs4 import BeautifulSoup

date = input("Which date do you want to create the spotify playlists from? Please enter date in YYYY-MM-DD format\n")

url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url=url)

html = response.text

soup = BeautifulSoup(html, "html.parser")

print(soup)