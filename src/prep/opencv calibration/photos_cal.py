import cv2
import glob
import time
import threading
import numpy as np
import sys
import os

print('Starting Capture...')
cap = cv2.VideoCapture(0)
while not cap.isOpened():  # 检查摄像头是否打开成功
    time.sleep(100)
    print('Camera is Initialize...')

width = int(cap.get(3))  # 读取摄像头分辨率参数
height = int(cap.get(4))

frame = np.zeros((width, height, 3), dtype=np.uint8)  # 创建图像模板
ret, frame = cap.read()

Key_val = 0  # 保存键值


def Keybo_Moni():  # 按键测试函数
    count = 0
    while True:
        global Key_val, frame, process_flag, cap
        if Key_val == ord('r'):
            Key_val = 0
            cv2.imwrite('ResPic' + str(count) + '.jpg', frame)  # 保存图像
            count += 1
            print('Get new pic %d' % count)


try:
    Keybo_Moni_Thread = threading.Thread(target=Keybo_Moni, name='Keyboard-Thread')  # 创建键盘监控线程
    Keybo_Moni_Thread.start()  # 启动键盘监测线程
except:
    print('Error:uqnable to start the thread!')

while True:
    ret, frame = cap.read()  # 读取视频帧
    cv2.imshow('Video_Show', frame)  # 显示图像
    Key_val = cv2.waitKey(1)  # 获取键值，不加此句，无法运行程序！(Ref:https://www.cnblogs.com/kissfu/p/3608016.html)
    if Key_val == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        print('Pic Sample Finished!')
        break

print('Starting CalibrateCamera...')

# 标定算法开始

# 设置寻找亚像素角点的参数，采用的停止准则是最大循环次数30和最大误差容限0.001
criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# 获取标定板角点的位置
ojbp = np.zeros((6 * 7, 3), np.float32)
# reshape(-1,N)转换矩阵的为N列的矩阵，-1表示可以代表任意行
# 比如有10个元素：
# reshape(-1,1)==>10*1的矩阵
# reshape(-1,2)===>5*2的矩阵
# T 表示将矩阵当中的所有的元素全部顺序反转一遍
# 将世界坐标系建在标定板上，所有点的Z坐标全部为0，所以只需要赋值x和y
ojbp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

objpoints = []  # 存储世界坐标系中的3D点(实际上Zw在标定板上的值为0)
imgpoints = []  # 存储图像坐标系中的2D点

images = glob.glob('*.jpg')
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imshow('gray', gray)
    cv2.waitKey(300)
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (7, 6), flags=3)
    # If found, add object points, image points(after refining them)
    if ret == True:
        if fname.find('ResPic') != -1:
            time_name = str(int(time.time()))
            cv2.imwrite(time_name + '.jpg', img)
            os.remove(fname)
        objpoints.append(ojbp)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)  # 亚像素级焦点检测，基于提取的角点，进一步提高精确度
        imgpoints.append(corners2)
        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (7, 6), corners2, ret)
        cv2.imshow('img', img)
        cv2.waitKey(500)
    else:
        os.remove(fname)

cv2.destroyAllWindows()

gray = cv2.cvtColor(cv2.imread(images[0]), cv2.COLOR_RGB2GRAY)
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print('retval:\n', ret)
print('Camera-Intrinsics:\n', mtx)
print('Camera-Distortion:\n', dist)
print('Camera-Extrinsics-R:')
N = 1
for r in rvecs:
    print('r' + str(N) + ':', r[0], r[1], r[2])
    N += 1
print('Camera-Extrinsics-t:')
N = 1
for t in tvecs:
    print('t' + str(N) + ':', t[0], t[1], t[2])
    N += 1
# Test The Result

# The Picture need to Correct
img = cv2.imread('./Calibsource/test2.jpg')
cv2.imshow('img', img)
cv2.waitKey(800)
cv2.destroyAllWindows()

h, w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
mothed = 'undistort'
print('Starting Correct Photo...')
if mothed != 'remapping':
    # undistort
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
    x, y, w, h = roi
    print('ROI\'Param:', roi)
    dst1 = dst[y:y + h, x:x + w]
    cv2.imwrite('./Calibresult/calibresult.jpg', dst1)
else:
    # undistort
    mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w, h), 5)
    dst = cv2.remap(img, mapx, mapy, cv2.INTER_CUBIC)
    # crop the image
    x, y, w, h = roi
    print('ROI\'Param:', roi)
    dst1 = dst[y:y + h, x:x + w]
    cv2.imwrite('./Calibresult/calibresult.jpg', dst1)

# gesture_Draw
print('Starting Gesture_Draw...')

# 绘制简单的坐标系，调用此函数记得将下面的坐标修改为axis_axis
axis_axis = np.float32([[3, 0, 0], [0, 3, 0], [0, 0, -3]]).reshape(-1, 3)


# 绘制简单的坐标系，调用此函数记得将下面的坐标修改为axis_axis
def draw_axis(img, corners, imgpts):
    corner = tuple(corners[0].ravel())
    img = cv2.line(img, corner, tuple(imgpts[0].ravel()), (255, 0, 0), 5)
    img = cv2.line(img, corner, tuple(imgpts[1].ravel()), (0, 255, 0), 5)
    img = cv2.line(img, corner, tuple(imgpts[2].ravel()), (0, 0, 255), 5)
    return img


# 绘制立体方块在Pattern上，调用此函数记得将下面的坐标修改为axis_cube
axis_cube = np.float32([[0, 0, 0], [0, 3, 0], [3, 3, 0], [3, 0, 0], [0, 0, -3], [0, 3, -3], [3, 3, -3], [3, 0, -3]])


# 绘制立体方块在Pattern上，调用此函数记得将下面的坐标修改为axis_cube
def draw_cube(img, corners, imgpts):
    imgpts = np.int32(imgpts).reshape(-1, 2)
    # draw ground floor in green
    img = cv2.drawContours(img, [imgpts[:4]], -1, (0, 255, 0), -3)
    # draw pillars in blue color
    for i, j in zip(range(4), range(4, 8)):
        img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]), (255), 3)
    # draw top layer in red color
    img = cv2.drawContours(img, [imgpts[4:]], -1, (0, 0, 255), 3)
    return img


criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((6 * 7, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

images = glob.glob('*.jpg')
if len(images) == 0:
    print('No Test Picture can be loading!')
    exit()
img = cv2.imread(images[0])
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)
if ret == True:
    corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    # Find the rotation and translation vectors.
    ret, rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners2, mtx, dist)
    # project 3D points to image plane
    imgpts, jac = cv2.projectPoints(axis_cube, rvecs, tvecs, mtx, dist)
    img = draw_cube(img, corners2, imgpts)
    cv2.imshow('img', img)
    cv2.waitKey(800)
    cv2.imwrite('./Calibresult/gesture.png', img)
cv2.destroyAllWindows()
print('Gesture_Draw Finised')
try:
    sys.exit(0)
except:
    print('Program is dead.')
finally:
    print('Clean-Up')