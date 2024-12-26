#importing required packages
import cv2
import numpy as np

#reading image in BGR and grayscale and resizing it
img = cv2.imread("Resources/lords.png")
imgGreyscale = cv2.imread("Resources/lords.png",0)
imgResized = cv2.resize(img, (600, 396))
imgGreyResized = cv2.resize(imgGreyscale, (600, 396))
imgGray = cv2.cvtColor(imgResized, cv2.COLOR_BGR2GRAY)
imgGrayReshaped = cv2.cvtColor(imgGreyResized,cv2.COLOR_GRAY2BGR)
#print(imgResized.shape,imgGrayReshaped.shape)

#stacking two images together
img2 = np.hstack((imgResized,imgGrayReshaped))
greyname = "Resources/GreyLords.png"
cv2.imshow("Lords", imgResized)
cv2.imshow("Grey Lords", imgGray)
cv2.imshow("Lords Ground", img2)
#image will be displayed for 5 seconds
cv2.waitKey(5000)
#save the grayscale image
cv2.imwrite(greyname, imgGray)
