from bs4 import BeautifulSoup as bs
import requests as req

url='https://news.ycombinator.com/'

resp=req.get(url=url)
resp.encoding='utf-8'
soup=bs(resp.text,'lxml')


content=soup.find_all('span','titleline')

for txt in content:
    print(f'{txt.a.text}:\t{txt.a['href']}')
