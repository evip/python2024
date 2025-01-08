import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

csv_path = "gdp.csv"
df = pd.read_csv(csv_path)

# Hien thi thong tin
# print(df.head())
# print(df.info())

df = df.dropna(subset=['Value'])

country1 = 'Arab World'
country2 = 'Viet Nam'
country = [country1, country2]

#loc_country1 = df[df['Country Name'] ==country1]
#loc_country2 = df[df['Country Name'] ==country2]
#loc_country = pd.concat([loc_country1, loc_country2], ignore_index=True)
loc_country = df[df['Country Name'].isin(country)]
print(loc_country)

loc_c_y = loc_country[loc_country['Year'] >=2000]
print(loc_c_y)