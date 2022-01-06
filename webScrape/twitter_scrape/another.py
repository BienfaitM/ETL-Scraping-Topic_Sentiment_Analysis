# from requests_html import HTMLSession
# import pandas as pd 
# import numpy as np
# import requests
# import csv
# from bs4 import BeautifulSoup


# url = 'https://covid19.who.int/table'
# headers = []
# for table in soup.find_all('div',{"class":'sc-AxjAm kbGAkV'}):
#     for span in table.find_all('span'):
#         header = span.string
#         if header != None and header != ' - ':
#             headers.append(header)
# headers[1] = 'Cases-cumulative total'
# headers[2] = 'Cases-newly reported in last 7 days'
# headers[4] = 'Death-newly reported in last 7 days'
# # print(headers)
# # data = pd.DataFrame(columns = headers)

# names = []
# for j in soup.find_all('div',{"class":"tr depth_0"}):
#     for name in j('span'):
#         print(name.string)

# for k in soup.find_all('div',{"class":"column_Cumulative_Confirmed td"}):
#     for cumulative in k.find_all('div',{"class":"sc-pktCe jPVcHM"}):
#         print(cumulative.string)


   