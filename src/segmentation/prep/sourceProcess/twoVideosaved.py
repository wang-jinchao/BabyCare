# coding=utf-8
#用来将摄像头的画面分成两个视频并存储起来。


import cv2
import sys


if __name__ == '__main__':
    # cv2.namedWindow('cap', 0)
    # cv2.resizeWindow('cap', 900, 300)

    cap = cv2.VideoCapture('/Users/wangjinchao/project/PycharmProjects/Paper/prep/sourceProcess/2.avi')
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = 20
    size = (int(width/2),int(height))
    # size= (width,height)
    print(size)
    # v = cv2.VideoWriter('/home/wangjinchao/code/video/source/1l.avi',cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)
    # w = cv2.VideoWriter('/home/wangjinchao/code/video/source/1r.avi',cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)
    # fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G' )
    v = cv2.VideoWriter('/Users/wangjinchao/project/PycharmProjects/Paper/prep/sourceProcess/2l.avi', fourcc, fps, size)
    w = cv2.VideoWriter('/Users/wangjinchao/project/PycharmProjects/Paper/prep/sourceProcess/2r.avi', fourcc, fps, size)

    ret =True
    count = 0
    while count<500:
        ret, frame = cap.read()
        print(ret)
        print(count)
        left_cam = frame[:, :int(width / 2), :]
        right_cam = frame[:, int(width / 2):, :]
        print(left_cam.ndim)
        print(left_cam.shape)
        print(left_cam.size)
        print(left_cam.dtype)
        w.write(left_cam)
        v.write(right_cam)

        count=count + 1

    print("ffff")
    cap.release()
    v.release()
    w.release()
