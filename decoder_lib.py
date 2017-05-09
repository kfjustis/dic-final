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
    eArr = []
    while i < len(arr1):
        error += math.pow(abs((int(arr1[i]) - int(arr2[i]))), 2)
        eArr.append(error)
        i += 1

    error = error / (math.pow(512, 2))

    plt.plot(eArr)
    plt.show()

    return error

def getPSNR(mse):
    if mse is None:
        return None

    psnr = 10 * math.log10(math.pow(255, 2) / mse)

    return psnr