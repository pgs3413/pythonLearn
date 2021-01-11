import asyncio
import time

# 把会阻塞的代码封装成协程函数，用await挂起阻塞语句
async def func(url):
    print("正在下载",url)
    await asyncio.sleep(2)
    print("下载完成",url)

urls=["www.baidu.com","www.sogou.com","www.google.com"]


task_list=[]

for url in urls:
    c=func(url)#生成协程函数
    task=asyncio.ensure_future(c)#封装成任务对象
    task_list.append(task)#生成任务队列

# 生成事件循环对象
loop=asyncio.get_event_loop()

start=time.time()
# 把任务队列注册到事件循环对象中
loop.run_until_complete(asyncio.wait(task_list))
print(time.time()-start)