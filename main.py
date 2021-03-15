import pandas as pd
import matplotlib.pyplot as plt
import get_datasets as gd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

gd.get_dataset()

country_data = pd.read_csv("country_vaccinations.csv")

print(country_data.head())
print(country_data.shape)

find_nulls = country_data.isnull().sum()
new_data = country_data.sort_values('total_vaccinations', ascending=False).groupby('country',
                                                                                  sort=True).first().reset_index()
