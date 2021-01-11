from PIL import Image
image=Image.open("gif/40.jpg")
blankW=500
blankH=500

def fill_image(img):
    newImg=Image.new("RGB",(blankW,blankH),color="white")
    w,h=img.size
    newImg.paste(img,(int((blankW-w)/2),int(blankH-h)))
    return newImg

if __name__=='__main__':
    for i in range(1,30):
        resizeW=int(image.size[0]*i/30)
        resizeH=int(image.size[1]*i/30)
        img=image.resize((resizeW,resizeH))
        img=fill_image(img)
        img.save(f"gif/{i+10}.jpg")


