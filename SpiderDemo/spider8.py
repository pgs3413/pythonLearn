# 验证码识别
import requests
import chaojiying

url="https://so.gushiwen.cn/RandCode.ashx?t=1599137306043"
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
img=requests.get(url,headers=headers).content
with open('a.jpg','wb') as f:
    f.write(img)

result=chaojiying.getCodeText('a.jpg',1902)
print(result)