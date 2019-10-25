import cv2

#
# img = cv2.imread('/Users/wangjinchao/Desktop/corner/10.png')
# img  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
import skimage.transform as st
import matplotlib.pyplot as plt
from skimage import data,feature

#使用Probabilistic Hough Transform.
# image = cv2.imread('/Users/wangjinchao/Desktop/corner/10.png')
# image  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# edges = feature.canny(image, sigma=2, low_threshold=1, high_threshold=25)
# lines = st.probabilistic_hough_line(edges, threshold=10, line_length=5,line_gap=3)
# print(len(lines))
# # 创建显示窗口.
# fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(16, 6))
# plt.tight_layout()
#
# #显示原图像
# ax0.imshow(image, plt.cm.gray)
# ax0.set_title('Input image')
# ax0.set_axis_off()
#
# #显示canny边缘
# ax1.imshow(edges, plt.cm.gray)
# ax1.set_title('Canny edges')
# ax1.set_axis_off()
#
# #用plot绘制出所有的直线
# ax2.imshow(edges * 0)
# for line in lines:
#     p0, p1 = line
#     ax2.plot((p0[0], p1[0]), (p0[1], p1[1]))
# row2, col2 = image.shape
# ax2.axis((0, col2, row2, 0))
# ax2.set_title('Probabilistic Hough')
# ax2.set_axis_off()
# plt.show()
#

# 一张图canny
# image = cv2.imread('/Users/wangjinchao/Desktop/corner/53.png')
image = cv2.imread('/home/wangjinchao/pred/53.png')
image  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges = feature.canny(image, sigma=2, low_threshold=1, high_threshold=25)
lines = st.probabilistic_hough_line(edges, threshold=10, line_length=5,line_gap=3)
print(len(lines))
# 创建显示窗口.
fig, (ax1) = plt.subplots(1, 1, figsize=(16, 6))
# fig, (ax1) = plt.subplots(1, 1, figsize=(16, 6))
plt.tight_layout()
#显示canny边缘
ax1.imshow(edges, plt.cm.gray)

# ax1.set_title('Canny edges')
# ax1.set_axis_off()
plt.axis('off')
plt.savefig("/home/wangjinchao/pred/examples.png")
# plt.savefig("/Users/wangjinchao/Desktop/corner/examples.jpg")
plt.show()

#
# import numpy as np
# import matplotlib.pyplot as plt
# from skimage import measure,draw
#
# import cv2
# img = cv2.imread("/Users/wangjinchao/Desktop/corner/examples.jpg")
# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #检测所有图形的轮廓
# contours = measure.find_contours(img, 0.5)
#
# #绘制轮廓
# fig, (ax0,ax1) = plt.subplots(1,2,figsize=(8,8))
# ax0.imshow(img,plt.cm.gray)
# ax1.imshow(img,plt.cm.gray)
# for n, contour in enumerate(contours):
#     ax1.plot(contour[:, 1], contour[:, 0], linewidth=2)
# ax1.axis('image')
# ax1.set_xticks([])
# ax1.set_yticks([])
# plt.show()

#  腐蚀
# import cv2
# import numpy as np
# img = cv2.imread('/Users/wangjinchao/Desktop/corner/53.png',0)
# kernel = np.ones((5,5),np.uint8)
# erosion = cv2.erode(img,kernel,iterations = 1)
# x = cv2.imwrite('/Users/wangjinchao/Desktop/corner/xx.png',erosion)

# 膨胀  可以消除块
# import cv2
# import numpy as np
# img = cv2.imread('/Users/wangjinchao/Desktop/corner/53.png',0)
# kernel = np.ones((5,5),np.uint8)
# dilation = cv2.dilate(img,kernel,iterations = 1)
# x = cv2.imwrite('/Users/wangjinchao/Desktop/corner/pz.png',dilation)
#


#先膨胀再腐蚀。它经常被用来填充前景物体中的小洞，或者前景物体上的小黑点。
# import cv2
# import numpy as np
# img = cv2.imread('/Users/wangjinchao/Desktop/corner/53.png',0)
# kernel = np.ones((5,5),np.uint8)
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# x = cv2.imwrite('/Users/wangjinchao/Desktop/corner/closing.png',closing)

