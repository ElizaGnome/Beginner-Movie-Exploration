import requests
import bs4 as bs


#Create a place to store our collected information:
imdbRating = []
title = []

#what is the general opinion of buffy season one.
urlPath = "https://www.imdb.com/list/ls054779807/"
seasonOne = requests.get (urlPath)

#print to see if i can access the data.
print(seasonOne)
data = bs.BeautifulSoup(seasonOne.content, "html.parser")

#we want the rating and name of episode. Start with rating, as it appears to be easiest location when inspecting the page.

for line in data.findAll("div",  {"class" : "list-description"}):
    rating = line.text
    print(rating)
    imdbRating.append(rating)


for line in data.findAll("div", {"class": "lister-item-content"}):
     item = line.findAll("a", {"href": True})[1]
     text = item.text
     title.append(text)


titleScore = []
# I realize it gave you an overall score for the series, so i just got rid of that by stating the range.
#I looped over the values to place them into easy to write to file list.

for x, y in zip(title, imdbRating[2:13]):
    text = (x, y)
    titleScore.append(text)
#write to csv

with open("mycsv.csv", "W", newline ="") as f:
    writer = csv.writer(f, delimiter =",")
    writer.writerows(titleScore)

