from bs4 import BeautifulSoup

# with open(r"45_WebScrapingwBeautifulSoup\website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title.string)

# # print(soup.prettify())

# all_h3_tags =  soup.find_all(name="h3")
# # print(all_h3_tags)

# for tag in all_h3_tags:
#     # print(tag.getText())
#     # tag.get("href")
#     pass

# heading = soup.find(name="h2", class_="classist")
# # print(heading.getText())
# # print(heading.get("class"))

# date = soup.select(selector=".classist")
# print(date)

import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
article1 = soup.find(class_="titleline")
print(article1.get_text())