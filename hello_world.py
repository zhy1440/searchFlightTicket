#!/usr/bin/python3
import requests
import datetime
import re
from bs4 import BeautifulSoup
import json
import time

thisdict = {}
begin_date = datetime.datetime(2019, 3, 10)
end_date = datetime.datetime(2019, 4, 30)
output_filename = "./json/" + begin_date.strftime("%Y-%m-%d") + ".json"

origin = "PVG"
dst = "USU"


def writeFile(fileName, content):
    # 写文件
    with open(fileName, "w+", encoding="utf-8") as out_file:
        out_file.write(content)
    print("Save file success ============> ", fileName)


def getUrl(origin, destination, date):
    return  'https://book.cebupacificair.com/Flight/InternalSelect?' + \
        'o1=' + origin + \
        '&d1=' + destination + \
        '&o2=' + destination + \
        '&d2=' + origin + \
        '&dd1=' + currentDateStr + \
        '&p=&ADT=1&CHD=0&INF=0&s=true&mon=true'


def getFlightInfoStr(htmlContent, html_file_name):
    # 创建一个BeautifulSoup解析对象
    outputString = ""
    soup = BeautifulSoup(htmlContent, "html.parser", from_encoding="utf-8")
    print(soup.title)

    # 写文件
    writeFile(html_file_name, soup.prettify())

    unavailableTr = soup.find(attrs={"class": "avail-info-no-flights"})
    if (unavailableTr != None):
        print(unavailableTr)
    else:
        trs = soup.find_all(attrs={"class": "faretable-row"})
        for tr in trs:
            outputString += tr.get_text("|", strip=True) + "|"
    return outputString


deltaDays = (end_date - begin_date).days

for i in range(deltaDays):
    print(
        "-------------------------------------------------------------------")
    currentDate = begin_date + datetime.timedelta(days=i)
    currentDateStr = currentDate.strftime("%Y-%m-%d")
    print(currentDateStr)

    url = getUrl(origin, dst, currentDateStr)
    r = requests.get(url)

    print(len(r.text))
    if (len(r.text) < 10000):
        break
    if (len(r.text) < 100000):
        continue

    html_file_name = "./html/" + currentDateStr + ".html"
    thisdict[currentDateStr] = getFlightInfoStr(r.text, html_file_name)

    time.sleep(10)

resultJson = json.dumps(thisdict, indent=4)

# print(resultJson)
writeFile(output_filename, resultJson)

print("============ Finish all ============")

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
