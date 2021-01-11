import time
from itsdangerous import TimedJSONWebSignatureSerializer as Se

secret_key='oweirnwert'
s=Se(secret_key,4)
data=s.dumps({'user_id':343})
token=data.decode()
print(token)

time.sleep(2)
secret_key='oweirnwert'
s=Se(secret_key)
data=s.loads(token)
print(data)