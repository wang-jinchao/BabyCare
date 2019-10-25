# import os
# import cv2
#
# # 重命名等操作
# picpath = '/Users/wangjinchao/Desktop/show/resss/'
# zz = '/Users/wangjinchao/Desktop/show/pp/'
# a = os.listdir(picpath)
# dir_list = sorted(a, key=lambda x: int(x.split('.')[0]))
# print(dir_list)
#
# # dir_list = sorted(a, key=lambda x : os.path.getmtime(os.path.join(picpath, x)))
# for i in range(len(a)):
#     # if picpath[i].endswith('.png') and i%2==1:
#     img_dir = os.path.join(picpath, dir_list[i])
#     os.renames(img_dir,zz+str(i*2)+'.png')
#
# print(len(a))
#

# pic转视频
import cv2
import os
import numpy as np
picpath = '/Users/wangjinchao/Desktop/show/pic/'
piccon = '/Users/wangjinchao/Desktop/show/xx/'
a = os.listdir(picpath)
# print(a[1].split('.')[0])
dir_list = sorted(a, key=lambda x: int(x.split('.')[0]))
c= os.listdir(piccon)
dir_ll = sorted(c, key=lambda x: int(x.split('.')[0]))
print(dir_list)
print(dir_ll)

fps = 20

size = (960*3,540)
# size = (2560, 720)
vw = cv2.VideoWriter('./result.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, size)

print('start')
num = 0
while num < 298:
    pp = picpath+str(num)+'.png'
    seg = piccon+str(num)+'.png'

    framel = cv2.imread(pp)
    framer = cv2.imread(seg)
    imgl = cv2.resize(framel, (1920, 540))
    imgr = cv2.resize(framer, (960, 540))
    frame = np.concatenate((imgl, imgr),axis=1)
    # frame = cv2.hconcat([imgl, imgr])
    # frame = np.zeros((540, 2880, 3), np.uint8)
    # # # 写入图像到视频文件
    # frame[:, :int(1920), :] = imgl
    # frame[:, int(1920) :, :] = imgr
    vw.write(frame)
    num += 1
vw.release()

print('end')








