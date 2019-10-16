import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('./tl1.png',0)
imgR = cv2.imread('./tr1.png',0)

window_size = 3
min_disp = 16
num_disp = 112-min_disp
# (numDisparities=16, blockSize=15)
stereo = cv2.StereoSGBM_create(
# stereo = cv2.StereoBM_create(
    # minDisparity = min_disp,
    # numDisparities = num_disp,
    numDisparities = 16,
    blockSize =22,
    # P1 = 8*3*window_size**2,
    # P2 = 32*3*window_size**2,
    # disp12MaxDiff = 1,
    # uniquenessRatio = 10,
    # speckleWindowSize = 100,
    # speckleRange = 32
)

print('computing disparity...')
disparity = stereo.compute(imgL, imgR).astype(np.float32) / 16.0


plt.imshow(disparity,'gray')
plt.show()