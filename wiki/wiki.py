import lxml
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

from .constants import BASE

def summary(page):
    url = BASE + f"/page/summary/{page}"

    resp = requests.get(url)

    resp_json = resp.json()

    return resp_json["extract"]

def html(page):
    url = BASE + f"/page/html/{page}"

    resp = requests.get(url)

    soup = bs(resp.text,'lxml').find("body")

    return soup

def media_list(page):
    url = BASE + f"/page/media-list/{page}"

    resp = requests.get(url)

    resp_json = resp.json()

    return resp_json["items"]

def search(query):
    url = f"https://en.wikipedia.org/w/api.php?action=opensearch&format=json&formatversion=2&search={query}&namespace=0&limit=10"
    
    resp = requests.get(url)

    resp_json = resp.json()

    titles = resp_json[1]
    urls = resp_json[3]

    data = []
    entries = zip(titles,urls)
    for e in entries:
        data.append([e[0],e[1]])
    
    return pd.DataFrame(data=data,columns=["Page Title","URL"])