#Imports
import pandas as pd

#Create a dataframe
#CSV file is encoding (latin1)
df = pd.read_csv("data/raw/PPR-2025.csv", encoding="latin1")

#Explore the first rows
print("First 5 rows:")
print(df.head())

#Get information about my dataset
print("\nDataset info:")
print(df.info())

#Briefly explore the top 5 counties
print(df["County"].value_counts().head(5))

#Check about the specific of the null values
print(df.isna().sum())

#Check for duplicate values
print(df.duplicated().sum())