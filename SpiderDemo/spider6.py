# BeautifulSoup
# 获取三国演义

from bs4 import BeautifulSoup
import requests
import os
from time import sleep



headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
url="https://www.shicimingju.com/book/sanguoyanyi.html"

main_text=requests.get(url,headers=headers).text
main_soup=BeautifulSoup(main_text,"lxml")
a_list=main_soup.select(".book-mulu a")
a_list=a_list[88:]
for a in a_list:
    sleep(1)
    title=a.string
    content_url="https://www.shicimingju.com"+a['href']
    content_text=requests.get(content_url,headers=headers).text
    content_soup=BeautifulSoup(content_text,"lxml")
    div=content_soup.find("div",class_='chapter_content')
    content=div.text
    with open("D:\\sanguoyanyi.txt","a",encoding="utf-8") as f:
        f.write(title+"\n"+content+"\n")
    print(title+"下载完成！")

