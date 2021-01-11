# 1.获取图片 生成级联分类器对象 包含了人脸的特征数据 用于匹配
# 2.将img（numpy数组）与特征数据进行匹配 找到人脸
# 3.标记人脸
import cv2
# cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 转为灰度
# face_obj=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 生成级联分类器对象
# faces=face_obj.detectMultiScale(img,scaleFactor=1.05,minNeighbors=5) 匹配特征 返回一个数组
# scaleFactor:每次图像缩小的比例 minNeighbors :每一个目标至少检测多少次
# 遍历faces for x,y,w,h in faces: xy左上角坐标 wh宽高
# img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) 画矩形

def faceMatch(str,a=1.05,b=5):
    img=cv2.imread(str)
    img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_obj=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces=face_obj.detectMultiScale(grayImg,scaleFactor=a,minNeighbors=b)
    for x,y,w,h in faces:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("yang",img)
    cv2.waitKey(0)

# faceMatch("15.jpg",1.05,3)
# faceMatch("yang.jpg",1.05,5)
faceMatch("curry.jpg",1.07,7)
# faceMatch("f.jpg",1.10,3)
