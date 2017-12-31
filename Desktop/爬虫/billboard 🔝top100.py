from bs4 import BeautifulSoup
import requests

file = open('/Users/zhangmignqi/Desktop/billboard.txt','w')
url     =  "http://www.billboard.com/charts/hot-100"

def get_attractions(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, "lxml")
    titles = soup.select('div.chart-row__rank > span.chart-row__current-week')
    cates = soup.select('div.chart-row__title > h2')

    for title , cate in zip(titles, cates):
        data = {
            'title': title.get_text(),
            'cate' : cate.get_text(),
        }
        fan=str(data)
        file.write(fan+'\n')
        print(data)
print(get_attractions(url))