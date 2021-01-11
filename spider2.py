
"""                            001  urllib        """

"""urllib.request.urlopen"""
# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

"""Request对象 模拟浏览器  parse 解析"""
"""urllib.request.Request(url,data=None,headers={},method=None)"""
# from urllib import request, parse
# url = 'https://www.baidu.com'
# headers={
#     'User-agent':'Mozilla/5.0(X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11',
# }
# dict = {
#     'name':'Germey'
# }
# data = bytes(parse.urlencode(dict),encoding='utf-8')
# req=request.Request(url,data=data,headers=headers,method='POST')
# response=request.urlopen(req)
# print(response.read().decode('utf-8'))

"""                          002  requests       """
"""   get post  request head put patch delete """

"""r=requests.get(url,params=None,**kwargs)"""
"""
response对象包含爬虫返回的内容 
r.status_code r.text r.encoding r.apparent_encoding(备用编码方式） r.content(二进制形式）
"""
# import requests
# r = requests.get('http://wwww.baidu.com')
# print(r.status_code)
# r.encoding = 'utf-8'
# print(r.text)

"""爬取网页的通用代码框架"""
"""r.raise_for_status() 如果不是200,产生异常requests.HTTPError"""
# import requests
# def getHTMLText(url):
#     try:
#         r = requests.get(url)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return '产生异常'
# if __name__ == "__main__":
#     url = 'www.baidu.com'
#     print(getHTMLText(url))


"""URL格式：http://host[:port][path]"""
"""
host:合法的Internet主机域名或IP地址
port：端口号，缺省端口为80
path：请求资源的路径
"""
"""requests库主要方法"""
"""
request:基础方法 requests.request(method,url,**kwargs)
method:
get:请求获取url位置的资源
head：获得该资源的头部信息
post：请求向URL位置的资源后附加新的数据
put：请求向url位置存储一个资源，覆盖原url位置的资源
patch：请求局部更新url资源
delete：请求删除url位置存储的资源
**kwargs:控制访问的参数，均为可选项，13个
"""
# params:字典或字节序列，作为参数增加到url中,不止访问资源，带入参数，根据参数返回资源，比如在百度查询什么
# import requests
# kv={'key1':'value1','key2':'value2'}
# r=requests.request('GET','http://www.baidu.com',params=kv)
# print(r.url)

# data：字典，字节序列或文件，对象，向服务器提交资源时使用，比如账号和密码
# import requests
# kv={'key1':'value1','key2':'value2'}
# r=requests.request('POST','http://www.baidu.com',data=kv)
# body='主体内容'
# r=requests.request('POST','http://www.baidu.com',data=body)

# json：json格式数据
# headers：请求头，模拟浏览器
# hd = {'user-agent':'Chrome/10'}
# r=requests.request('POST','http://www.baidu.com',headers=hd)
# cookies auth files timeout proxies
# allow_redirects stream verify cert

"""                                    003    Beautiful Soup         """
"""
BeautifulSoup是个类  解析，遍历，维护“标签树”的功能库
BeautifulSoup对应一个HTML/XML文档的全部内容
soup = BeautifulSoup('<p>data</p>','html.parser')
解析器  html.parser(主要） lxml xml html5lib
"""
# from bs4 import BeautifulSoup
# import requests
# r = requests.get('http://python123.io/ws/demo.html')
# demo = r.text
# soup = BeautifulSoup(demo, "html.parser")
"""
BeautifulSoup类的基本元素  
标签 Tag：<p>..</p> <p class="title">...</p> 标签基本结构
名字 Name：标签的名字
属性 Attributes: 标签的属性
NavigableString: <>...</>中的字符串
Comment: 标签内字符串的注释部分
"""
"""
a标签：链接标签
"""
# print(soup)
# print(soup.prettify())
# print(soup.title)
# print(soup.a)
# print(soup.a.name)
# print(soup.a.parent.name)
# print(soup.p.parent.name)
# tag = soup.a
# print(tag.attrs) #返回一个字典
# print(tag.attrs['class'])
# print(soup.a.string)
# print(soup.p.string)


