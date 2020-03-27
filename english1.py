import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# 아리랑 tv 뉴스 URL
url = 'http://www.arirang.com/News/News_List.asp?sys_lang=Eng&category=0'

# 뉴스 제목 크롤링
r = requests.get(url)
html = r.content
soup = BeautifulSoup(html, 'html.parser')
titles_html = soup.select('.aI_section > div > div > ul > li > a > h4')

# 크롤링한 결과 출력 파일 생성
out=open("output.txt",'w', -1, "utf-8")

# 불용어 제거한 결과 출력 파일 생성
out1=open("stopword_output.txt",'w', -1, "utf-8")

stop_words = set(stopwords.words('english'))

result = []
for i in range(len(titles_html)):
    word_tokens = nltk.word_tokenize(titles_html[i].text)
    print(word_tokens, file=out)     # 크롤링 결과 저장
    for w in word_tokens:
        if w not in stop_words:
            result.append(w)
print(result, file=out1)      # 불용어 제거 결과 저장






