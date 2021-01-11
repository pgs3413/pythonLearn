# xpath解析
from lxml import etree
import requests

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }

# 爬取58二手房信息
# url='https://bj.58.com/ershoufang/'
# page_text=requests.get(url,headers=headers).text
# tree=etree.HTML(page_text)
# title_list=tree.xpath("//ul[@class='house-list-wrap']/li/div[2]/h2/a/text()")
# for title in title_list:
#     print(title)


# 4k图片解析下载
# import os 
# os.mkdir("D:\\imgLibs")
# url="http://pic.netbian.com/4kmeinv/"
# response=requests.get(url,headers=headers)
# text=response.text
# tree=etree.HTML(text)
# a_list=tree.xpath("//ul[@class='clearfix']/li/a")
# for a in a_list:
#     img_src="http://pic.netbian.com/"+a.xpath("./img/@src")[0]
#     img_name=a.xpath("./img/@alt")[0]+".jpg"
#     img_name=img_name.encode("iso-8859-1").decode("gbk")
    # print(img_name,img_src)
    # img=requests.get(img_src,headers=headers).content
    # filename='D:\\imgLibs\\'+img_name
    # with open(filename,"wb") as f:
    #     f.write(img)
    # print(img_name+"下载成功")
、

