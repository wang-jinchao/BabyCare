# matlab的方法如下
'''
J = (checkerboard(300,3,4)>0.5);   %生成黑白棋盘图像
figure, imshow(J) %显示黑白棋盘图像
imwrite(J,'plate.jpg');%保存黑白棋盘图像
'''

import cv2
import numpy as np

width = 1000*5
height = 700*5
length = 100*5

image = np.zeros((width,height),dtype = np.uint8)
print(image.shape[0],image.shape[1])

for j in range(height):
    for i in range(width):
        if((int)(i/length) + (int)(j/length))%2:
            image[i,j] = 255;
cv2.imwrite("/Users/wangjinchao/project/PycharmProjects/Paper/cal/ch2ess.jpg",image)
# cv2.imshow("chess",image)
# cv2.waitKey(0)