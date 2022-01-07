from requests_html import HTMLSession
import pandas as pd 
import numpy as np
import requests
import csv
from bs4 import BeautifulSoup

# https://medium.com/analytics-vidhya/how-to-scrape-a-table-from-website-using-python-ce90d0cfb607

url = 'https://www.worldometers.info/coronavirus/'
page = requests.get(url)
soup = BeautifulSoup(page.text,'lxml')

headers = []
table =soup.find('table',{"id":"main_table_countries_today"})
for header in table.find_all('th'):
    headers.append(header.text)


covid_df = pd.DataFrame(columns = headers)
# covid_df.to_csv('covid_df.csv')

for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row= [i.text for i in row_data]
    length = len(covid_df)
    covid_df.loc[length] = row

# Drop and clearing unnecessary rows
covid_df.drop(covid_df.index[0:7], inplace=True)
covid_df.drop(covid_df.index[222:229], inplace=True)
covid_df.reset_index(inplace=True, drop=True)

covid_df.to_csv('covid_df.csv')