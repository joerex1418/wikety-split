import requests

from constants import BASE

def summary(page_title):
    url = BASE + f"/page/summary/{page_title}"
    
    resp = requests.get(url)

    return resp.json()