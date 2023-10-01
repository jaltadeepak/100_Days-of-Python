from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

contentlist = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")

movielist = []
for tag in contentlist:
    movielist.append(tag.getText())

# did not need to sort, could just move backwards
# rank = []
# name = []
# for movie in movielist:
#     name.append(movie.split(")")[1].strip())
#     rank.append(int(movie.split(")")[0]))
# print(name)
# print(rank)

with open(r"45_WebScrapingwBeautifulSoup\scrapemovielist\movielist.txt", "w") as file:
    for movie in movielist[::-1]:
        file.write(movie)
        file.write("\n")
