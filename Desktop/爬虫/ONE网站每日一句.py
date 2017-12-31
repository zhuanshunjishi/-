from bs4 import BeautifulSoup
import requests
import time

file    =  open('/Users/zhangmignqi/Desktop/one.txt','w')
url     =  "http://wufazhuce.com/one/020"
a       =  ["http://wufazhuce.com/one/{}".format(str(i))for i in range(0,1866,1)]

def get_attractions(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, "lxml")
    titles = soup.select('div.one-titulo')
    imgs = soup.select('div.one-imagen > img')
    cates = soup.select('div.one-cita')
    for title,img,cate in zip(titles,imgs,cates):
        data ={
            'title':title.get_text(),
            'img'  :img.get('src'),
            'cate' :cate.get_text(),
            }
        fang=str(data)
        file.write(fang+'\n')
        print(data)

for singke_url in a:
    get_attractions(singke_url)