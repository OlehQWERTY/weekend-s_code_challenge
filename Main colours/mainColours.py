# pip install -U scikit-learn

#usage
# python color_mask.py --image maxresdefault.jpg 

import numpy as np
import argparse
import cv2
import time
 

timer1 = time.time()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
# load the image
image = cv2.imread(args["image"])

# h, w, _ = image.shape # aspect ratio
rH = 120
rW = 160
resizedImg = cv2.resize(image, (rW,rH))



# cv2.imshow("Main colours", resizedImgToShow)

# Reshape the image to be a list of pixels
# print(resizedImg)
# resizedImageArray = resizedImg.reshape((resizedImg.shape[0] * resizedImg.shape[1], 3))


sensitivity = 20
pxAmmount = rW * rH * 3
for x in range(rH):
	for y in range(rW):
		for z in range(3):
			if((resizedImg[x][y][z]%sensitivity) != 0):
				resizedImg[x][y][z] = int(resizedImg[x][y][z]/sensitivity)*sensitivity
colourArr = []

for x in range(int(rH/20)):
	blue = 0
	red = 0
	green = 0
	for y in range(rW):
		# for z in range(3):
		blue += resizedImg[x*20][y][0]
		red += resizedImg[x*20][y][1]
		green += resizedImg[x*20][y][2]
	blue = int(blue/rW)
	red = int(red/rW)
	green = int(green/rW)
	# print([blue,red,green])
	colourArr.append([blue,red,green])

print(colourArr)

# b = np.zeros([600,200,3])

# for i in range(6):
# 	for o in range(0,3):
# 		ko = i * 100
# 		b[range(ko, ko+100),:,o] = np.full((100,200), colourArr[i][o]) # 1111111111111111111111111
# 		# print(b[1])
# 		# print(i)
# 		# print(colourArr[i][o])


# # print(b[range(ko, ko+100),:,o])
# cv2.imshow("b", b)


# Create a black image
img = np.zeros((600,100,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
# cv2.line(img,(0,0),(511,511),(255,0,0),5)
for i in range(6):
	# for o in range(0,3):
	cv2.circle(img,(50,50+100*i), 50, (colourArr[i][0],colourArr[i][1],colourArr[i][2]), -1)

cv2.imshow("b", img)

# print(b)
# displayColourArr = []

# for i in range(6):
# 	for o in range(3):
# 		for x in range(60):
# 			for y in range(10):
# 				displayColourArr[x][y].append(colourArr[i][o])

# cv2.imshow("Main colours", displayColourArr)
# print(displayColourArr)

# (480/rH/10)
resizedImgToShow = cv2.resize(resizedImg, (640, 480))

cv2.imshow("Image", resizedImgToShow)

# print(resizedImageArray[0][1])

timer2 = time.time() - timer1

print(timer2)

cv2.waitKey(0)

# define the list of boundaries
# boundaries = [
# 	([17, 15, 100], [50, 56, 200]), #brg
# 	([86, 31, 4], [220, 88, 50]),
# 	([25, 146, 190], [62, 174, 250]),
# 	([103, 86, 65], [145, 133, 128])
# ]

# # loop over the boundaries
# for (lower, upper) in boundaries:
# 	# create NumPy arrays from the boundaries
# 	lower = np.array(lower, dtype = "uint8")
# 	upper = np.array(upper, dtype = "uint8")
 
# 	# find the colors within the specified boundaries and apply
# 	# the mask
# 	mask = cv2.inRange(image, lower, upper)
# 	output = cv2.bitwise_and(image, image, mask = mask)
 
# 	# show the images
# 	cv2.imshow("images", np.hstack([image, output]))
# 	cv2.waitKey(0)
