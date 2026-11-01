#Imports
import pandas as pd
import matplotlib.pyplot as plt

#Load my processed data
df = pd.read_csv("data/processed/ppr_clean.csv", encoding="latin1")

#Insight 1: How the property prices in Ireland have changed over time
#@reference (reset_index)
#https://pandas.pydata.org/docs/reference/api/pandas.Series.reset_index.html
#Method
monthly_prices = (
    df.groupby("Month")["Price_EUR"]
      .median()
      .reset_index()
)

print(monthly_prices)

#Visualisation
monthly_prices.plot(
    x="Month",
    y="Price_EUR",
    kind="line",
    marker="o",
    linewidth=2,
    color="black"
)

plt.title("Median Property Prices Over Time in Ireland")
plt.xlabel("Month")
plt.ylabel("Median Property Price (€)")
plt.grid(True)

plt.show()

#Insight 2: The price differences across different counties in Ireland for 2025
county_prices = (
    df.groupby("County")["Price_EUR"]
      .median()
      .sort_values(ascending=False) #Descending order
      .reset_index()
)

#The first few
print(county_prices.head())

#First 10 counties
top_counties = county_prices.head(10).set_index("County")

ax = top_counties.plot.bar(
    y="Price_EUR",
    rot=45,
    color="skyblue",
)

plt.title("Top 10 Counties in Ireland by Median Property Price for 2025")
plt.xlabel("County")
plt.ylabel("Median Property Price (€)")

#Add the values on top of the bar chart
#Format the numbers so it looks cleaner
for container in ax.containers:
    ax.bar_label(container, fmt="€{:,.0f}", padding=3, fontsize=7)

plt.show()

#Insight 3: The price difference between newer properties and older properties
property_type_prices = (
    df.groupby("Description_of_Property")["Price_EUR"]
      .median()
      .reset_index()
)

print(property_type_prices)

ax = property_type_prices.plot.barh(
    x="Description_of_Property",
    y="Price_EUR",
    color="purple",
    #@reference (figsize)
    #https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
    figsize=(12,6)
)

plt.title("Median Property Prices by Property Type (2025)")
plt.xlabel("Property Type")
plt.ylabel("Median Property Price (€)")
#@reference (xticks)
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html
plt.xticks(rotation=30, ha="right")

#Values on top of the bars
#Add the formatting
for container in ax.containers:
    ax.bar_label(container, fmt="€{:,.0f}")

#@reference (subplots_adjust)
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html
plt.subplots_adjust(left=0.35)
plt.show()

#Insight 4: Are there any outliers that would affect the median property prices across Ireland?
ax = df.plot.box(
    column="Price_EUR",
    figsize=(8, 5),
    capprops=dict(color="grey"),
    whiskerprops=dict(color="red", linestyle="--"),
    flierprops=dict(marker="o", markerfacecolor="orange", markersize=6),
    medianprops=dict(color="black", linewidth=2)
)

plt.title("Distribution of Residential Property Prices in Ireland (2025)")
plt.ylabel("Property Price (€)")
plt.show()










