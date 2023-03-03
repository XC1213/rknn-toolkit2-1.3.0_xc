import os
import urllib
import traceback
import time
import sys
import numpy as np
import cv2
from rknn.api import RKNN
from cv2 import getTickCount, getTickFrequency  # fps
import torch

IMG_PATH = './images'
save_images = './save_images/save1.jpg'
files = os.listdir(IMG_PATH)

for file in files:
    print(file)
    img = cv2.imread(IMG_PATH+"/"+file)
    # cv2.imshow("src", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