# a['href']
"""基于bs4库的HTML内容遍历方法"""
"""
下行遍历 上行遍历 平行遍历
"""
"""
下行遍历
.contents：子节点的列表，将<tag>所有儿子节点存入列表 返回列表
.children: 子节点的迭代类型，与.contents类似，用于循环遍历儿子节点
.descendants:子孙节点的迭代类型，包含所有子孙节点，用于循环遍历
"""
# print(soup.head.contents)
# print(len(soup.body.contents))
# print(soup.body.contents[1])
# for child in soup.body.children:
#     print(child)
"""
上行遍历
.parent:节点的父亲标签
.parents:节点先辈标签的迭代类型，用于循环遍历先辈节点
"""
# for parent in soup.a.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)
"""
平行遍历 发生在同一个父亲节点下
.next_sibling .previous_sibling .next_siblings .previous_siblings
"""

"""基于bs4库的HTML格式输出"""
# print(soup.prettify())

"""信息标记"""
"""
提取HTML中所有URL链接
思路：1）搜索到所有<a>标签 2）解析<a>标签格式，提取href后的链接内容
"""
# for link in soup.find_all('a'):
#     print(link.get('href'))
"""
基于bs4库的HTML内容查找方法

find('div',class_=..,name=..)
select('css选择器') 返回一个列表 >一个层级 " "多个层级

text/get_text() 获取标签下的所有内容
string 获取标签直属的内容

.find_all(name,attrs,recursive,string,**kwarg) 返回一个列表
name:对标签名称的检索字符串
attrs:对标签属性值的检索字符串，可标注属性检索
recursive:是否对子孙全部检索，默认为True
string:对字符串区域检索

<tag>(..)等价于<tag>.find_all(..)
soup(..)等价于soup.find_all(..)

常用扩展方法：
.find() .find_parents() .find_parents().........
"""
# print(soup.find_all('a'))
# print(soup.find_all(['a', 'b']))
# for tag in soup.find_all(True):
#     print(tag.name)
# print(soup.find_all('p', 'course'))
# print(soup.find_all(id='link1'))
# import re
# print(soup.find_all(id=re.compile('link')))
# print(soup.find_all('a', recursive=False))
# print(soup.find_all(string="Basic Python"))
# print(soup.find_all(string=re.compile('python')))
# print(soup('a'))


"""                         004  正则表达式       """

"""
正则表达式是用来简洁表达一组字符串的表达式  正则表达式主要应用在字符串匹配中  
编译：将符合正则表达式语法的字符串转换成正则表达式特征 p=re.compile(regex)
正则表达式语法由字符和操作符构成的
"""
"""
常用的操作符
. 表示任何单个字符（表示一个字符）
[ ] 字符集，对单个字符给出取值范围 [abc]表示a,b,c  [a-z]表示a到z单个字符
[^] 非字符集，对单个字符给出排除范围 [^abc]表示非a或b或c的单个字符
* 表示前一个字符0次或无限次扩展   abc*表示ab,abc,abcc,abccc等
+ 表示前一个字符1次或无限次扩展   abc+表示abc,abcc等
? 表示前一个字符0次或无限次扩展  abc？表示ab，abc
| 表示左右表达式任意一个 abc|def表示abc，def
{m} 扩展前一个字符m次 ab{2}c表示abbc
{m,n} 扩展前一个字符m至n次（含n） ab{1,2}c表示abc，abbc
^ 匹配字符串开头 ^abc表示abc且在一个字符串的开头
$ 匹配字符串结尾 abc$表示abc且在一个字符串的结尾
() 分组标记，内部只能使用|操作符 （abc）表示abc，（abc|def）表示abc，def
\d  数字，等价于[0-9]
\w 单词字符，等价于[A-Za-z0-9]
"""
"""re库的基本使用"""
"""
:re库采用raw string类型(原生字符串类型）表示正则表达式， 表示为：r'text'
原生字符串：不包含转义符
主要功能函数
re.search() 在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
re.match() 从一个字符串的开始位置起匹配正则表达式，返回match对象
re.findall() 搜索字符串，以列表类型返回全部能匹配的子串
re.split() 将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
re.finditer() 搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
re.sub() 在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
"""
# import re

# re.search(pattern,string,flags=0)
# match = re.search(r'[1-9]\d{5}', 'BIT 100081')
# if match:
#     print(match.group(0))

# re.match(pattern,string,flags=0)
# match = re.match(r'[1-9]\d{5}', 'BIT 100081')
# print(match.group(0))
# match = re.match(r'[1-9]\d{5}', '100081 BIT')
# print(match.group(0))

# re.findall(pattern,string,flags=0)
# ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
# print(ls)

# re.split(pattern,string,maxsplit=0,flags=0)
# ls = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084')
# print(ls)
# ls = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1)
# print(ls)

