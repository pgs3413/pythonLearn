import os

filesize=50*1024*1024
for root,dirs,files in os.walk("C:\\Users"):
    for file in files:
        filename=os.path.join(root,file)
        if not os.path.isfile(filename):
            continue
        size=os.path.getsize(filename)
        if(size>filesize):
            size=size//(1024*1024)
            size=f"{size}M"
            print(filename,size)
    