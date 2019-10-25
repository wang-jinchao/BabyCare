# filename: camera_configs.py
import cv2
import numpy as np

left_camera_matrix = np.array([[1371.44061411032,3.19796391528182,573.575012696487],
                               [0,1359.81614481812,253.611535292964],
                               [0,0,1]])
left_distortion = np.array([[0.0283093180345463	,0.0342398788902207,	-0.00289132504500225,	0.00494584129969822 ,   0.0228497075803429]])

right_camera_matrix = np.array([[1379.25590195365,2.72464457708726,633.515497386406],
                                [0,1366.96391618486,281.322992791120],
                                [0,0,1]])
right_distortion = np.array([[0.0210633260466918,	0.177236731930286,	-0.00290771460472166,	0.00448233121128710,    -0.672255679881776]])

R = np.array([[0.999964046714269,-0.00333981716069863,0.00779428637888376],
               [0.00330318476454348,0.999983461462424,0.00470805395457740],
               [-0.00780988151217659,-0.00468213871655113,0.999958540804470]])  # 旋转关系向量
# R = cv2.Rodrigues(om)[0]  # 使用Rodrigues变换将om变换为R
T = np.array([-58.0636028358932	,-0.076864979231634,	1.88946393284669])  # 平移关系向量

size = (480, 360)  # 图像尺寸

# 进行立体更正
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)
# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)