# re.finditer(pattern,string,flags=0)
# for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
#     if m:
#         print(m.group(0))

# re.sub(pattern,replace,string,count=0,flags=0)
# s = re.sub(r'[1-9]\d{5}', 'zipcode', 'BIT100081 TSU100084')
# print(s)

# regex = re.compile(pattern,flags=0) 将正则表达式的字符串形式编译成正则表达式对象
# pat = re.compile(r'[1-9]\d{5}')
# rst = pat.search('BIT 100081')
# print(rst.group(0))

"""match对象  一次匹配的结果 包含匹配的信息"""
# match = re.search(r'[1-9]\d{5}', 'BIT 100081')
# print(match.string)
# print(match.re)
# print(match.pos)
# print(match.endpos)
# print(match.group(0))
# print(match.start())
# print(match.end())
# print(match.span())

# Re库默认采用贪婪匹配，即输出匹配最长的子串
# match = re.search(r'PY.*N', 'PYANBNCNDN')
# print(match.group(0))
#输出最短的子串
# match = re.search(r'PY.*?N', 'PYANBNCNDN')
# print(match.group(0))

# 最小匹配操作符
# *?   +?    ??       {m,n}?

"""
group(0) 就是匹配正则表达式整体结果
group（1）列出第一个括号匹配部分 group（2）列出第2个括号匹配部分
"""
# import re
# content = 'Xiaoshuaib has 100 bananas'
# res = re.match('^Xi.*?(\d+)\s.*s$', content)
# print(res.group(1))
# content = """Xiaoshuaib has 100
# bananas"""
# res = re.match('^Xi.*?(\d+)\s.*s$', content,re.S)
# print(res.group(1))
# content = 'Xiaoshuaib has 100 bananas Xiaoshuaib has 200 bananas Xiaoshuaib has 300 bananas'
# res = re.findall('Xi.*?\d+\s.*?s', content)
# print(res)
# res = re.findall('Xi.*?(\d+)\s(.*?)s', content)
# print(res)

"""                              005 xpath   """
"""
原理：
1.实例化一个etree对象，将要解析的页面源码数据加载到该对象中
2.调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获

如何实例化一个etree对象: from lxml import etree 
1.e=etree.parse(filepath)
2.e=etree.HTML('page_text')

r=e.xpath('xpath表达式') 返回一个列表 元素为etree对象



--xpath表达式
标签定位 /html/head/title /html/body/div /html//div //div 
属性定位 //div[@class="..."] tag[@triName='..']
索引定位  //div[@class="..."]/p[3] 从1开始
/一个层级 //对个层级

取文本：../text()直系内容  ..//text()所有内容 
取属性值：img/@src

li.xpath('./a/text()')
"""

# 通用处理中文乱码的解决方案
# text=text.encode("iso-8859-1").decode("gbk")

"""               验证码              """
# 利用chaojiying.getCodeText()


"""               模拟登录                   """
"""
爬取某些用户的用户信息

点击登录按钮之后会发起一个post请求
post请求中会携带登录之前录入的相关的登录信息（用户名，密码，验证码....）
验证码：每次请求都会变化

"""
"""                 代理                  """
"""
代理：破解封IP这种反爬机制

代理：代理服务器

代理的作用：突破自身IP访问的限制 ， 隐藏自身真实IP 

相关网站：块代理 西祠代理 www.goubanjia.com

代理ip的类型：
--http 应用到http协议对应的url中
--https 应用到https协议对应的url中

proxies属性
proxies={"http(s)":"ip:port"}

代理ip的匿名度：
透明：服务器知道该次请求使用了代理，也知道请求对应的真实ip
匿名：知道使用了代理，不知道真实ip
高匿：不知道使用了代理
"""
"""                高性能异步爬虫               """
"""
异步爬虫方式：
多线程 ，多进程：
为相关阻塞的操作单独开启线程、进程，阻塞操作可以异步操作
线程池，进程池：

使用：
from multiprocessing.dummy import Pool
pool=Pool(4)
pool.map(function,list) 将list每一个元素传递给function进行处理 返回值为function的返回值列表
"""
"""                    异步爬虫 协程              """
"""

"""
"""                  selenium                     """
"""
selenium 与 爬虫
--便捷的获取网站中动态加载的数据
--便捷实现模拟登录

selenium模块：基于浏览器自动化的一个模块 控制浏览器自动化完成任务

selenium使用流程：
1.环境安装
2.下载浏览器的驱动程序


"""