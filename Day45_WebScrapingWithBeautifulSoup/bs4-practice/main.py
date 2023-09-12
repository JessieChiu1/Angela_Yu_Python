from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")

# this get the whole HTML file
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

# title and links
title_lines = soup.find_all(name="span", class_="titleline")

# upvote points
upvote_lines = soup.find_all(name="span", class_="score")

# variable to store result
articles = []


for i in range(0, len(title_lines) - 1):
    anchor_title_tag = title_lines[i].find(name="a")

    article_title = anchor_title_tag.text
    article_link = anchor_title_tag.get("href")

    upvote_span_tag = upvote_lines[i]
    upvote_text = upvote_span_tag.text
    upvote = int(upvote_text.split()[0])

    # print(f"{article_title} at {article_link} with {upvote} points")

    # create a dictionary item so we can add it to our list of articles
    article_dic = {
        "title": article_title,
        "link": article_link,
        "upvote": upvote
    }
    articles.append(article_dic)

# print(articles)

# https://www.w3schools.com/python/python_lambda.asp
# https://docs.python.org/3/library/functions.html#max
# max function's "key" parameter is to specify what we are comparing
max_upvote_item = max(articles, key=lambda article: article['upvote'])
print(max_upvote_item)

