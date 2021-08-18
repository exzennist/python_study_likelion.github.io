import urllib.request
from bs4 import BeautifulSoup

url ="https://comic.naver.com/webtoon/weekday"
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

title=soup.find_all(class_='title')

for i in title:
    if len(i.attrs['title'])>10:
       print(i.attrs['title'])