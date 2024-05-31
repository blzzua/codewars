# https://www.codewars.com/kata/5895326bcc949f496b00003e

def box_blur(image):
    res = []
    for i, line in enumerate(image[1:-1], 1):
        new_line = []
        for j, val in enumerate(line[1:-1], 1):
            new_line.append( (image[i-1][j-1] + image[i-1][j] + image[i-1][j + 1] + \
                              image[i][j-1]   + image[i][j]   + image[i][j + 1]   + \
                              image[i+1][j-1] + image[i+1][j] + image[i+1][j + 1]) // 9) 
        res.append(new_line)
    return res


# clever lib
# from scipy.ndimage import convolve
# return convolve(image, [[1, 1, 1], [1, 1, 1], [1, 1, 1]] )[1:-1, 1:-1]//9
