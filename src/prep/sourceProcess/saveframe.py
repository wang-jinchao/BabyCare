# -*- coding:utf8 -*-
# 将视频切片 每帧
import cv2
import os
import shutil

# 视频文件名字
filename = '/Users/wangjinchao/project/PycharmProjects/Paper/prep/sourceProcess/2r.avi'

# 保存图片的路径
savedpath = '/Users/wangjinchao/Desktop/ste/rr/'
# print(savedpath)
# isExists = os.path.exists(savedpath)
# if not isExists:
#     os.makedirs(savedpath)
#     print('path of %s is build' % (savedpath))
# else:
#
#     os.makedirs(savedpath)
#     print('path of %s already exist and rebuild' % (savedpath))
#

# 保存图片的帧率间隔
count = 1

# 开始读视频
videoCapture = cv2.VideoCapture(filename)
i = 0
j = 0

while True:
    success, frame = videoCapture.read()
    i += 1
    if (i % count == 0):
        # 保存图片
        j += 1
        # savedname = filename.split('.')[0] + '_' + str(j) + '_' + str(i) + '.jpg'

        savedname ='2r' + str(i) + '.png'

        cv2.imwrite(savedpath + savedname, frame)
        print('image of %s is saved' % (savedname))
    if not success:
        print('video is all read')
        break

videoCapture.release()