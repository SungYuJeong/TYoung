from datetime import datetime
import re
import csv
import json
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def toCSV(arirang_list):
    with open('arirang_title.csv', 'w', encoding='utf-8', newline='') as file:
        csvfile = csv.writer(file)
        for row in arirang_list:
            csvfile.writerow(row)


def toJson(arirang_dict):
    with open('arirang_title.json', 'w', encoding='utf-8') as file:
        json.dump(arirang_dict, file, ensure_ascii=False, indent='\t')


id = -1
arirang_list = []
arirang_dict = {}
for page in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
    source = 'http://www.arirang.com/News/News_List.asp?sys_lang=Eng&category='+str(page+1)
    req = requests.get(source)
    html = BeautifulSoup(req.text, 'html.parser')
    li_list = html.select('#aNews_List > ul > li')

    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        temp_list = []
        temp_dict = {}
        id += 1

        # 뉴스 제목 크롤링
        title = li_list[i].find('h4').text

        # 각 뉴스의 날짜 크롤링
        date = li_list[i].find('div').text.strip()

        temp_list.append([id, source, date[0:10], title])
        temp_dict[str(id)] = {'id': id,'source': source, 'date': date[0:10], 'title': title}


        arirang_list += temp_list
        arirang_dict = dict(arirang_dict, **temp_dict)

# 리스트 출력
for item in arirang_list:
    print(item)

# 사전형 출력
id = -1
for item in arirang_dict:
    id += 1
    print(item, arirang_dict[item]['id'],arirang_dict[item]['source'], arirang_dict[item]['date'], arirang_dict[item]['title'])

# CSV 파일 생성
toCSV(arirang_list)

# Json 파일 생성
toJson(arirang_dict)




