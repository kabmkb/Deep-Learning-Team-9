import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from contextlib import redirect_stdout

data = pd.read_csv('country_vaccinations.csv')
print(data.head())

# check for null values
nulls = data.isnull().sum()
nulls[nulls > 0]
print(nulls[nulls > 0])

#printing info
print(data.info)

#printing shape
print(data.shape)

#total count of unique values of top 20 elements in descending order
print(data['country'].value_counts().head(20))


#"England" "Wales" , "Scotland" , "Northern Ireland" all country are the part of the United kingdom so replace these countries with United_Kingdom.
rename_continent1 = ["China" , "Israel" , "Qatar" , "Bahrain"]

for i in rename_continent1:

    data["country"] = data["country"].str.replace(i ,"Asia")

rename_continent2=["Canada", "United States", "Mexico", "Costa Rica", "Cayman Islands"]

for a in rename_continent2:
    data["country"]=data["country"].str.replace(a, "North America")

rename_continent3=["United Kingdom", "Scotland", "England", "Wales", "Lithuania", "Portugal", "Italy", "Czechia"]

for b in rename_continent3:
    data["country"]=data["country"].str.replace(b,"Europe")

rename_continent4=["Northern Ireland"]

for c in rename_continent4:
    data["country"]=data["country"].str.replace(c,"Ocenia")

rename_continent5=["Russia"]
for d in rename_continent5:
    data["country"]=data["country"].str.replace(d,"Eurasia")

print(data['country'].value_counts().head(5))
# plot between total no. of people vaccinated and no. of people vaccinated per country
plt.figure(figsize=(8, 7))
sorted_data = data.groupby("country").people_fully_vaccinated.agg("max").sort_values(ascending = False)
sorted_data[sorted_data> 2000000].plot.bar(color = "blue")
plt.ylabel("Total no of people fully vaccinated ")
plt.title("Number of fully vaccinated people per country")
sns.set_style("whitegrid")
plt.show()

#daily Vaccination progress of Continentwise
data2 = data.pivot_table(index = "date", columns = "country", values = "daily_vaccinations")
data2[["Asia", "North America", "Eurasia", "Europe", "Ocenia"]].replace(0, np.nan).fillna(method = "bfill", axis = 0).plot(xlabel= "Date", ylabel = "No of people vaccinated daily", title = "Progress of daily vaccinations continentwise", figsize = (10,7))
plt.legend()
plt.style.use("classic")
plt.show()


#Which vaccines are used by which country
print(pd.DataFrame(data.groupby("country")[["vaccines"]].max()))
#plot graph

#printing result of which vaccines are used by which country into a text document
with open('file.txt', 'w') as f:
    with redirect_stdout(f):
        print(pd.DataFrame(data.groupby("country")[["vaccines"]].max()))
f.close()


plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (20, 20)
#read original dataset
train = pd.read_csv('us_state_vaccinations (1).csv')
#read dataset with only most recent numbers for each state
train_bystate = pd.read_csv('us_state_vaccinations_to_date.csv')
#read dataset with all states summed up (data for whole of US)
train_allstates = pd.read_csv('us_state_vaccinations_all_states.csv')

#Print description of data
print("Most recent data for each state: ")
print("total distributed: ")
print(train_bystate.total_distributed.describe())
print("total vaccinations per 100: ")
print(train_bystate.total_vaccinations_per_hundred.describe())
print(" people fully vaccinated per 100: ")
print(train_bystate.people_fully_vaccinated_per_hundred.describe())

print("Daily vaccination information: ")
print("daily vaccinations: ")
print(train.daily_vaccinations.describe())

#format x-axis label for better readability
plt.xticks(rotation=90)

#visualize percentage of people vaccinated per location
plt.scatter(train_bystate.location, train_bystate.people_vaccinated_per_hundred)
plt.xlabel('Location')
plt.ylabel('Percentage People Vaccinated')
plt.show()

#visualize daily vaccinations by state as of 3/24/21
plt.scatter(train_bystate.location, train_bystate.daily_vaccinations)
plt.xlabel('Location')
plt.ylabel('Daily Vaccinations')
plt.show()

#visualize daily vaccinations by date up til 3/24/21
plt.scatter(train_allstates.date, train_allstates.daily_vaccinations)
plt.xlabel('Date')
plt.ylabel('Daily Vaccinations')
plt.show()

#visualize percent of people vaccinated by date up til 3/24/21
plt.scatter(train_allstates.date, train_allstates.people_fully_vaccinated_per_hundred)
plt.xlabel('Date')
plt.ylabel('Percentage Fully Vaccinated')
plt.show()

#visualize distributed vaccines vs. total vaccinations for US
plt.scatter(train_allstates.total_distributed, train_allstates.total_vaccinations)
plt.xlabel('Distributed Vaccines')
plt.ylabel('Total Vaccinations')
plt.show()

