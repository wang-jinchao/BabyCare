import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('../tl1.png',0)
imgR = cv2.imread('../tr1.png',0)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
print(disparity)
print(np.max(disparity, axis=1))
plt.imshow(disparity,'gray')
plt.show()