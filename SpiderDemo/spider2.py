# 破解有道翻译(ajax请求)
# post请求
# 返回一个json数据

import requests

# post(url,data,json,**kw)
url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
word=input("请输入：")
data={
    'i':word,
    'doctype': 'json'
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
response=requests.post(url,data=data,headers=headers)

# json()返回一个json对象（字典）

obj=response.json()
print("结果为",obj['translateResult'][0][0]['tgt'])

