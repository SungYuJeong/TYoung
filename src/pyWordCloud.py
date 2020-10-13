from bs4 import BeautifulSoup
import requests
import threading
import time

import stylecloud
₩

if __name__ == '__main__':

    source = 'http://arirang.com/index.asp?sys_lang=Eng'
    req = requests.get(source)
    dataset = BeautifulSoup(req.text, 'html.parser')
    print(dataset)

    stylecloud.gen_stylecloud(dataset.text,
                             icon_name = 'fas fa-crown',
                             palette = 'colorbrewer.diverging.Spectral_11',
                             gradient = 'vertical', #horizontal
                             size=(1024, 512)
    )


    # def thread_run():
    #     stylecloud.gen_stylecloud(dataset.text)
    #     print(dataset)
    #     threading.Timer(10, thread_run).start()
    #
    # thread_run()


