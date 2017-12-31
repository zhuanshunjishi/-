from bs4 import BeautifulSoup
import requests
import time

file    =  open('/Users/zhangmignqi/Desktop/北京 二手车.txt','w')
url     =  "http://bj.58.com/ershouche/?PGTID=0d3036e3-0000-1d0b-f044-da003cb6acba&ClickID=31"
a       =  ["http://bj.58.com/ershouche/pn{}/?PGTID=0d30001d-0000-1e7b-58d8-f479e5a46751&ClickID=33".format(str(i))for i in range(0,1000,1)]

def get_attractions(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, "lxml")
    titles = soup.select('div.col.col2 > a > h1')
    prices = soup.select('div.col.col3 > h3')
    cates = soup.select('div.tags_left')
    for title, price, cate in zip(titles, prices, cates):
        data = {
            'title': title.get_text(),
            'price': price.get_text(),
            'cate': list(cate.stripped_strings),
        }
        fang = str(data)
        file.write(fang + '\n')
        print(data)

for singke_url in a:
    get_attractions(singke_url)