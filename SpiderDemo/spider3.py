# 爬取豆瓣电影（ajax请求）

# import requests
# url = 'https://movie.douban.com/j/new_search_subjects?'
# params={
#     'sort': 'U',
#     'range': '0,10',
#     'tags': '',
#     'start': '0',
#     'genres': '喜剧'
# }
# headers={
#    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
# }
# for x in range(5):
#     count=x*20
#     params['start']=str(count)
#     response=requests.get(url,params=params,headers=headers)
#     obj=response.json()
#     with open("douban.txt",'a',encoding='utf-8') as f:
#         for y in range(20):
#             f.write(str(x*20+y+1)+" "+obj['data'][y]['title']+" "+obj['data'][y]['rate']+"\n")
# print(obj['data'][0]['title'],obj['data'][0]['rate'])


# 爬取kfc
import requests
import json
url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
data={
    'cname': '',
    'pid':'',
    'keyword': '北京',
    'pageIndex': '1',
    'pageSize': '10'
}
headers={
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
response=requests.post(url,data=data,headers=headers)
# print(response.text)
obj=json.loads(response.text)
for i in range(10):
    print(str(i+1)+" "+obj["Table1"][i]['storeName'])