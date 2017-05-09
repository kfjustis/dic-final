import cv2
from PIL import Image
import math
import matplotlib.pyplot as plt
import numpy as np

def getImageError(img1_arr, img2_arr):
    if img1_arr is None or img2_arr is None:
        return None

    arr1 = img1_arr.ravel()
    arr2 = img2_arr.ravel()

    i = 0
    error = 0.0
    while i < len(arr1):
        error += math.exp(abs(int(arr1[i]) - int(arr2[i])))
        error = error / len(arr1)
        i += 1

    #ret = total/(math.pow(512, 2))
    return error
