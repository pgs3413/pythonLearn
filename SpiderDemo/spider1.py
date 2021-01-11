# 网页采集器

from requests import *

# get(url,params=None,**kwargs)
url="http://www.baidu.com/s"
params={'wd':'中国'}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
}
response=get(url=url,params=params,headers=headers)
# print(response.url)
t=response.text
with open("1.txt","w",encoding="utf-8") as f:
    f.write(t)
