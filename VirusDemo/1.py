from wx import *
from _thread import start_new_thread
from time import sleep

app=App()
app.MainLoop()

i=2

def virus():
    global i
    i+=1
    if i%2==0:
        MessageBox("这是一个句子","警告",OK|ICON_WARNING)
    else:
        MessageBox("这也是一个句子","错误",OK|ICON_ERROR)

while True:
    start_new_thread(virus,())
    sleep(0.4)