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

for i in range(0, len(title_lines) - 1):
    anchor_title_tag = title_lines[i].find(name="a")

    article_title = anchor_title_tag.text
    article_link = anchor_title_tag.get("href")

    upvote_span_tag = upvote_lines[i]
    upvote_text = upvote_span_tag.text
    upvote = upvote_text.split()[0]

    print(f"{article_title} at {article_link} with {upvote} points")

