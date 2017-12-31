from bs4 import BeautifulSoup
import requests

file = open('/Users/zhangmignqi/Desktop/北京短租房0.txt','w')
url  = 'http://bj.xiaozhu.com/fangzi/1209886305.html'

def get_attractions(url,data=None):
    wb_data = requests.get(url)
    soup    = BeautifulSoup(wb_data.text, "lxml")
    titles  = soup.select('h4 > em')
    adds    = soup.select('div.pho_info > p > span')
    prices  = soup.select('div.day_l')
    names   = soup.select('h6 > a.lorder_name')


    for title, add , price , name in zip(titles , adds , prices , names ):
        data = {
            'title': title.get_text(),
            'add'  : add.get_text(),
            'price': price.get_text(),
            'name' : name.get_text(),
            }
        fan=str(data)
        file.write(fan+'\n')
        print(data)

abc        = 'http://bj.xiaozhu.com/'
zmq_data   = requests.get(abc)
soup       = BeautifulSoup(zmq_data.text, "lxml")
hrefs_list = soup.select('a.resule_img_a')
for href in hrefs_list:
    link = (href.get("href"))
    if 'bj' in link:
        get_attractions(link)