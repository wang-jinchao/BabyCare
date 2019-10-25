import cv2
import numpy as np

import matlab.engine

def Height(centroids):
    eng = matlab.engine.start_matlab()
    eng.cd(r'/Users/wangjinchao/project/PycharmProjects/Paper/master/STERO', nargout = 0)
    # eng.ls(nargout = 0)
    # [centroids3D,centroids3D_t] = eng.steroVision(matlab.double(centroids),matlab.double(centroids_t),nargout=2)
    # [centroids3D,centroids3D_t] = eng.steroVision(centroids, centroids_t,nargout=2)
    centroids3D,fdx = eng.steroVision(matlab.double(centroids), nargout=2)
    centroids3D = np.array(centroids3D._data)
    # centroids3D_t = np.array(centroids3D_t._data)
    eng.quit()
    return centroids3D, fdx

# import matlab.engine
# eng = matlab.engine.start_matlab()
# future = eng.sqrt(4.0,background=True)
# ret = future.result()
#
# print(1+1)
# # tf = future.done()
# if future.done():
#     print(ret)