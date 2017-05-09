import os.path
import cv2
import stasm
import numpy as np
path = '33.jpg'

img1 = cv2.imread(path)
img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

if img is None:
    print("Cannot load", path)
    raise SystemExit

landmarks = stasm.search_single(img)

if len(landmarks) == 0:
    print("No face found in", path)
else:
    landmarks = stasm.force_points_into_image(landmarks, img)
    landmarks = np.concatenate((landmarks[:60],landmarks[80:]),axis=0)
    for point in landmarks:
	x = int(round(point[1]))
	y = int(round(point[0]))
        img1[x][y] = 0
	img1[x+1][y] = 0
	img1[x][y+1] = 0
	img1[x-1][y] = 0
	img1[x][y-1] = 0
	img1[x+1][y-1] = 0
	img1[x-1][y+1] = 0
	img1[x+1][y+1] = 0
	img1[x-1][y-1] = 0

cv2.imshow("stasm minimal", img1)
cv2.waitKey(0)
