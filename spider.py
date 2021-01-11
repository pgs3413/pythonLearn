"""                        1.京东商品页面的爬取      """
# import requests
# url = 'https://item.jd.com/100008348530.html'
# r = requests.get(url)
# print(r.status_code)
# print(r.encoding)
# print(r.text)

"""                       2.百度（360）搜索关键词提交            """
# import requests
# url = 'http://www.so.com/s'
# wd = '中国'
# kv = {'q': '中国'}
# headers = {'user-agent': 'Mozilla/5.0(X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}
# r = requests.get(url, params=kv, headers=headers)
# url='http://www.baidu.com/s?wd=python'
# r=requests.get(url)
# print(r.status_code)
# print(r.url)
# print(r.encoding)
# r.encoding = 'utf-8'
# print(r.text)

"""                                       3.网络图片的爬取和存储         """
# 网络图片链接格式：http://www.example.com/picture.jpg
# import requests
# 点开大图，右键复制图像地址
# url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1578042662202&di=f9ab3dcfc9a5117eb83e4bdc24838573&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20181119%2Fd5651667201942f19eafbcceba15736c.jpeg'
# r = requests.get(url)
# print(r.status_code)
# path = 'D:\yang.jpeg'
# with open(path, 'wb') as f:
#     f.write(r.content)

"""                                     4.模拟登录微博 (不会）           """

"""                              5.中国大学排名定向爬虫             """
"""
1：从网络上获取排名网页内容 getHTMLText()
2：提取网页内容中信息到合适的数据结构（二维列表） fillUnivList()
3.利用数据结构展示并输出结果 printUnivList()
"""
# import requests
# from bs4 import BeautifulSoup
# import bs4
#
# def getHtMLText(url):
#     try:
#         r = requests.get(url)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         print("请求失败")
#
# def fillUnivList(html,ulist):
#     soup = BeautifulSoup(html, "html.parser")
#     for tr in soup.find('tbody').children:
#         if isinstance(tr,bs4.element.Tag):
#             tds = tr.find_all('td')
#             ulist.append([tds[0].string, tds[1].string, tds[2].string])
#
# def printUnivList(ulist, num):
#     print("{:^10}\t{:^6}\t{:^10}".format("排名","学校","城市"))
#     for i in range(num):
#         print("{:^10}\t{:^10}\t{:^10}".format(ulist[i][0],ulist[i][1],ulist[i][2]))
#
# def main():
#     ulist = []
#     url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
#     html = getHtMLText(url)
#     fillUnivList(html, ulist)
#     printUnivList(ulist, 20)
#
# main()

""""                    6.虎扑主页爬取信息并保存到文件中            """
# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://voice.hupu.com/nba'
# r = requests.get(url)
# r.encoding=r.apparent_encoding
# demo = r.text
# soup = BeautifulSoup(demo, "html.parser")
# list = []
# for news in soup.find_all("div", "list-hd"):
#     list.append(news.find('a').string.rstrip())
# path = 'hupu.txt'
# with open(path,'w') as f:
#     for x in list:
#         f.write(x+"\n")


"""                   7.淘宝商品比价定向爬虫             """
"""
目标： 获取淘宝搜索页面的信息，提取其中的商品名称和价格
理解：淘宝的搜索接口 翻页的处理
步骤： 
1.提交商品搜索请求，循环获取页面(失败）
2.对于每个页面，提取商品名称和价格
3.将信息输出到屏幕中
"""
"""
淘宝和京东都要登录，迫不得已只能爬当当网
"""
# import requests
# import re
#
#
# def getHTMLText(url):
#     try:
#         r = requests.get(url)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         print("Wrong")
#
# def ParseHtml(ulist,html):
#     nums = re.findall('<div.*?>(\d+).</div>', html)
#     infos = re.findall('<div class="name"><a.*?title="(.*?)">', html)
#     for i in range(len(nums)):
#         ulist.append([nums[i], infos[i]])
#
#
# def printInfo(ulist):
#     for i in range(len(ulist)):
#         print(ulist[i][0]+"    "+ulist[i][1])
#
#
# start_url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-all-0-0-1-'
# pagelist = [1, 2, 3]
# ulist = []
# for i in range(3):
#     url = start_url+str(pagelist[i])
#     html = getHTMLText(url)
#     ParseHtml(ulist, html)
# printInfo(ulist)

"""
不同的信息存在于不同的标签内，有不同的标签属性，要利用好这点
"""
