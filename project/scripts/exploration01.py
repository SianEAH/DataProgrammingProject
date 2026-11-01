#Imports
import pandas as pd

#Create a dataframe
#CSV file is encoding (latin1)
df = pd.read_csv("data/raw/PPR-2025.csv", encoding="latin1")

#Strip my columns
df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
)


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

#Check for any obvious outliers in the pricing
#Rename the column because of character issues with the euro sign
df = df.rename(columns={"Price ()": "Price_EUR"})
print(df["Price_EUR"].describe())

#Check Conversion
#@reference (errors="coerce")
#https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html
#Issues in this section to addressed during the next stages
#Date
df["Date of Sale (dd/mm/yyyy)"] = pd.to_datetime(
    df["Date of Sale (dd/mm/yyyy)"],
    dayfirst=True,
    errors="coerce"
)

print(df["Date of Sale (dd/mm/yyyy)"].isna().sum())


#Price
df["Price_EUR"] = (
    df["Price_EUR"]
    .astype(str)
    .str.replace(",", "")
)

df["Price_EUR"] = pd.to_numeric(df["Price_EUR"], errors="coerce")
print(df["Price_EUR"].isna().sum())
print(df["Price_EUR"].describe())






