import requests
import re

r = requests.get("https://book.douban.com/")
html = r.text
regex = re.compile('<li.*?href="(.*?)"title="(.*?)".*?author">(.*?).*?year">(.*?)</span>.*?</li>',re.S)
Quans = re.findall(regex,html)
for Quan in Quans:
    url,name,author,date = Quan
    author = re.sub('\s',"",author)
    date = re.sub('\s',"",date)
    print(url,name,author,date)


