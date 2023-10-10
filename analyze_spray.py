import os
from PIL import ImageGrab
import cv2
import numpy as np
import time

IMG_PATH = r"E:\teachme2spray\pics\test.png"
IMG_DIR = r"E:\teachme2spray\pics"

def grab_spray_screenshot():
    pil_screenshot = ImageGrab.grab(bbox = (2550, 280, 2950, 475))
    screenshot_to_numpy = np.array(pil_screenshot.getdata(), dtype='uint8').reshape((pil_screenshot.size[1], pil_screenshot.size[0],3))
    return screenshot_to_numpy



# filename = "test2.png"
# pic = grab_spray_screenshot()  
# cv2.imshow("window", pic)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imwrite(filename, pic)

img = cv2.imread("test2.png")
orig_img = img
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
original_img = img
#img = cv2.GaussianBlur(img, (5,5), 0)
img = cv2.Canny(img, threshold1=50, threshold2=100)
# cv2.imshow('window', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()





contours, heigharchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


# cv2.imshow('window', threshed)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

s1 = 1
s2 = 25

xcnts = []



# for cnt in cnts:
#     if s1 < cv2.contourArea(cnt) < s2:
#         xcnts.append(cnt)
def distance(point_one, point_two):
    return ((point_one[0] - point_two[0]) ** 2 +
            (point_one[1] - point_two[1]) ** 2) ** 0.5


def total_distance(points):
    return sum(distance(p1, p2) for p1, p2 in zip(points, points[1:]))


print(len(contours))
centers = []
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    center = [x+w/2, y+h/2]
    centers.append(center)
    
print("TOTAL DIST", total_distance(centers))

# my_points = [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
# print(total_distance(my_points))

# centers = np.array(centers)


    
# cv2.drawContours(original_img, contours, -1, (0,255, 0), 3)
# cv2.imshow('contours', original_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# for cnt in xcnts:
#     print(cnt)
#     break
        
