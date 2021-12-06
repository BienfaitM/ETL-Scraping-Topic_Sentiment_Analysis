import requests_html
from requests_html import HTMLSession
import pandas as pd 
import numpy as np
import json
import csv


session = HTMLSession()

def get_url(url):
    page = session.get(url)
    #sleep and scroll
    page.html.render(sleep =1, scrolldown=5)
    
    #find news by inspecting articlec
    articles = page.html.find('article')
    newslist = []

    for item in articles:
        try:
            newsitem = item.find('h3', first = True)
            title    = newsitem.text
            link     = newsitem.absolute_links

            newsarticle = {
                'title' : title,
                'link'  : link
            }
            newslist.append(newsarticle)
        except:
            pass
    return newslist

def list_csv(my_list,my_columns = []):
    with open('test.csv','w') as f:
        writer = csv.DictWriter(f,fieldnames = my_columns)
        writer.writeheader()
        writer.writerows(my_list)

url = 'https://news.google.com/search?q=Congo&hl=en-KE&gl=KE&ceid=KE%3Aen'
the_list = get_url(url)
list_csv(the_list, ['title','link'])
