from PIL import Image 
import random
im = Image.open('./org-s.bmp')
#im = Image.open('./org.bmp')


def isVaildColor(color):
    return color!=(102,102,102) and color!=(153,204,255)

def randMapColor():
    color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    while(not isVaildColor(color)):
        color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    return color

def MapColorP(color):
    r=color[0]
    g=color[1]
    b=color[2]+1
    if b>255:
        b=0
        g=g+1
        if g>255:
            g=0
            r=r+1
            print("红色进位")
            if r>255:
                print("颜色不够用")
                r=0
    color=(r,g,b)

    if isVaildColor(color):
        return color
    else:
        return MapColorP(color,1)

print("-------------------------------处理中----------------------------------")
color=(0,0,0)
color=MapColorP(color)

colorList=[]

colorDir={}
colorFatherDir={}
colorDir[color]=()
colorDir[color]+=(color,)
for i in range(im.size[0]):
    if isVaildColor(im.getpixel((i,0))):
        im.putpixel((i,0),color)
    else:
        color=MapColorP(color)
        colorDir[color]=()
        colorFatherDir[color]=color

for j in range(1,im.size[1]):
    if isVaildColor(im.getpixel((0,j))):
        if isVaildColor(im.getpixel((0,j-1))):
            colorMate=im.getpixel((0,j-1))
            im.putpixel((0,j),colorMate)
        else:
            color=MapColorP(color)
            colorDir[color]=()
            colorFatherDir[color]=color
            im.putpixel((0,j),color)
    for i in range(1,im.size[0]):
        if isVaildColor(im.getpixel((i,j))):
            if isVaildColor(im.getpixel((i,j-1))):
                colorMate=im.getpixel((i,j-1))
                im.putpixel((i,j),colorMate)
                #归属集处理
                #colorDir[im.getpixel((i,j))]=colorMate
                if isVaildColor(im.getpixel((i-1,j))):
                    #if im.getpixel((i-1,j)) in colorDir and colorDir[im.getpixel((i-1,j))]!=im.getpixel((i-1,j)):
                    if colorFatherDir[im.getpixel((i,j))]!=colorFatherDir[im.getpixel((i-1,j))]:
                        colorDir[colorFatherDir[im.getpixel((i-1,j))]]=colorDir[colorFatherDir[im.getpixel((i,j))]]+colorDir[colorFatherDir[im.getpixel((i-1,j))]]
                        del colorDir[colorFatherDir[im.getpixel((i,j))]]
                        colorFatherDir[im.getpixel((i-1,j))]=colorFatherDir[im.getpixel((i,j))]
                    #colorFatherDir[im.getpixel((i,j))]=colorFatherDir[im.getpixel((i-1,j))]
                #    if colorDir[im.getpixel((i-1,j))]!=im.getpixel((i-1,j)):
                #        colTmp=colorDir[im.getpixel((i-1,j))]
                #        colorDir[im.getpixel((i-1,j))]=colorDir[im.getpixel((i,j))]
                #        colorDir[colTmp]=colorDir[im.getpixel((i,j))]
                #    else:
                #        colorDir[im.getpixel((i-1,j))]=colorDir[im.getpixel((i,j))]

            elif isVaildColor(im.getpixel((i-1,j))):
                colorMate=im.getpixel((i-1,j))
                im.putpixel((i,j),colorMate)
            else:
                color=MapColorP(color)
                colorDir[color]=()
                colorFatherDir[color]=color
                im.putpixel((i,j),color)
#for j in range(1,im.size[1]):
#    for i in range(1,im.size[0]):
#        if isVaildColor(im.getpixel((i,j))):
#            #print(colorDir[im.getpixel((i,j))])
#            #if colorDir.has_key(im.getpixel((i,j))):
#            if im.getpixel((i,j)) in colorDir:
#                im.putpixel((i,j),colorDir[im.getpixel((i,j))])
#            else:
#                print("不存在颜色的值(",i,",",j,")")
im.show()
im.save("./tmp.bmp","BMP") #保存图像为gif格式




