from PIL import Image

def fill_img_with_img(imgParent,imgChild):
    imgSize=(imgParent.width*imgChild.width,imgParent.height*imgChild.height)
    imgRet=Image.new("L",imgSize,"white")
    for w in range(imgParent.width):
        for h in range(imgParent.height):
            if imgParent.getpixel((w,h))<127:
                imgRet.paste(imgChild,(w*imgChild.width,h*imgChild.height))

    return imgRet


imgParent=Image.open("1.jpg")
imgParent=imgParent.convert('L')

imgChild=Image.open("1.jpg")
imgChild=imgChild.convert('L')

imgRet=fill_img_with_img(imgParent,imgChild)

imgRet.save("2.png")
