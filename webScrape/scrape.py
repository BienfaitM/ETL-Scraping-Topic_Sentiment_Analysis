import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests.models import Response

def read_csv(path):
    return pd.read_csv(path, delimiter=',', encoding='cp1252')
path = '/Users/mt/Desktop/python/webScrape/congo_corruption.csv'

data = read_csv(path)

corruption_copy = data.copy()
corruption_copy= corruption_copy.convert_dtypes()
# links remove so characters
def remove_b(link):
    return link.strip("{}")
corruption_copy['link'] = corruption_copy['link'].apply(remove_b)

def remove_other(link):
    return link.strip("'")
corruption_copy['link'] = corruption_copy['link'].apply(remove_other)

def scrape_screenplay(url):
    Response = requests.get(url)
    html_string = Response.text
    return html_string

corruption_copy['text'] = corruption_copy['link'][:30].apply(scrape_screenplay)



    #with open('corruption.txt','a') as f
    #f.write(para)
for text in corruption_copy['text'][:30]:
    soup = BeautifulSoup(text,'html.parser')

    for para in soup.find_all('p'):
        para.get_text()

        newscorruption = para.get_text()
        with open('corruption.txt','a', encoding='utf-8') as f:
            f.write(newscorruption)
