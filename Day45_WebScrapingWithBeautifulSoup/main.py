import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

html = response.text

soup = BeautifulSoup(html, "html.parser")

movie_list_html = soup.find(name="div", class_="gallery")
movie_sections = movie_list_html.find_all(name="section", class_="gallery__content-item--gallery")
# print(len(movie_sections))

# list to store all the movie
movie_list = []

for i in range(0, len(movie_sections)):
    title_div_tag = movie_sections[i].find(name="h3")
    title = title_div_tag.text
    movie_list.append(title)

movie_list.reverse()

print(movie_list)

# if you get UnicodeEncodeError, add encoding="utf-8"
with open("top100MovieList.txt", mode="w", encoding="utf-8") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")