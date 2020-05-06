import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#From the last file, where the buffy information was I will use the data set to plot scores.
path = pd.read_csv("/Rating_Title.csv")

dataFrame = pd.DataFrame(path, columns=["Title", "Rating"])
#remove out of /10 and ensuring the rating is numerical
dataFrame = dataFrame.replace("/10", "", regex = True)
dataFrame['Rating'] = pd.to_numeric(dataFrame['Rating'], errors='ignore')
#Plot a bar chart
plt.figure(figsize=(150,10))
plt.bar(dataFrame.Title, dataFrame.Rating, color = '#6a0dad')
plt.yticks([0,1,2,3,4,5,6,7,8,9,10])
plt.xticks(dataFrame.Title, rotation = 70)
plt.title("Season One of Buffy The Vampire Slayer", fontsize = 20, fontweight = "bold")
plt.ylabel("Rating Value Out of Ten")
plt.xlabel ("Episode Rating")
plt.show()

#Other Analysis
#See the middle number of the ratings
Range = (dataFrame["Rating"].max() - dataFrame['Rating'].min())
Mean = dataFrame["Rating"].mean()
Median = dataFrame['Rating'].median()
Mode = dataFrame['Rating'].mode()
standardDeviation = dataFrame['Rating'].std()
print("The median value of the rating was,",(Median),".")
print("The standard deviation was low, as it had a ",(standardDeviation), "standard deviation.")
print("There was only a range of,", (Range))
print("The average rating of season one was",(Mean), ".")
print("The most common rating was,",(Mode))
