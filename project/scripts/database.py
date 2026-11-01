#Imports
import mysql.connector
import pandas as pd


#Load my processed ata
df = pd.read_csv(
    "data/processed/ppr_clean.csv",
    encoding="latin1"
)

#Create a MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bestintheworld1!",
    database="property_data"
)

#Create a cursor
cursor = conn.cursor()

#Insert statement
#@reference (%s)
#https://www.geeksforgeeks.org/python/what-does-s-mean-in-a-python-format-string/
insert_sql = """
INSERT INTO ppr_clean (
    Date_of_Sale, Address, County, Eircode, Price_EUR,
    Not_Full_Market_Price, VAT_Exclusive, Description_of_Property,
    Year, Month
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

#Make sure the columns are in order expected in workbench
cols = [
    "Date_of_Sale_(dd/mm/yyyy)",
    "Address",
    "County",
    "Eircode",
    "Price_EUR",
    "Not_Full_Market_Price",
    "VAT_Exclusive",
    "Description_of_Property",
    "Year",
    "Month"
]

#MySQL recognizes NaN as NULL values
#@reference (Pandas masking)
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mask.html
df = df.where(pd.notna(df), None)

#Make a list
data = df[cols].values.tolist()

#@reference
#https://www.w3schools.com/python/python_mysql_insert.asp
cursor.executemany(insert_sql, data)

#Validation (for database issues found)
print("Rows to insert:", len(data))
print("Sample row:", data[0]) #first index

#Commit my changes
conn.commit()
#Close
cursor.close()
conn.close()

#Validation
print("Data successfully inserted into MySQL")
