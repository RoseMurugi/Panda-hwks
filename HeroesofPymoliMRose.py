
# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
file_to_load = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(file_to_load)

#purchase_data

## Player Count

#Diplaying Total Number of Players
Player_data= purchase_data.drop_duplicates(subset = ["SN"], keep = "first")
player_count= len(purchase_data)
player_count=pd.DataFrame({"Total Players":[576]})
player_count

#Purchase Analysis
#Summary of numeric data
#purchase_data.describe()

#Calculating max Unique items
UniqueItems_max = purchase_data["Item ID"].max()
#print(UniqueItems_max)

#Finding number of unique items
UniqueItems_mean = purchase_data["Price"].mean()
#print("$","{0:.2f}".format(UniqueItems_mean))

#Caluculating purchases
UniqueItems_Purchases = purchase_data["Purchase ID"].max()
#print(UniqueItems_Purchases)

#calulating sum unique items
UniqueItems_sum =purchase_data["Price"].sum()
#print("$","{0:.2f}".format(UniqueItems_sum))


#create summary DataFrame
Summary_table= pd.DataFrame({"UniqueItems_max":[183],
                             "UniqueItems_mean":["$ 3.07"],
                             "UniqueItems_Purchases":[778],
                             "UniqueItems_sum":["$ 1768.65"]
})

#Summary_table.head()                                            

#clean data (Renaming columns)
Summary_table_renamed = Summary_table.rename(columns ={"UniqueItems_max":"Number of Unique Items",
                                                      "UniqueItems_mean":"Average Price",
                                                      "UniqueItems_Purchases":"Number of Purchases",
                                                      "UniqueItems_sum":"Total Revenue"
})
Summary_table_renamed.head()


## Gender Demographics
#purchase_data["Gender"].describe
#calculating the total count of each Gender type
total_gender = purchase_data["Gender"].count()

male=purchase_data["Gender"].value_counts()["Male"]

female=purchase_data["Gender"].value_counts()["Female"]

Other= total_gender-male-female

#calculating the total count of each Gender type
total_gender = purchase_data["Gender"].count()

male=purchase_data["Gender"].value_counts()["Male"]

female=purchase_data["Gender"].value_counts()["Female"]

Other= total_gender-male-female
#print(f"Total:{total_gender}\n Male:{male}\n Female:{female}\n Other/Non-Disclosed:{Other}")

#calculating Percentages of Gender type

male_Percentage=male/total_gender*100
#print("{0:.2f}".format(male_Percentage),"%")

female_Percentage= female/total_gender*100
#print("{0:.2f}".format(female_Percentage),"%")

other_Percentage = Other/total_gender*100
#print("{0:.2f}".format(other_Percentage),"%")

#Summary table for the gender count and percentages
summary_table=pd.DataFrame({"Percentage of Players":[84.03,14.06,1.91],
                            "Total Count":[484,81,11],
                            "Gender":["Male","Female","Other/Non-Disclosed"]
})
summary_table.set_index("Gender",inplace=True)
summary_table


#Purchase Analysis(Gender)

#calculating total purchase price per gender

Total=purchase_data["Price"].groupby(purchase_data["Gender"]).sum()
#Total

#calculating avg price per gender
#avg = purchase_data["Price"].groupby(purchase_data["Gender"]).mean()
#avg

#average Purchase total per person
Male=Total/male
#Male
Female=Total/female
#Female
Other = Total/Other
#Other

#Summary Table Purchase Analysis(Gender)
Purchase_Analysis = pd.DataFrame({"Gender":["Female","Male","Other/Non-Disclosed"],
                                "Purchase Count":[81,484,11],
                                "Average Purchase Price":["$3.17","$3.05","$3.41"],
                                "Total Purchase Value":[256.43,1474.70,37.52],
                                "Avg Purchase Total per Person":["$3.17","$3.05","$3.41"]
})
Purchase_Analysis.set_index("Gender",inplace=True)
Purchase_Analysis


