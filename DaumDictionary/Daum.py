from selenium import webdriver
import pandas as pd

path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(path)

# print("검색하려는 영어 단어를 입력하세요.")
# word = input()

driver.get("https://small.dic.daum.net/index.do?dic=eng&q=")
search_box = driver.find_element_by_name("q")
search_box.send_keys("International")
search_box.submit()

mean = driver.find_element_by_xpath("//*[@id='mArticle']/div[1]/div[1]/div[3]/div")

out=open("mean.txt",'w', -1, "utf-8")
means = mean.text.replace('\r', '').replace('듣기', '').replace('뜻별예문', '').replace('참고', '').replace('더보기', '').replace('열기', '').replace('\n', '\n')


#[어원]으로 시작하는 행을 제거 (개선필요 ,,,,)
with open("mean.txt", 'r') as infile:
    data = infile.readlines()
with open("mean.txt", 'w') as outfile:
    for i in data:
        if not i.startswith("[어원]"):
            outfile.write(i)

print(means, file = out)
driver.quit()
