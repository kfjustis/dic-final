import cv2
from PIL import Image
import numpy as np
import pywt

def load_image_as_array(imgFile):
    img = Image.open(imgFile)
    imgArray = np.asarray(img)

    return imgArray