#Age Demographics

# Establish bins for ages
age_data=purchase_data
df=pd.DataFrame(age_data)
bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

#Placing data to bins

#Placing data series in bins new column
df["Age Group"] = pd.cut(df["Age"],bins, labels=group_names)
#Creating Group that is based on bins
df=df.groupby("Age Group")
#df.max()

#Calculating percentages and total count by age group
#df["Age Group"] = pd.cut(df["Age"],bins, labels=group_names)
AG=df.SN.count()
#AG



#Summary Table of the Age demographic
Age=pd.DataFrame({"Percentage of Players":[3.99,4.86,23.61,63.37,17.53,12.67,7.12,2.26],
                  "Total Count":[23,28,136,365,101,73,41,13],
                  "Age Group":["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"]

}).set_index("Age Group")
Age


#Purchase Analysis(Age)

#mean=Age("Price").agg(['sum','mean'])
murugi= purchase_data
murugi_df = pd.DataFrame(murugi)
#murugi

# Establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

#Creating Group that is based on bins
murugi_df=murugi_df.groupby("Age Group")
#murugi_df.max()




#create summary table
Age=pd.DataFrame({"Percentage of Players":[3.99,4.86,23.61,63.37,17.53,12.67,7.12,2.26],
                  "Total Count":[23,28,136,365,101,73,41,13],
                  "Age Group":["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"]
            

}).set_index("Age Group")
sum_price=murugi_df.Price.sum()
Age


#Total Purchase Value(Age)

Age["Total Purchase Value"]=sum_price

#Average Total Purchase Value
Age['Average Purchase Price']=(Age['Total Purchase Value']/Age['Total Count']).map("${:.2f}".format)

#Total Purchase Value
Age["Total Purchase Value"]=sum_price

#Average Purchase Total per Person
Age['Average Purchase Total per Person']=(Age['Total Purchase Value']/Age['Total Count']).map("${:.2f}".format)

#Drop column not needed in summary
Age.drop('Percentage of Players',axis=1,inplace=True)
Age

#Top Spenders
#Identify the top 5 spenders
Five_tspenders=pd.merge(purchase_data.groupby(["SN"])[["Item ID"]].count(),
                      purchase_data.groupby(["SN"])[["Price"]].sum(), on="SN").sort_values(by=['Price'],ascending=False)
Five_tspenders=Five_tspenders.rename({"Item ID":"Purchase Count","Price":"Total Purchase Value"},axis="columns")
Five_tspenders["Average Purchase Price"]=(Five_tspenders["Total Purchase Value"]/Five_tspenders["Purchase Count"]).map("${:.2f}".format)
Five_tspenders["Total Purchase Value"]=Five_tspenders["Total Purchase Value"].map("${:.2f}".format)


#Print Summary Table of Top Five Spenders
Five_tspenders.head(5)

#Most Popular Items
#Retrieving Item ID,Item Name,Purchase ID from purchase_data dataframe
#Grouping by Item Item ID
Pop_items=pd.merge(purchase_data.groupby(["Item ID","Item Name"])[["Purchase ID"]].count(),
                       purchase_data.groupby(["Item ID", "Item Name"])[["Price"]].sum(),
                       on = ["Item ID","Item Name"]).sort_values(by=["Purchase ID"],ascending=False)

#Renaming Columns to resemble summary
Pop_items=Pop_items.rename({"Purchase ID":"Purchase Count","Price":"Total Purchase"},axis="columns")

Pop_items["Total Purchase Value"]=(Pop_items["Total Purchase"]).map("${:.2f}".format)

Pop_items.drop(columns=["Total Purchase"]).head()



#Most profitable items in descending order by Total Purchase Value
#Pop_items.sort_values(by='Total Purchase Value')
Pop_items.sort_values(['Total Purchase Value'],ascending=[True])
Pop_items.head()