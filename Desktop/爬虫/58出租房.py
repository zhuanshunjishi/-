from bs4 import BeautifulSoup
import requests
import time

file    =  open('/Users/zhangmignqi/Desktop/北京出租房.txt','w')
url     =  "http://bj.58.com/chuzu/?PGTID=0d3090a7-0000-11cd-3998-3a7e3d2181a0&ClickID=2"
a       =  ["http://bj.58.com/chuzu/pn{}/?PGTID=0d3090a7-0000-17e5-2252-4b7c1fada833&ClickID=2".format(str(i))for i in range(0,71,1)]

def get_attractions(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, "lxml")
    titles = soup.select('div.des > p.add')
    sts = soup.select('div.des > p.room')
    prices = soup.select('div.money')
    for title,st,price in zip(titles,sts,prices):
        data ={
            'title':title.get_text(),
            'st'   :st.get_text(),
            'price':price.get_text()
            }
        fang=str(data)
        file.write(fang+'\n')
        print(data)

for singke_url in a:
    get_attractions(singke_url)