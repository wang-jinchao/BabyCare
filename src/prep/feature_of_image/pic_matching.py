
import numpy as np
import cv2

# Load the images in gray scale
# img1 = cv2.imread('../tsukuba_l.png', 0)
# img2 = cv2.imread('../tsukuba_r.png', 0)
img1 = cv2.imread('../tl1.png', 0)
img2 = cv2.imread('../tr1.png', 0)

# Detect the ORB key points and compute the descriptors for the two images
orb = cv2.ORB_create()
keyPoints1, descriptors1 = orb.detectAndCompute(img1, None)
keyPoints2, descriptors2 = orb.detectAndCompute(img2, None)

# Create brute-force matcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match the descriptors
matches = bf.match(descriptors1, descriptors2)

# Sort them in by distance
matches = sorted(matches, key=lambda x:x.distance)
print(matches[0].trainIdx)
print(matches[0].queryIdx)
print(matches[0].imgIdx)
print(keyPoints1[269].pt)
print(keyPoints2[222].pt)
#=====
print(matches[1].trainIdx)
print(matches[1].queryIdx)
print(matches[1].imgIdx)
print(keyPoints2[165].pt)
print(keyPoints1[188].pt)

# Draw the first 10 matches
result = cv2.drawMatches(img1, keyPoints1, img2, keyPoints2, matches[-2:], None, flags=2)

# for i in range(len(matches)):
#     print(matches[i].distance)
#     print('***'*12)
# Display the results
# cv2.namedWindow("BF matches10",0)
# cv2.resizeWindow('BF matches10',1280,360)
cv2.imshow('BF matches10', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
