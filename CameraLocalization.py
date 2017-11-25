import cv2
import numpy as np
from matplotlib import pyplot as mp
"""
Script to verfiy the install of numpy and opencv
print(np.__version__)
print("OpenCV Version: {}". format(cv2. __version__))
"""

#loading the image in grayscale
pattern = cv2.imread('pattern.png',0)
img = cv2.imread('IMG_6723.JPG',0)


w,h = pattern.shape[::-1]

#applying the method for comparison : making it dynamic to test our observations
method = cv2.TM_CCOEFF
#method = eval(method)
res = cv2.matchTemplate(img,pattern,method)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right =(top_left[0]+w,top_left[1]+h)
cv2.rectangle(img,top_left,bottom_right,255,2)
#displaying the result

#mp.subplot(121), mp.imshow(res, cmap='gray')
#mp.title('Matching Result'), mp.xticks([]), mp.yticks([])
#mp.subplot(122),
#mp.imshow(img, cmap='gray')
mp.imshow(img)
mp.title('Detected Point'), mp.xticks([]), mp.yticks([])
mp.scatter(top_left[1],top_left[0])
mp.scatter(bottom_right[1],bottom_right[0])
mp.show()


#print(top_left[1])
#print(res)
#end of script
cv2.waitKey(0)
cv2.destroyAllWindows()