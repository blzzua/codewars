# https://www.codewars.com/kata/589d60c8665341ee

def test(large_img, small_img):
    for line1, line2 in zip(large_img, small_img):
        for pix1, pix2 in zip(line1, line2):
            if pix1 == True and pix2 != False:
                return 0
    return 1
    
def overlapping_images(large_img, small_img):
    diff1=len(large_img) - len(small_img)+1
    diff2=len(large_img[0]) - len(small_img[0])+1
    res = 0
    for d1 in range(diff1):
        for d2 in range(diff2):
            sub_img = [line[d2:]  for line in large_img[d1:]]
            res += test(sub_img,small_img)
    return res


# numpy stride_tricks.sliding_window_view solution
import numpy as np
def overlapping_images(large_img, small_img):    
    A = np.array(large_img, dtype=bool)
    B = np.array(small_img, dtype=bool)
    sliding_windows_view = np.lib.stride_tricks.sliding_window_view(A, B.shape)
    overlap_mask = sliding_windows_view & B
    valid_positions = ~np.any(overlap_mask, axis=(2, 3))
    return int(np.sum(valid_positions))
