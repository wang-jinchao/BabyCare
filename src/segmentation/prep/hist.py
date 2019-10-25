# #encoding:utf-8
#
# #
# #灰度图像直方图
# #
#
# from matplotlib import pyplot as plt
# import cv2
#
# image = cv2.imread("/Users/wangjinchao/Desktop/img/3.png")
# cv2.imshow("Original",image)
#
# #图像直方图
# hist = cv2.calcHist([image],[0],None,[256],[-10,256])
#
# plt.figure()#新建一个图像
# plt.title("Grayscale Histogram")#图像的标题
# plt.xlabel("Bins")#X轴标签
# plt.ylabel("# of Pixels")#Y轴标签
# plt.plot(hist)#画图
# plt.xlim([0,256])#设置x坐标轴范围
# plt.show()#显示图像


from matplotlib import pyplot as plt
import cv2
import numpy as np

img = cv2.imread('/Users/wangjinchao/Desktop/img/2.png')

chans = cv2.split(img)
colors = ('b', 'g', 'r')

plt.figure()
plt.title("’Flattened’ Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)
    plt.xlim([0, 256])
plt.show()