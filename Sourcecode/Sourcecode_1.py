import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from contextlib import redirect_stdout
import matplotlib.dates as mdates

# Global covid-19 vaccination distribution
data = pd.read_csv('country_vaccinations.csv')
print(data['country'].nunique())

#GDP data set
data1=pd.read_csv('GDP_1.csv')

# check for null values
nulls = data.isnull().sum()
nulls[nulls > 0]
print(nulls[nulls > 0])

#printing info
print(data.info)

#printing shape
print(data.shape)

#how many countries are present in the dataset
print(data['country'].nunique())

#total count of unique values of top 20 elements in descending order
print(data['country'].value_counts().head(195))

#"England" "Wales" , "Scotland" , "Northern Ireland" all country are the part of the United kingdom so replace these countries with United_Kingdom.
rename_UNITED_KINGDOM = ["England" , "Wales" , "Scotland" , "Northern Island"]

for i in rename_UNITED_KINGDOM:

    data["country"] = data["country"].str.replace(i ,"UNITED KINGDOM")

# plot between total no. of people vaccinated and no. of people vaccinated per country
plt.figure(figsize=(8, 7))
sorted_data = data.groupby("country").people_fully_vaccinated.agg("max").sort_values(ascending = False)
sorted_data[sorted_data> 2000000].plot.bar(color = "blue")
plt.ylabel("Total no of people fully vaccinated ")
plt.title("Number of fully vaccinated people per country")
sns.set_style("whitegrid")
plt.show()

#Which vaccines are used by which country
print(pd.DataFrame(data.groupby("country")[["vaccines"]].max()))

#printing result of which vaccines are used by which country into a text document
with open('file.txt', 'w') as f:
    with redirect_stdout(f):
        print(pd.DataFrame(data.groupby("country")[["vaccines"]].max()))
f.close()

#Most recent data of all the unique countries from the  dataset
data1_max_year = data1.groupby(['Country'])['Year'].max().reset_index()
print(data1_max_year)

#Join back to iteself to get the latest year available in economic data
data1_max = data1.merge(data1_max_year,how='inner',on=['Country','Year'])

#Join to main dataset
data_data1 = data.merge(data1_max,how='left',left_on='country',right_on='Country')
print(data_data1.head())

#Continent plot
graph = sns.lineplot(data=data_data1.sort_values(by="date"), x="date", y="people_fully_vaccinated_per_hundred",hue='continent')
graph.xaxis.set_major_locator(mdates.DayLocator(interval = 2))
plt.xticks(rotation = 45)

plt.show()

#GDP plot
plt.figure(figsize=(8, 7))
data_data1['gdp_grp'] = pd.qcut(data_data1['gdp'],q=8)
graph = sns.lineplot(data=data_data1.sort_values(by="date"), x="date", y="people_fully_vaccinated_per_hundred",hue='gdp_grp')
graph.xaxis.set_major_locator(mdates.DayLocator(interval = 7))
plt.xticks(rotation = 45)
plt.show()

#Top 10 GDP countries in the world vaccination rates
plt.figure(figsize=(20,5))
graph = sns.lineplot(data=data_data1[data_data1['country'].isin(['United Kingdom','Indonesia','Brazil','Russia','Germany','Japan','India','United States','China'])]
                     .sort_values(by="date"), x="date", y="people_fully_vaccinated_per_hundred",hue='country')
graph.xaxis.set_major_locator(mdates.DayLocator(interval = 5))
plt.xticks(rotation = 45)

plt.show()