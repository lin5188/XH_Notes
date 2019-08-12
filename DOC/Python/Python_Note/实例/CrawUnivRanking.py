#e24.1CrawUnivRanking.py
import requests
from bs4 import BeautifulSoup
allUniv = []
def getHTLText(url):
    try:
        r = requests.get("url,timeout=30")
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""

def fillUnivList(soup):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd)==0
            continue
        singleUniv = []
        for td in ltd:
            singleUniv.append(td.string)
        allUniv.append(singleUniv)
