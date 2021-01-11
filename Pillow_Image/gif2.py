import os
import imageio
# imageio.mimwrite()

List=os.listdir('gif')
imgList=[]
for name in List:
    img=imageio.imread(f"gif/{name}")
    imgList.append(img)

imageio.mimwrite('yang.gif',imgList,duration=0.15)