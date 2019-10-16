import numpy as np
import cv2
import camera_configs

cv2.namedWindow("left")
cv2.namedWindow("right")
cv2.namedWindow("depth")
cv2.moveWindow("left", 0, 0)
cv2.moveWindow("right", 600, 0)
cv2.createTrackbar("num", "depth", 0, 10, lambda x: None)
cv2.createTrackbar("blockSize", "depth", 5, 255, lambda x: None)
# camera1 = cv2.VideoCapture(0)
# camera2 = cv2.VideoCapture(1)

# 添加点击事件，打印当前点的距离
def callbackFunc(e, x, y, f, p):
    if e == cv2.EVENT_LBUTTONDOWN:
        print(threeD[y][x])

cv2.setMouseCallback("depth", callbackFunc, None)

# while True:
    # ret1, frame1 = camera1.read()
    # ret2, frame2 = camera2.read()
    # 
    # if not ret1 or not ret2:
    #     break
frame1 = cv2.imread('/Users/wangjinchao/project/PycharmProjects/Paper/master/left.png')
frame2 = cv2.imread('/Users/wangjinchao/project/PycharmProjects/Paper/master/right.png')
# 根据更正map对图片进行重构
img1_rectified = cv2.remap(frame1, camera_configs.left_map1, camera_configs.left_map2, cv2.INTER_LINEAR)
img2_rectified = cv2.remap(frame2, camera_configs.right_map1, camera_configs.right_map2, cv2.INTER_LINEAR)

# 将图片置为灰度图，为StereoBM作准备
imgL = cv2.cvtColor(img1_rectified, cv2.COLOR_BGR2GRAY)
imgR = cv2.cvtColor(img2_rectified, cv2.COLOR_BGR2GRAY)

# 两个trackbar用来调节不同的参数查看效果
num = cv2.getTrackbarPos("num", "depth")
blockSize = cv2.getTrackbarPos("blockSize", "depth")
if blockSize % 2 == 0:
    blockSize += 1
if blockSize < 5:
    blockSize = 5

# 根据Block Maching方法生成差异图（opencv里也提供了SGBM/Semi-Global Block Matching算法，有兴趣可以试试）
stereo = cv2.StereoBM_create(numDisparities=16*num, blockSize=blockSize)
disparity = stereo.compute(imgL, imgR)

disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
# 将图片扩展至3d空间中，其z方向的值则为当前的距离
threeD = cv2.reprojectImageTo3D(disparity.astype(np.float32)/16., camera_configs.Q)

cv2.imshow("left", img1_rectified)
cv2.imshow("right", img2_rectified)
cv2.imshow("depth", disp)

cv2.waitKey(0)
#
#
# camera1.release()
# camera2.release()
cv2.destroyAllWindows()