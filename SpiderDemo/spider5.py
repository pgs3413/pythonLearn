# 爬取图片 换页 正则表达式

import re
import requests
import os

# os.mkdir("D:\\qiutuImg")

def getImage(a):
    url=f"https://www.qiushibaike.com/imgrank/page/{a}/"
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }

    page_text=requests.get(url,headers=headers).text
    # print(page_text)

    # <div class="thumb">
    # <a href="/article/123410269" target="_blank">
    # <img src="//pic.qiushibaike.com/system/pictures/12341/123410269/medium/J9BP4LDTVWZS6FII.jpg" alt="糗事#123410269" class="illustration" width="100%" height="auto">
    # </a>
    # </div>

    reg = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    src_list=re.findall(reg,page_text,re.S)
    # print(src_list)

    for src in src_list:
        src="https:"+src
        img=requests.get(src,headers=headers).content
        imgName=src.split('/')[-1]
        imgSrc="D:\\qiutuImg\\"+imgName
        with open(imgSrc,"wb") as f:
            f.write(img)
        print(imgName,"下载成功！")

for i in range(2):
    getImage(i+1)
