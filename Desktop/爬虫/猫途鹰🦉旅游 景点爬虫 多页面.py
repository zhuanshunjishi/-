from bs4 import BeautifulSoup
import requests
import time

file    =  open('/Users/zhangmignqi/Desktop/巴黎景点.txt','w')
url     =  "https://www.tripadvisor.cn/Attractions-g187147-Activities-Paris_Ile_de_France.html"
a       =  ["https://www.tripadvisor.cn/Attractions-g187147-Activities-oa{}-Paris_Ile_de_France.html#ATTRACTION_LIST".format(str(i))for i in range(0,1200,30)]

def get_attractions(url,data=None):
    wb_data = requests.get(url)
    time.sleep(2)
    soup    = BeautifulSoup(wb_data.text,"lxml")
    titles  = soup.select('div.listing_title > a')
    imgs    = soup.select('img[height="180"]')
    cates = soup.select('div.p13n_reasoning_v2')
    for title,img,cate in zip(titles,imgs,cates):
        data ={
            'title':title.get_text(),
            'img'  :img.get('src'),
            'cate' :list(cate.stripped_strings),
            }
        fang=str(data)
        file.write(fang+'\n')
        print(data)

for singke_url in a:
    get_attractions(singke_url)