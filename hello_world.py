#!/usr/bin/python3
from PIL import Image
from io import BytesIO
import requests
import datetime

import re
from bs4 import BeautifulSoup
import json

thisdict = {}
begin_date = datetime.datetime(2019, 3, 10)
end_date = datetime.datetime(2019, 3, 20)
deltaDays = (end_date - begin_date).days
for i in range(deltaDays):
    # print(i)
    x = begin_date+datetime.timedelta(days=i)
    print(x.strftime("%Y-%m-%d"))

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
    print(soup.title)
    print("============> Start write file")
    # 写文件
    html_file_name = "./html/"+date+".html"
    print(html_file_name)
    with open(html_file_name, "w+", encoding="utf-8") as out_file:
        out_file.write(soup.prettify())
    print("============> Finish write file!!!")
    outputString = ""
    trs = soup.find_all(attrs={"class": "faretable-row"})
    for tr in trs:
        outputString += tr.get_text("|", strip=True)+"|"
# arr = outputString.split("|")
# print(arr)
    thisdict[date] = outputString
y = json.dumps(thisdict, indent=4)

print(y)
# 写文件
with open("./json/output.json", "w+", encoding="utf-8") as out_file:
    out_file.write(y)
print("============> Finish all!!!")


# img_ul = soup.find_all('ul', {"class": "img_list"})
# print(img_ul)
# for ul in img_ul:
#     imgs = ul.find_all('img')
#     for img in imgs:
#         url = img['src']
#         r = requests.get(url, stream=True)
#         image_name = url.split('/')[-1]
#         with open('./img/%s' % image_name, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=128):
#                 f.write(chunk)
#         print('Saved %s' % image_name)
# links = soup.find_all('a')
# print("所有的链接")
# for link in links:
#     print("=====================================")
#     print(link.name, link['href'], link.get_text())
#     link_node = soup.find('a', href=link["href"])
#     print(link_node.name, link_node['href'],
#           link_node['class'], link_node.get_text())

# print("正则表达式匹配")
# link_node = soup.find('a', href=re.compile(r"ti"))
# print(link_node.name, link_node['href'],
#       link_node['class'], link_node.get_text())

# print("获取P段落的文字")
# p_node = soup.find('p', class_='story')
# print (p_node.name, p_node['class'], p_node.get_text())
