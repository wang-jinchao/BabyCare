import cv2
img = cv2.imread('/home/wangjinchao/pred/examples.png', 0)
cv2.namedWindow("Image")   
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(thresh, 3, 2)
cnt = contours[0]
# 2.寻找凸包，得到凸包的角点
hull = cv2.convexHull(cnt)
# 3.绘制凸包
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, (0, 255, 0), 2)
cv2.imshow("Image", image)
cv2.waitKey (0)  
cv2.destroyAllWindows()