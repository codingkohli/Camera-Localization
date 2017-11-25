import numpy as np
import cv2
from matplotlib import pyplot as plt


pattern = cv2.imread('pattern.png',0)
img = cv2.imread('IMG_6723.JPG')
gray = cv2.imread('IMG_6723.JPG',0)
gray = np.float32(gray)
#using the harris corner detector
dst = cv2.cornerHarris(gray,2,3,0.08)

dst = cv2.dilate(dst,None)

img[dst>0.01*dst.max()]=[0,0,255]

"""cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
"""



