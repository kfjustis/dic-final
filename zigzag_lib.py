'''
Source: http://wdxtub.com/interview/14520595473495.html
I modified this for functional design and converted it
to Python 3 with 2to3.
'''
# @param: a matrix of integers
# @return: a list of integers
def printZMatrix(matrix):
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
