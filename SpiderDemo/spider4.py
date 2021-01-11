# json 套 json

import requests

def get(url,data):
    headers={
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    re=requests.post(url,data=data,headers=headers)
    obj=re.json()
    return obj

url="http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"

data={
    'on': 'true',
    'page': '1',
    'pageSize': '15',
    'productName': '',
    'conditionType': '1',
    'applyname': ''

}

idList=[]
for x in range(2):
    data['page']=str(x+1)
    obj = get(url,data)   
    for i in range(15):
        id=obj['list'][i]['ID']
        idList.append(id)



url="http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
data={
    'id':''
}
for i in range(30):
    data['id']=idList[i]
    obj=get(url,data)
    print(i+1,obj['epsName'],obj['businessPerson'])
    

