#Imports
import pandas as pd

#Load my data
df = pd.read_csv("data/raw/PPR-2025.csv", encoding="latin1")

#Strip my columns
df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
)

#Drop the Product Size Description column, as it's completely null
df = df.drop(columns=["Property_Size_Description"])
#Check to make sure it's gone
print(df.columns)

#Convert the date of sale to datetime
#@reference (errors="coerce")
#https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html
df["Date_of_Sale_(dd/mm/yyyy)"] = pd.to_datetime(
    df["Date_of_Sale_(dd/mm/yyyy)"],
    dayfirst=True,
    errors="coerce"
)

print(df["Date_of_Sale_(dd/mm/yyyy)"].isna().sum())
#if it can't convert, get rid of it
df = df[df["Date_of_Sale_(dd/mm/yyyy)"].notna()]


