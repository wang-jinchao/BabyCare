#coding=utf-8
import cv2
import sys
import MRange
from decimal import Decimal
import numpy as np
import os
import time

#  将480*360转为1280*720尺寸
def trans(corX, corY) :
    return corX * 8 / 3, corY * 2


def realdistance(ta, tb) :
    vector1 = np.array(ta)
    vector2 = np.array(tb)
    op = np.sqrt(np.sum(np.square(vector1 - vector2)))
    return op

def resize(dir_path,ter_path):
    for filename in os.listdir(dir_path):
        # If the images are not .JPG images, change the line below to match the image type.
        # if filename.endswith(".png"):
        if filename.endswith("left_cam.png"):
            name = os.path.join(dir_path,filename) #要resize的图像的名字
            image = cv2.imread(name)
            resized = cv2.resize(image,(480,360), interpolation = cv2.INTER_CUBIC)
            re_dir_path = os.path.join(ter_path, 'Resize'+filename)
            print(re_dir_path)
            cv2.imwrite(re_dir_path,resized)


if __name__ == '__main__' :
    path = '/Users/wangjinchao/project/PycharmProjects/Paper/master/STERO/'
    testpath = '/Users/wangjinchao/segnet/data/CamVid/test'
    width = 2560
    height = 720

    #读取视频图片，以创建时间排序
    picpath = '/Users/wangjinchao/Pictures/Screenshots/'
    a = os.listdir(picpath)
    dir_list = sorted(a, key=lambda x : os.path.getmtime(os.path.join(picpath, x)), reverse=True)
    if dir_list[0].endswith('.png') :
        img_dir = os.path.join(picpath, dir_list[0])
    else :
        img_dir = os.path.join(picpath, dir_list[1])

    # img_dir = '/Users/wangjinchao/Pictures/Screenshots/t30_f15_t3-0001.png'
    img = cv2.imread(img_dir)


    # 对影像进行拆分，左右影像
    right_cam = img[:, :int(width / 2), :]
    left_cam = img[:, int(width / 2) :, :]
    # 分别显示
    # cv2.imshow("left_cam", left_cam)
    # cv2.imshow("right_cam", right_cam)
    cv2.imwrite(path + 'left_cam.png', left_cam)
    cv2.imwrite(path + 'right_cam.png', right_cam)
    resize(path, testpath)
    # cv2.waitKey(0)
    # 注销录制窗口
    # cv2.destroyWindow('left_cam')
    # cv2.destroyWindow('right_cam')
    os.system('python model.py')

    #   像素距离
    img = cv2.imread("/Users/wangjinchao/project/PycharmProjects/Paper/master/eval/model-20000/pred/1.png", 1)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # gray = cv2.GaussianBlur(gray, (111,111), 0)

    redLower = np.array([0, 43, 46])
    redUpper = np.array([179, 255, 255])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, redLower, redUpper)
    ret, thresh = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)

    # bitwiseNot = cv2.bitwise_not(gray)
    # ret, thresh = cv2.threshold(bitwiseNot, 222, 251, cv2.THRESH_BINARY)
    image, contours, hierarchy = cv2.findContours(thresh, 2, 1)

    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(thresh, kernel, iterations=1)
    image, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print(len(contours))
    cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

    rate = 0.001
    edges = cv2.Canny(img, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 91)  # 这里对最后一个参数使用了经验型的值
    result = img.copy()

    hull = cv2.convexHull(contours[0])
    # print(len(hull))
    epsilon = rate * cv2.arcLength(hull, True)
    hull = cv2.approxPolyDP(hull, epsilon, True)
    M = cv2.moments(hull)  # 质心
    # print(M,type(M))
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])

    print('质心在480*360图像的坐标为：(%d,%d)' % (cx, cy))
    centroids = trans(cx, cy)
    centroids = list(map(int, centroids))
    print('质心在1280*720图像的坐标为:' + str(centroids))

    # matlab 返回世界坐标，fdx
    Tdcor, fdx = MRange.Height(centroids)
    worldH = Tdcor[2]
    print('高度为：', worldH)

    # print(len(hull),'3232')
    length = len(hull)

    # for line in lines:
    #     print('---', line)
    min = result.shape[1]

    for idx in range(length) :
        i = tuple(hull[idx][0])
        j = tuple(hull[(idx + 1) % length][0])
        cv2.line(result, i, j, (10, 155, 60), 1, cv2.LINE_AA)
        for line in lines :
            rho = line[0][0]  # 第一个元素是距离rho
            theta = line[0][1]  # 第二个元素是角度theta
            pt1 = (int(rho / np.cos(theta)), 0)
            pt2 = (int((rho - result.shape[0] * np.sin(theta)) / np.cos(theta)), result.shape[0])

            # pt1 = (np.float32(rho / np.cos(theta)), 0)
            # pt2 = (np.float32(rho - result.shape[0] * np.sin(theta) / np.cos(theta)), result.shape[0])

            cv2.line(result, pt1, pt2, (255), 1, cv2.LINE_AA)

            dis = np.abs(np.cos(theta) * i[0] + np.sin(theta) * i[1] - rho)
            if dis < min :
                min = dis
                ll = [rho, theta]
                hullpoint = i
                lc = np.cos(ll[1])
                ls = np.sin(ll[1])
                xx = lc * ll[0] - lc * ls * np.float32(hullpoint[1]) + ls * ls * np.float32(hullpoint[0])
                if theta == 0 :
                    yy = hullpoint[1]
                else :
                    yy = -xx * lc / ls + ll[0] / ls
                linepoint = (xx, yy)
                min_X = np.abs(hullpoint[0] - linepoint[0])
                min_Y = np.abs(hullpoint[1] - linepoint[1])

    cv2.line(result, hullpoint, linepoint, (206,13,244), 2, cv2.LINE_AA)
    cv2.circle(result, (cx, cy), 10, (0, 0, 0), 14)
    hull_M = (hullpoint[0], hullpoint[1])
    linepoint_M = (linepoint[0], linepoint[1])
    print('最小距离坐标点为：%s, %s' % (hull_M, linepoint_M))
    print('min_X', min_X)  # X方向最小长度
    print('min_Y', min_Y)  # Y方向最小长度
    print('最小距离', min)  # 最小距离

    print('==' * 12)
    # 转换后的各方向长度
    minTrans = trans(min_X, min_Y)
    distance = realdistance(minTrans, [0, 0])

    print('distance:', distance)
    print('fdx', fdx)
    wordL = 100*distance*worldH/fdx
    wordL = Decimal(wordL).quantize(Decimal("0.000"))
    print(wordL)

    cv2.rectangle(result, (345, 10), (475, 70), (200, 100, 30),1)
    cv2.putText(result, 'The Minimum Distance:', (345, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), lineType=cv2.LINE_AA)
    cv2.putText(result, '   '+str(wordL)+'cm', (350, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (300, 200, 30), lineType=cv2.LINE_AA)
    cv2.imshow('Result', result)
    cv2.waitKey(0)
    cv2.imwrite(str(time.time())+'.png',result)
    cv2.destroyAllWindows()
