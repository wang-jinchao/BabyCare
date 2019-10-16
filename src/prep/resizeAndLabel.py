from PIL import Image
import os.path
import glob


def convertjpg(jpgfile, outdir, width=480, height=360):
    img = Image.open(jpgfile)
    new_img = img.resize((width, height), Image.NEAREST)
    # 采用最近邻算法进行缩放，主要是保证灰度化后不同类之间的灰度值差异大
    outdir1 = os.path.join(outdir, os.path.basename(jpgfile))
    outdir2 = outdir1.split('.')
    new_img.save(outdir2[0]+'.png')  # 将图像保存为.png格式
    print(outdir2[0])


for jpgfile in glob.glob("/Users/wangjinchao/Desktop/first/trainannot/*.png"):
    convertjpg(jpgfile, '/Users/wangjinchao/Desktop/first/trainannot')
#######
# from PIL import Image
# import numpy as np
# import os.path
# import glob
#
# def convert_gray(pngfile):
#     img=Image.open(pngfile).convert('L')
#     img.save(pngfile)
#
# for pngfile in glob.glob('/Users/wangjinchao/Projects/PycharmProjects/Paper/data/trainannot/*.png'):
#     convert_gray(pngfile)
####
#
#
# from PIL import Image
# from pylab import *
# import numpy
# import glob
# import os.path
#
#
# def convert(pngfile):
#     im = array(Image.open(pngfile))
#     w = im.shape[0]
#     h = im.shape[1]
#     for x in range(w):
#         for y in range(h):
#             if im[x][y] >= 200 and im[x][y] < 254:  # 背景
#                 im[x][y] = 0
#             elif im[x][y] >= 140 and im[x][y] < 200:  # baby
#                 im[x][y] = 1
#             else:
#                 im[x][y] = 2                # bed
#
#     img = Image.fromarray(im.astype('uint8'))
#     img.save(pngfile)
#
# for pngfile in glob.glob('/Users/wangjinchao/Projects/PycharmProjects/Paper/data/trainannot/*.png'):
#     convert(pngfile)
