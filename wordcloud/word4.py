import numpy as np # linear algebra
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import json

from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS

#mpl.rcParams['figure.figsize']=(8.0,6.0)    #(6.0,4.0)
mpl.rcParams['font.size']=12                #10
mpl.rcParams['savefig.dpi']=100             #72
mpl.rcParams['figure.subplot.bottom']=.1


stopwords = set(STOPWORDS)
data = "/Users/sungyujeong/Documents/졸작/front/wordcloud/Economy_news.arirang.json"

with open(data, "r") as json_file:
    json_data = json.load(json_file)
    context = json_data['contents'][0]['context']
    print(context)

wordcloud = WordCloud(
    background_color='white',
    stopwords=stopwords,
    width=1000,
    height=500,
    colormap="Set3"
    ).generate(context)

print(wordcloud)
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
fig.savefig("/Users/sungyujeong/Documents/졸작/front/wordcloud/word4.png", dpi=600)
