#!/usr/bin/python3
import datetime
import requests
from bs4 import BeautifulSoup

x = datetime.datetime(2019, 3, 10)

date = x.strftime("%Y-%m-%d")
url = 'https://book.cebupacificair.com/Flight/InternalSelect?o1=MNL&d1=USU&o2=USU&d2=MNL&dd1=' + \
    date + '&p=&ADT=1&CHD=0&INF=0&s=true&mon=true'
print(url)
r = requests.get(url)

print(len(r.text))
# # Read a file
# with open("test.txt", "rt", encoding="utf-8") as in_file:
#     text = in_file.read()

# 创建一个BeautifulSoup解析对象
soup = BeautifulSoup(r.text, "html.parser", from_encoding="utf-8")
print(soup.title.get_text())
imgs = soup.find_all('img')
for img in imgs:
    imgUrl = "https://book.cebupacificair.com/"+img['src']
    r = requests.get(imgUrl, stream=True)
    image_name = imgUrl.split('/')[-1]
    print("================>", imgUrl)
    # with open('./img/%s' % image_name, 'wb') as f:
    #     for chunk in r.iter_content(chunk_size=128):
    #         f.write(chunk)
    # print('Saved %s' % image_name)
