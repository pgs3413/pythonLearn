# 模拟登录古诗文网
# 1.验证码识别
# 2.发送post请求（携带相应参数）
# 3.保存响应数据

# 模拟登录人人网
import requests
from bs4 import BeautifulSoup
import chaojiying
import json

session=requests.Session()
url="http://www.renren.com/"
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
main_text=session.get(url,headers=headers).text
soup=BeautifulSoup(main_text,"lxml")
img_src=soup.find("img",id="verifyPic_login")["src"]
# print(img_src)
img=session.get(img_src,headers=headers).content
with open("a.jpg","wb") as f:
    f.write(img)
post_url="http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=202085110108"

codeText=chaojiying.getCodeText("a.jpg",1902)

data={
    'email': 'www.zhangbowudi@qq.com',
    'icode':codeText,
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': "6cc43fc30ade20f0740892610fad005c9696c9809329279c1985dc4cd8ab591f",
    'rkey': "3d1f9abdaae1f018a49d38069fe743c8"

}
response=session.post(post_url,data=data,headers=headers)
print(response.status_code)
text=json.loads(response.text)
per_url=text["homeUrl"]
# print(per_url)
re=session.get(per_url,headers=headers)
print(re.status_code)
# with open("renren.html","w",encoding="utf-8") as f:
#     f.write(re.text)
# fri_url="http://friend.renren.com/managefriends"
# re=session.get(fri_url,headers=headers)
# print(re.status_code)
# with open("renren2.html","w",encoding="utf-8") as f:
#     f.write(re.text)
geren_url="http://www.renren.com/289676607/profile"
re=session.get(geren_url,headers=headers)
print(re.status_code)
with open("renren3.html","w",encoding="utf-8") as f:
    f.write(re.text)



#模拟登录古诗文网
# import requests
# from bs4 import BeautifulSoup
# import chaojiying

# session=requests.Session()

# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
# }

# url="https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"

# main_text=session.get(url,headers=headers).text
# soup=BeautifulSoup(main_text,"lxml")
# img_src="https://so.gushiwen.cn"+soup.find("img",id="imgCode")['src']
# img=session.get(img_src,headers=headers).content
# with open("a.jpg","wb") as f:
#     f.write(img)

# __VIEWSTATE=soup.find("input",id="__VIEWSTATE")['value']
# __VIEWSTATEGENERATOR=soup.find("input",id="__VIEWSTATEGENERATOR")["value"]

# post_url="https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"

# codeText=chaojiying.getCodeText("a.jpg",1902)

# data={
#     '__VIEWSTATE': __VIEWSTATE,
#     '__VIEWSTATEGENERATOR':__VIEWSTATEGENERATOR,
#     'from': 'http://so.gushiwen.cn/user/collect.aspx',
#     'email': '13070230452',
#     'pwd': 'pgs990525',
#     'code': codeText,
#     'denglu': '登录'
# }
# response=session.post(post_url,data=data,headers=headers)
# print(response.status_code)
# per_text=response.text
# with open("gushiwen.html","w",encoding="utf-8") as f:
#     f.write(per_text)
 
