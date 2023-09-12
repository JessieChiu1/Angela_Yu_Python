from bs4 import BeautifulSoup

# grab content so we can scrap it
# UnicodeDecodeError - issue decoding - default encoding is not compatible, manually set the encoding
with open("website.html", encoding="utf-8") as file:
    content = file.read()

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# BeautifulSoup can read XML and HTML
# import lxml for XML

soup = BeautifulSoup(content, "html.parser")


# printing basic information
# ==========================


# the soup contain the html with all the html tag
# ===============================================
# print(soup)


# print the HTML but indented
# ===========================
# print(soup.prettify())


# print the title with the html tag
# =================================
# print(soup.title)


# print the title STRING
# ======================
# print(soup.title.string)


# this will ONLY get the FIRST tag
# ================================
# print(soup.p)

# ============
# finding info
# ============

# .find_all() this will find ALL tag and it will be a LIST if there is more than 1
# ================================================================================

# all_a_tags = soup.find_all(name="a")
# print(all_a_tags)

# You can loop through the list to get some info, or even to get specific elements of the tag
# for tag in all_a_tags:
#     print(tag.getText())
#     print(tag.get("href"))


# .find() Finding SPECIFIC element with class/id
# ==============================================

# name will be the TAG
# heading = soup.find(name="h1", id="name")
# print(heading)

# since class is a reserved keyword, we use class_ instead
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.name)
# print(section_heading.get_text())
# print(section_heading.get("class"))


# .select_one()Drilling down to the tag element
# ==============================================

# this is similar to CSS selector with parent/child relationship

# find a tag that is wrapped in p tag
# company_url = soup.select_one(selector="p a")
# print(company_url)

# can be specific selector like class/id
# name = soup.select_one(selector="#name")
# print(name)

# if there is more than 1 class named "heading", it will be a list
# heading = soup.select_one(selector=".heading")
# print(heading)