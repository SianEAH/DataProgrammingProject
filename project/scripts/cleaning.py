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
print("Columns before renaming")
print(df.columns)

#Convert the date of sale to datetime
#@reference (errors="coerce")
#https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html
#Date of Sale
df["Date_of_Sale_(dd/mm/yyyy)"] = pd.to_datetime(
    df["Date_of_Sale_(dd/mm/yyyy)"],
    dayfirst=True,
    errors="coerce"
)

print(df["Date_of_Sale_(dd/mm/yyyy)"].isna().sum())
#if it can't convert, get rid of it
df = df[df["Date_of_Sale_(dd/mm/yyyy)"].notna()]

#Price
#Rename the Price column because the euro symbol has been removed with the stripping
#Get rid of any hidden characters, spacing & encoding
#@reference (List Comprehension)
#https://www.w3schools.com/python/python_lists_comprehension.asp
df.columns = [
    "Price_EUR" if col.startswith("Price_") else col
    for col in df.columns
]


#Check to see if it worked
print("Columns after renaming the price column:")
print(df.columns)

#Price Conversion
df["Price_EUR"] = (
    df["Price_EUR"]
    .astype(str)
    #Treat as character, not regular expression
    #@reference
    #https://www.w3schools.com/python/python_regex.asp
    .str.replace(r"[^\d.]", "", regex=True)
)


df["Price_EUR"] = pd.to_numeric(df["Price_EUR"], errors="coerce")

#Drop any prices that are invalid (missing or <= 0)
#@reference (subset)
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html
df = df.dropna(subset=["Price_EUR"])
df = df[df["Price_EUR"] > 0]

#Validate
print(df["Price_EUR"].head())
#The Nulls
print("NaNs:", df["Price_EUR"].isna().sum())

#Create extra columns for Year and Month that will help with analysis later
df["Year"] = df["Date_of_Sale_(dd/mm/yyyy)"].dt.year
df["Month"] = df["Date_of_Sale_(dd/mm/yyyy)"].dt.month

#Final Checking
print(df.info())
print(df["Price_EUR"].describe())
print(df.isna().sum())

#Testing (for database issues found)
print("Cleaned rows: ", len(df))

#Save my cleaned data
#@reference (index=False)
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
df.to_csv(
    "data/processed/ppr_clean.csv",
    index=False,
    encoding="latin1",
    lineterminator="\n"
)






