# 通过双目直接保存一个视频，并存储

import cv2
# 获取摄像头
cameraCapture = cv2.VideoCapture(1)
# cv2.namedWindow('cap', 0)
# cv2.resizeWindow('cap', 2560, 720)
# 设置每秒传输帧数
fps = 20
# size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
size = (2560,720)
print(size)
# 设置视频文件格式
# 视频编码类型
# cv2.VideoWriter_fourcc('X','V','I','D') MPEG-4 编码类型
# cv2.VideoWriter_fourcc('I','4','2','0') YUY编码类型
# cv2.VideoWriter_fourcc('P','I','M','I') MPEG-1 编码类型
# cv2.VideoWriter_fourcc('T','H','E','O') Ogg Vorbis类型，文件名为.ogv
# cv2.VideoWriter_fourcc('F','L','V','1') Flask视频，文件名为.flv
# # fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# # fourcc = cv2.VideoWriter_fourcc(*'mpeg')

vw = cv2.VideoWriter('./chess.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, size)
# 读取摄像头的图像，函数 isOpened 判断摄像头是否开启，返回布尔型
# if cameraCapture.isOpened():
#     success, frame = cameraCapture.read()
    # # 若有多个摄像头，可使用
    # success = cameraCapture.grab()
    # success, frame = cameraCapture.retrieve()
num = 100 * fps
print('start')
while cameraCapture.isOpened() and num>0:
    # 读取摄像头的图像
    success, frame = cameraCapture.read()
    # 显示摄像头录制窗口
    cv2.namedWindow('cap',1)
    cv2.resizeWindow('cap',1280,360)
    cv2.imshow('cap',frame)
    # 写入图像到视频文件
    vw.write(frame)

    # # 若有多个摄像头，可使用
    # success = cameraCapture.grab()
    # success, frame = cameraCapture.retrieve()
    num -= 1
    if cv2.waitKey(30) & 0xFF == ord('q'):
         break
print('end')
# 释放摄像头
cameraCapture.release()
# 注销录制窗口
cv2.destroyWindow('cap')







