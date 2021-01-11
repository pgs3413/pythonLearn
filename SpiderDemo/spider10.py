# 代理


import requests
import re


url="http://www.data5u.com/"
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
response=requests.get(url,headers=headers)
print(response.status_code)
page_text=response.text

reg='<ul class="l2">(.*?) </ul>'
ul_list=re.findall(reg,page_text,re.S)
# print(ul_list)
ip_list=[]
for ul in ul_list:
    list1=[]
    reg='<span style=.*?><li>([a-z]*?)</li></span>'
    type1=re.search(reg,ul)
    type2=type1.group(1)
    if type2=='https':
        list1.append(type2)
        reg='<span><li>([\.|\d]*?)</li></span> '
        ip=re.search(reg,ul)
        list1.append(ip.group(1))
        reg='<span style.*?><li class.*?>(.*?)</li></span>'
        port=re.search(reg,ul)
        list1.append(port.group(1))
        ip_list.append(list1)
    


url="https://www.baidu.com/s?wd=ip"

for ip in ip_list:
    s="https://"+ip[1]+":"+ip[2]
    proxies={
    "https":s
    }
    try:
        re=requests.get(url,headers=headers,proxies=proxies)
        print(re.status_code)
    except Exception as e:
        pass
    else:
        with open("ip.html","w",encoding="utf-8") as f:
            f.write(re.text)
        print("success!")
        break



