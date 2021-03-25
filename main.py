import pandas as pd
import matplotlib.pyplot as plt
import get_datasets as gd
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

gd.get_dataset()

country_vaccination_data = pd.read_csv("country_vaccinations.csv")

#print(country_vaccination_data.head())

country_case_data = pd.read_csv('country_wise_latest.csv')

#print(country_case_data)
#
# country2=[]
#
# for country in country_case_data['Country/Region']:
#     country2.append(country)
#     for country3 in country_vaccination_data['country']:
#         if country3 not in country2:
#             print(country3)


