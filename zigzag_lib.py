import math
import numpy as np

'''
Source: http://wdxtub.com/interview/14520595473495.html
I modified this for functional design then converted it
to Python 3 with 2to3.
'''
def generateZigMatrix(matrix):
    i = 0
    j = 0
    m = len(matrix)
    n = len(matrix[0])
    ret = []

    up = True
    for _ in range(m*n):
        ret.append(matrix[i][j])
        if up:
            if i-1<0 or j+1>=n:
                up = False
                if j+1>=n:  # go down
                    i += 1
                else:  # go right
                    j += 1
            else:
                i -= 1
                j += 1
        else:
            if i+1>=m or j-1<0:
                up = True
                if i+1>=m:
                    j += 1  # go right
                else:
                    i += 1  # go up
            else:
                i += 1
                j -= 1

    return ret

def iZigZag(matrix, qsize):
    # dimension 2D array from 1D length (length must be square)
    dim = int(math.sqrt(len(matrix)))

    k = False
    i = 0
    x = 0
    y = 0
    j = 0
    size = qsize
    count = 0

    # build 2d array
    ret = np.zeros(shape=(dim,dim), dtype="float")

    # top-left triangle of matrix
    while i < size:
        if k:
            x = 0
            y = i
            while x <= i:
                ret[x][y] = matrix[count]
                count += 1
                x += 1
                y -= 1
            k = False
        else:
            x = i
            y = 0
            while y <= i:
                ret[x][y] = matrix[count]
                count += 1
                x -= 1
                y += 1
            k = True
        i += 1

    # bottom-right triangle of matrix
    j = size - 2
    while j >= 0:
        if k:
            x = size - 1 - j
            y = size - 1
            while x <= size-1:
                ret[x][y] = matrix[count]
                count += 1
                x += 1
                y -= 1
            k = False
        else:
            x = size - 1 - j
            y = size - 1
            while y <= size-1:
                ret[x][y] = matrix[count]
                count += 1
                x -= 1
                y += 1
            k = True
        j -= 1

    return ret
