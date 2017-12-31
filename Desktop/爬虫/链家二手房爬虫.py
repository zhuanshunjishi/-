from bs4 import BeautifulSoup
import requests

file    =  open('/Users/zhangmignqi/Desktop/北京二手房.txt','w')
url     =  "https://bj.lianjia.com/ershoufang/"
a       =  ["https://bj.lianjia.com/ershoufang/pg{}/".format(str(i))for i in range(0,10000,1)]

def get_attractions(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, "lxml")
    titles = soup.select('div.houseInfo')
    loucens = soup.select('div.positionInfo')
    prices = soup.select('div.totalPrice')
    for title,loucen,price in zip(titles,loucens,prices):
        data ={
            'title':title.get_text(),
            'loucen'  :loucen.get_text(),
            'price' :price.get_text(),
            }
        fang=str(data)
        file.write(fang+'\n')
        print(data)

for singke_url in a:
    get_attractions(singke_url)