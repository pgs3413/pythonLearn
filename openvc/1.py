import cv2
#cv2.imread(路径名，像素模式) 1 彩色 0 灰色 -1 alpha通道
# img.shape 返回一个元祖(height,width)
# cv2.imshow(name,img)
# cv2.imwrite(路径名，img)
# cv2.waitKey(0) 返回按键的ASCII码
# cv2.destroyWindow(name) cv2.destroyAllWindow()
# cv2.resize(img,(width,height))
#   
img=cv2.imread("yang.jpg",0)
# print(img.shape)
img=cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4)))
cv2.imshow("yang",img)
key=cv2.waitKey(0)
if key==115:
    cv2.imwrite("yang_grey2.jpg",img)
    cv2.destroyWindow("yang")
