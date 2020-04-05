import csv
import json
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


for page in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
    source = 'http://www.arirang.com/News/News_List.asp?sys_lang=Eng&category='+str(page+1)
    req = requests.get(source)
    html = BeautifulSoup(req.text, 'html.parser')
    li_list = html.select('#aNews_List > ul > li ')

    stop_words = set(stopwords.words('english'))
    result = []
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        result = []
        for i in range(len(li_list)):
            word_tokens = nltk.word_tokenize(li_list[i].find('h4').text)

            for w in word_tokens:
                if w not in stop_words:
                    result.append(w)

    tagged_list = pos_tag(result)
    print(tagged_list)







