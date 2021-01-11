from PIL import Image
# open new paste crop save

image=Image.open("yang.jpg")
width,height=image.size
size=max(width,height)
new_image=Image.new(image.mode,(size,size),color="white")
if width>height:
    new_image.paste(image,(0,int((size-width)/2)))
else:
    new_image.paste(image,(int((size-height)/2),0))

width,height=new_image.size
image_list=[]
one=int(width/3)
for x in range(3):
    for y in range(3):
        left=x*one
        right=(x+1)*one
        upper=y*one
        lower=(y+1)*one
        image_list.append(new_image.crop((left,upper,right,lower)))
for index,image in enumerate(image_list):
    image.save(f"{index+1}.jpg")

print("success!")        
