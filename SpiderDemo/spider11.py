# 爬取梨视频的视频数据

import requests
from lxml import etree
import re
from multiprocessing.dummy import Pool

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
first_url="https://www.pearvideo.com/category_5"

first_text=requests.get(url=first_url,headers=headers).text
tree=etree.HTML(first_text)
li_list=tree.xpath('//ul[@id="listvideoListUl"]/li')
video_list=[]
for li in li_list:
    second_url="https://www.pearvideo.com/"+li.xpath("./div/a/@href")[0]
    video_name=li.xpath('.//div[@class="vervideo-title"]/text()')[0]+".mp4"
    # print(second_url,video_name)
    second_text=requests.get(url=second_url,headers=headers).text
    r='srcUrl="(.*?)",vdoUrl'
    video_url=re.findall(r,second_text)[0]
    # print(video_name,video_url)
    dic={
        'name':video_name,
        'url':video_url
    }
    video_list.append(dic)

def getVideoData(dic):
    url=dic['url']
    name=dic['name']
    print(name,"正在下载...")
    data=requests.get(url=url,headers=headers).content
    filename="E:\\spiderVideo\\"+name
    with open(filename,"wb") as f:
        f.write(data)
    print(name,"下载完成")

pool=Pool(4)
pool.map(getVideoData,video_list)
pool.close()
pool.join()
